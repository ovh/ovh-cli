# -*- coding: utf-8 -*-

from click.exceptions import UsageError

from ovhcli.modules.setup.utils import (check_choice, check_endpoint,
                                        config_file_exists, create_config_file)

from ..base import CliTestCase
from ..base import patch
from ..fixtures.setup import FAKE_ENDPOINTS


class SetupTest(CliTestCase):

    def test_check_valid_choices(self):
        self.assertEqual(check_choice('1'), 1)
        self.assertEqual(check_choice('2'), 2)
        self.assertEqual(check_choice('3'), 3)

    def test_check_invalid_choice(self):
        self.assertRaises(UsageError, check_choice, 'foobar')

    @patch('ovhcli.modules.setup.utils.ENDPOINTS', FAKE_ENDPOINTS)
    def test_check_valid_endpoints(self):
        self.assertEqual(check_endpoint('ENDPOINT1'), 'ENDPOINT1')
        self.assertEqual(check_endpoint('ENDPOINT2'), 'ENDPOINT2')

    @patch('ovhcli.modules.setup.utils.ENDPOINTS', FAKE_ENDPOINTS)
    def test_check_invalid_endpoint(self):
        self.assertRaises(UsageError, check_endpoint, 'foobar')

        with self.assertRaises(UsageError) as cm:
            check_endpoint('foobar')
        self.assertEqual('This endpoint does not exist (ENDPOINT1, ENDPOINT2)',
                         str(cm.exception))

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    def test_check_config_file_exists(self):
        with self.runner.isolated_filesystem():
            with open('./testing.conf', 'w') as f:
                f.write('foobar')

            self.assertTrue(config_file_exists())

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    def test_check_config_file_not_exists(self):
            self.assertFalse(config_file_exists())

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    def test_check_create_config_file(self):
            with self.runner.isolated_filesystem():
                result = create_config_file('foobar', 'app_key', 'app_secret',
                                            'consumer_key')

                self.assertTrue(result)

                with open('./testing.conf', 'r') as f:
                    self.assertEqual(f.read(), """\
[default]
endpoint=foobar

[foobar]
application_key=app_key
application_secret=app_secret
consumer_key=consumer_key

[ovh-cli]
""")
