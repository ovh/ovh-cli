# -*- coding: utf-8 -*-

from ovhcli.modules.webhosting import commands
from ovhcli.modules.webhosting.controllers import Webhosting

from ..base import CliTestCase
from ..base import patch
from ..fixtures.webhosting import list as _list, info, get_users, config


class WebhostingTest(CliTestCase):

    @patch.object(Webhosting, 'list')
    def test_list_services(self, mock):
        mock.return_value = _list()
        result = self.runner.invoke(commands.list)
        self.assertEqual(result.output, """\
+-------------+
| Services    |
+-------------+
| johndoe.ovh |
| mydomain.fr |
| ovh.com     |
+-------------+
""")

    @patch.object(Webhosting, 'info')
    def test_show_service(self, mock):
        mock.return_value = info()
        result = self.runner.invoke(commands.info, ['mydomain.fr'])
        self.assertEqual(result.output, """\
+---------------------+-------------------------------------------+
| Property            | Value                                     |
+---------------------+-------------------------------------------+
| availableBoostOffer |                                           |
| boostOffer          |                                           |
| cluster             | cluster006                                |
| clusterIp           | 213.186.33.17                             |
| clusterIpv6         | 2001:41d0:1:1b00:213:186:33:17            |
| datacenter          | p19                                       |
| displayName         |                                           |
| filer               | 2049                                      |
| hasCdn              | False                                     |
| hasHostedSsl        | False                                     |
| home                | /homez.2049/johndoe                       |
| hostingIp           | 213.186.33.17                             |
| hostingIpv6         | 2001:41d0:1:1b00:213:184:33:14            |
| offer               | perso2014                                 |
| operatingSystem     | linux                                     |
| primaryLogin        | johndoe                                   |
| quotaSize           | {"unit": "GB", "value": 100}              |
| quotaUsed           | {"unit": "MB", "value": 37.4374389648438} |
| recommendedOffer    |                                           |
| resourceType        | shared                                    |
| serviceName         | mydomain.fr                               |
| state               | active                                    |
| token               | NWdPiouPiouSiDeuEy/2Pg                    |
| trafficQuotaSize    |                                           |
| trafficQuotaUsed    |                                           |
+---------------------+-------------------------------------------+
""")

    @patch.object(Webhosting, 'info')
    def test_show_quota(self, mock):
        mock.return_value = info()
        result = self.runner.invoke(commands.quota, ['mydomain.fr'])
        self.assertEqual(result.output, """\
+------+-----------+
| Used | 37.44 MB  |
+------+-----------+
| Size | 100.00 GB |
+------+-----------+
""")

    @patch.object(Webhosting, 'info')
    def test_list_countries(self, mock):
        mock.return_value = info()
        result = self.runner.invoke(commands.countries, ['mydomain.fr'])
        self.assertEqual(result.output, """\
+---------+----------------+---------------------------------+
| country | ip             | ipv6                            |
+---------+----------------+---------------------------------+
| CZ      | 94.23.175.17   | 2001:41d0:1:1b00:94:23:175:17   |
| DE      | 87.98.247.17   | 2001:41d0:1:1b00:87:98:247:17   |
| ES      | 87.98.231.17   | 2001:41d0:1:1b00:87:98:231:17   |
| FI      | 188.165.143.17 | 2001:41d0:1:1b00:188:165:143:17 |
| FR      | 213.186.33.17  | 2001:41d0:1:1b00:213:186:33:17  |
| IE      | 188.165.7.17   | 2001:41d0:1:1b00:188:165:7:17   |
| IT      | 94.23.64.17    | 2001:41d0:1:1b00:94:23:64:17    |
| LT      | 188.165.31.17  | 2001:41d0:1:1b00:188:165:31:17  |
| NL      | 94.23.151.17   | 2001:41d0:1:1b00:94:23:151:17   |
| PL      | 87.98.239.17   | 2001:41d0:1:1b00:87:98:239:17   |
| PT      | 94.23.79.17    | 2001:41d0:1:1b00:94:23:79:17    |
| UK      | 87.98.255.17   | 2001:41d0:1:1b00:87:98:255:17   |
+---------+----------------+---------------------------------+
""")

    @patch.object(Webhosting, 'get_users')
    def test_list_users(self, mock):
        mock.return_value = get_users()
        result = self.runner.invoke(commands.get_users, ['mydomain.fr'])
        self.assertEqual(result.output, """\
+-------------+
| Users       |
+-------------+
| johndoe     |
| johndoe-foo |
+-------------+
""")

    @patch.object(Webhosting, 'get_users')
    def test_list_full_users(self, mock):
        mock.return_value = get_users(full=True)
        args = ['mydomain.fr', '--full']
        result = self.runner.invoke(commands.get_users, args)
        self.assertEqual(result.output, """\
+-------------+------+-------+--------+-----------------+
| Login       | Home | State | Ssh    | Primary account |
+-------------+------+-------+--------+-----------------+
| johndoe     | .    | rw    | none   | False           |
| johndoe-foo | foo  | rw    | active | False           |
+-------------+------+-------+--------+-----------------+
""")

    @patch.object(Webhosting, 'config')
    def test_list_config(self, mock):
        mock.return_value = config()
        result = self.runner.invoke(commands.config, ['mydomain.fr'])
        self.assertEqual(result.output, """\
+---------+-------------+----------------+-----------+------+--------+----------+
| #ID     | Environment | Engine version | Container | Path | Engine | Firewall |
+---------+-------------+----------------+-----------+------+--------+----------+
| 2000001 | production  | 5.6            | legacy    |      | php    | none     |
+---------+-------------+----------------+-----------+------+--------+----------+
""")

    @patch.object(Webhosting, 'update_config')
    def test_update_config(self, mock):
        mock.return_value = True
        args = ['mydomain.fr', '--confirm']
        result = self.runner.invoke(commands.update_config, args)
        self.assertEqual(result.output, """\
[*] The configuration will be updated in a few seconds.
""")

    @patch.object(Webhosting, 'create_user')
    def test_create_user(self, mock):
        mock.return_value = True
        args = ['mydomain.fr', '-l', 'foobar', '--confirm']
        input = 'password1234\npassword1234\n'
        result = self.runner.invoke(commands.create_user, args, input=input)
        self.assertEqual('\n'.join(
            [s.strip() for s in result.output.split('\n')]
        ), """\
Password:
Repeat for confirmation:
[*] User foobar will be created in a few seconds.
""")

    @patch.object(Webhosting, 'remove_user')
    def test_remove_user(self, mock):
        mock.return_value = True
        args = ['mydomain.fr', '-l', 'foobar', '--confirm']
        result = self.runner.invoke(commands.remove_user, args)
        self.assertEqual(result.output, """\
[*] User foobar will be removed in a few seconds.
""")

    @patch.object(Webhosting, 'update_user')
    def test_update_user(self, mock):
        mock.return_value = True
        args = ['mydomain.fr', '-l', 'foobar', '--confirm']
        result = self.runner.invoke(commands.update_user, args)
        self.assertEqual(result.output, """\
[*] Information about foobar will be updated in a few seconds.
""")
