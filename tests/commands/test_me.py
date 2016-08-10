# -*- coding: utf-8 -*-

from ovhcli.modules.me import commands
from ovhcli.modules.me.controllers import Me

from ..base import CliTestCase
from ..base import patch
from ..fixtures.me import (info, get_applications, get_application,
                           get_credentials, get_rules)


class MeTest(CliTestCase):

    @patch.object(Me, 'info')
    def test_show_info(self, mock):
        mock.return_value = info()
        result = self.runner.invoke(commands.info)
        self.assertEqual(result.output, """\
[*] Welcome here John
+-----------------+-----------------------------------+
| Property        | Value                             |
+-----------------+-----------------------------------+
| address         | 2 rue Kellermann                  |
| area            |                                   |
| birthCity       |                                   |
| birthDay        |                                   |
| city            | Roubaix                           |
| corporationType |                                   |
| country         | FR                                |
| currency        | {"code": "EUR", "symbol": "EURO"} |
| email           | john@doe.com                      |
| fax             |                                   |
| firstname       | John                              |
| language        | fr_FR                             |
| legalform       | individual                        |
| name            | Doe                               |
| nichandle       | dj12345-ovh                       |
| organisation    |                                   |
| ovhCompany      | ovh                               |
| ovhSubsidiary   | FR                                |
| phone           | +33.123456789                     |
| sex             |                                   |
| spareEmail      |                                   |
| state           | complete                          |
| vat             |                                   |
| zip             | 59100                             |
+-----------------+-----------------------------------+
""")

    @patch.object(Me, 'get_applications')
    def test_list_applications(self, mock):
        mock.return_value = get_applications()
        result = self.runner.invoke(commands.applications)
        self.assertEqual(result.output, """\
+---------------+------------------+---------------+----------+--------+
| applicationId | applicationKey   | description   | name     | status |
+---------------+------------------+---------------+----------+--------+
| 20003         | 1BAbFJLrfvOr9vu0 | Lorem ipsum 3 | foobar-3 | active |
| 20002         | Cpc4mPw9vdoaLwy0 | Lorem ipsum 2 | foobar-2 | active |
| 20001         | j1sWWzqb1dw0GyUI | Lorem ipsum 1 | foobar-1 | active |
+---------------+------------------+---------------+----------+--------+
""")

    @patch.object(Me, 'get_application')
    def test_show_application(self, mock):
        mock.return_value = get_application('20001')
        result = self.runner.invoke(commands.application, ['20001'])
        self.assertEqual(result.output, """\
+----------------+------------------+
| Property       | Value            |
+----------------+------------------+
| applicationId  | 20001            |
| applicationKey | j1sWWzqb1dw0GyUI |
| description    | Lorem ipsum 1    |
| name           | foobar-1         |
| status         | active           |
+----------------+------------------+
""")

    @patch.object(Me, 'get_credentials')
    def test_list_credentials(self, mock):
        mock.return_value = get_credentials('20001')
        result = self.runner.invoke(commands.credentials, ['20001'])
        self.assertEqual(result.output, """\
+---------------------------+--------------+---------------------------+---------------------------+-----------+
| creation                  | credentialId | expiration                | lastUse                   | status    |
+---------------------------+--------------+---------------------------+---------------------------+-----------+
| 2016-08-03T17:52:21+02:00 | 50000002     | 2016-08-04T17:52:21+02:00 | 2016-08-03T17:51:12+02:00 | validated |
| 2016-08-03T17:47:33+02:00 | 50000001     | 2016-08-04T17:47:33+02:00 | 2016-08-03T17:50:23+02:00 | validated |
+---------------------------+--------------+---------------------------+---------------------------+-----------+
""")

    @patch.object(Me, 'get_rules')
    def test_list_rules(self, mock):
        mock.return_value = get_rules('50000001')
        result = self.runner.invoke(commands.rules, ['50000001'])
        self.assertEqual(result.output, """\
+--------+------+
| method | path |
+--------+------+
| GET    | /*   |
| POST   | /*   |
| PUT    | /*   |
| DELETE | /*   |
+--------+------+
""")
