# -*- coding: utf8 -*-

import unittest
try:
    from unittest import mock
except ImportError:
    import mock

# Used in the tests
from mock import patch

from click.testing import CliRunner


class CliTestCase(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        # Mock the OVH client
        patcher = mock.patch('ovhcli.context.OvhContext.get_ovh_client')
        self.addCleanup(patcher.stop)
        self.mock_client = patcher.start()

        self.runner = CliRunner()
