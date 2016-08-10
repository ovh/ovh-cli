# -*- coding: utf-8 -*-

from ovhcli.modules.setup import commands

from ..base import CliTestCase
from ..base import patch


class SetupTest(CliTestCase):

    @patch('ovhcli.modules.setup.commands.config_file_exists')
    def test_conf_already_exists(self, mock):
        mock.return_value = True
        result = self.runner.invoke(commands.init)

        self.assertEqual(result.output, """\
[error] A configuration file already exists (use --force to erase it).
""")

    @patch('ovhcli.modules.setup.commands.config_file_exists')
    @patch('ovhcli.modules.setup.commands.click')
    def test_erase_conf_file(self, mock_file_exists, mock_click):
        mock_file_exists.return_value = True
        mock_click.prompt.side_effect = exit
        result = self.runner.invoke(commands.init, ['--force'])

        self.assertTrue(result.output.startswith("""\
[warning] The configuration file will be erased.
"""))

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    def test_setup_1(self):
        inputs = '1\novh-eu\nCHOICE1_AK\nCHOICE1_AS\nCHOICE1_CK\n'

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(commands.init, input=inputs)
            self.assertEqual(result.output, """\
{welcome}
Your choice [1]: 1

Endpoint [ovh-eu]: ovh-eu
Application key: CHOICE1_AK
Application secret: CHOICE1_AS
Consumer key: CHOICE1_CK
[*] Configuration file created.
""".format(welcome=commands.WELCOME_MESSAGE))

            with open('./testing.conf', 'r') as f:
                self.assertEqual(f.read(), """\
[default]
endpoint=ovh-eu

[ovh-eu]
application_key=CHOICE1_AK
application_secret=CHOICE1_AS
consumer_key=CHOICE1_CK

[ovh-cli]
""")

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    @patch('ovhcli.modules.setup.utils.get_ck_validation')
    def test_setup_2(self, mock_ck):
        mock_ck.return_value = {'validationUrl': 'https://eu.api.ovh.com/auth/?credentialToken=IwUoqGPCh2x0aAyTwkJN1vngnVv4RLHepdILexvmx2it6jMNAyL2yeBTfNQ7Hv0b',
                                'consumerKey': 'CHOICE2_CK'}

        inputs = '2\novh-eu\nCHOICE2_AK\nCHOICE2_AS\nc\n'

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(commands.init, input=inputs)
            self.assertEqual(result.output, """\
{welcome}
Your choice [1]: 2

Endpoint [ovh-eu]: ovh-eu
Application key: CHOICE2_AK
Application secret: CHOICE2_AS

[-] Please visit the following link to authenticate you and validate the token :
[-] https://eu.api.ovh.com/auth/?credentialToken=IwUoqGPCh2x0aAyTwkJN1vngnVv4RLHepdILexvmx2it6jMNAyL2yeBTfNQ7Hv0b
[*] Configuration file created.
""".format(welcome=commands.WELCOME_MESSAGE))

            with open('./testing.conf', 'r') as f:
                self.assertEqual(f.read(), """\
[default]
endpoint=ovh-eu

[ovh-eu]
application_key=CHOICE2_AK
application_secret=CHOICE2_AS
consumer_key=CHOICE2_CK

[ovh-cli]
""")

    @patch('ovhcli.modules.setup.utils.CONFIG_PATH', './testing.conf')
    def test_setup_3(self):
        inputs = '3\novh-eu\nCHOICE3_AK\nCHOICE3_AS\nCHOICE3_CK\n'

        with self.runner.isolated_filesystem():
            result = self.runner.invoke(commands.init, input=inputs)
            self.assertEqual(result.output, """\
{welcome}
Your choice [1]: 3

[-] Please visit the following link to authenticate you and obtain your keys (AK, AS and CK) :
[-] https://api.ovh.com/createToken/index.cgi?GET=/*&POST=/*&PUT=/*&DELETE=/*

Endpoint [ovh-eu]: ovh-eu
Application key: CHOICE3_AK
Application secret: CHOICE3_AS
Consumer key: CHOICE3_CK
[*] Configuration file created.
""".format(welcome=commands.WELCOME_MESSAGE))

            with open('./testing.conf', 'r') as f:
                self.assertEqual(f.read(), """\
[default]
endpoint=ovh-eu

[ovh-eu]
application_key=CHOICE3_AK
application_secret=CHOICE3_AS
consumer_key=CHOICE3_CK

[ovh-cli]
""")
