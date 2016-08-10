# -*- coding: utf-8 -*-


def list():
    return [
        'ovh.com',
        'mydomain.fr',
        'johndoe.ovh'
    ]


def info():
    return {
        'quotaUsed': {
            'unit': 'MB',
            'value': 37.4374389648438
        },
        'cluster': 'cluster006',
        'boostOffer': None,
        'displayName': None,
        'clusterIpv6': '2001:41d0:1:1b00:213:186:33:17',
        'datacenter': 'p19',
        'token': 'NWdPiouPiouSiDeuEy/2Pg',
        'resourceType': 'shared',
        'recommendedOffer': None,
        'trafficQuotaSize': None,
        'availableBoostOffer': [],
        'home': '/homez.2049/johndoe',
        'trafficQuotaUsed': None,
        'hasCdn': False,
        'filer': '2049',
        'serviceName': 'mydomain.fr',
        'offer': 'perso2014',
        'hostingIpv6': '2001:41d0:1:1b00:213:184:33:14',
        'primaryLogin': 'johndoe',
        'state': 'active',
        'countriesIp': [
            {
                'ipv6': '2001:41d0:1:1b00:188:165:7:17',
                'ip': '188.165.7.17',
                'country': 'IE'
            }, {
                'ipv6': '2001:41d0:1:1b00:94:23:79:17',
                'ip': '94.23.79.17',
                'country': 'PT'
            }, {
                'ipv6': '2001:41d0:1:1b00:87:98:255:17',
                'ip': '87.98.255.17',
                'country': 'UK'
            }, {
                'ipv6': '2001:41d0:1:1b00:94:23:64:17',
                'ip': '94.23.64.17',
                'country': 'IT'
            }, {
                'ipv6': '2001:41d0:1:1b00:87:98:231:17',
                'ip': '87.98.231.17',
                'country': 'ES'
            }, {
                'ipv6': '2001:41d0:1:1b00:87:98:239:17',
                'ip': '87.98.239.17',
                'country': 'PL'
            }, {
                'ipv6': '2001:41d0:1:1b00:94:23:175:17',
                'ip': '94.23.175.17',
                'country': 'CZ'
            }, {
                'ipv6': '2001:41d0:1:1b00:94:23:151:17',
                'ip': '94.23.151.17',
                'country': 'NL'
            }, {
                'ipv6': '2001:41d0:1:1b00:188:165:143:17',
                'ip': '188.165.143.17',
                'country': 'FI'
            }, {
                'ipv6': '2001:41d0:1:1b00:188:165:31:17',
                'ip': '188.165.31.17',
                'country': 'LT'
            }, {
                'ipv6': '2001:41d0:1:1b00:213:186:33:17',
                'ip': '213.186.33.17',
                'country': 'FR'
            }, {
                'ipv6': '2001:41d0:1:1b00:87:98:247:17',
                'ip': '87.98.247.17',
                'country': 'DE'
            }
        ],
        'hasHostedSsl': False,
        'operatingSystem': 'linux',
        'phpVersions': [
            {
                'version': '5.3',
                'support': 'END_OF_LIFE'
            }, {
                'version': '5.5',
                'support': 'SECURITY_FIXES'
            }, {
                'version': '5.2',
                'support': 'END_OF_LIFE'
            }, {
                'version': '7.0',
                'support': 'SUPPORTED'
            }, {
                'version': '5.4',
                'support': 'END_OF_LIFE'
            }, {
                'version': '5.6',
                'support': 'SUPPORTED'
            }, {
                'version': '4.4',
                'support': 'END_OF_LIFE'
            }
        ],
        'quotaSize': {
            'unit': 'GB',
            'value': 100
        },
        'clusterIp': '213.186.33.17',
        'hostingIp': '213.186.33.17'
    }


def get_users(full=False):
    if full:
        return [
            {
                'iisRemoteRights': None,
                'webDavRights': None,
                'isPrimaryAccount': False,
                'home': 'foo',
                'sshState': 'active',
                'state': 'rw',
                'login': 'johndoe-foo'
            }, {
                'iisRemoteRights': None,
                'webDavRights': None,
                'isPrimaryAccount': False,
                'home': '.',
                'sshState': 'none',
                'state': 'rw',
                'login': 'johndoe'
            }
        ]

    return ['johndoe-foo', 'johndoe']


def config():
    return [
        {
            'path': '',
            'creationDate': '2016-08-04T19:54:48+02:00',
            'httpFirewall': 'none',
            'environment': 'production',
            'id': 2000001,
            'container': 'legacy',
            'fileExist': True,
            'engineVersion': '5.6',
            'engineName': 'php',
            'historical': False
        }
    ]
