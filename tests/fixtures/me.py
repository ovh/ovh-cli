# -*- coding: utf-8 -*-


def info():
    return {
        'country': 'FR',
        'firstname': 'John',
        'legalform': 'individual',
        'name': 'Doe',
        'currency': {
            'code': 'EUR',
            'symbol': 'EURO'
        },
        'ovhSubsidiary': 'FR',
        'birthDay': None,
        'organisation': '',
        'spareEmail': None,
        'area': '',
        'phone': '+33.123456789',
        'nationalIdentificationNumber': None,
        'ovhCompany': 'ovh',
        'email': 'john@doe.com',
        'companyNationalIdentificationNumber': None,
        'language': 'fr_FR',
        'fax': '',
        'zip': '59100',
        'nichandle': 'dj12345-ovh',
        'corporationType': None,
        'sex': None,
        'birthCity': None,
        'state': 'complete',
        'city': 'Roubaix',
        'vat': '',
        'address': '2 rue Kellermann'
    }


def get_applications():
    return [
        {
            'status': 'active',
            'applicationKey': 'j1sWWzqb1dw0GyUI',
            'applicationId': 20001,
            'name': 'foobar-1',
            'description': 'Lorem ipsum 1'
        }, {
            'status': 'active',
            'applicationKey': '1BAbFJLrfvOr9vu0',
            'applicationId': 20003,
            'name': 'foobar-3',
            'description': 'Lorem ipsum 3'
        }, {
            'status': 'active',
            'applicationKey': 'Cpc4mPw9vdoaLwy0',
            'applicationId': 20002,
            'name': 'foobar-2',
            'description': 'Lorem ipsum 2'
        }
    ]


def get_credentials(app_id):
    return [cred for cred in [
        {
            'ovhSupport': False,
            'rules': [
                {
                    'method': 'GET', 'path': '/*'
                }, {
                    'method': 'POST', 'path': '/*'
                }, {
                    'method': 'PUT', 'path': '/*'
                }, {
                    'method': 'DELETE', 'path': '/*'
                }
            ],
            'expiration': '2016-08-04T17:52:21+02:00',
            'status': 'validated',
            'credentialId': 50000002,
            'applicationId': 20001,
            'creation': '2016-08-03T17:52:21+02:00',
            'lastUse': '2016-08-03T17:51:12+02:00'
         }, {
            'ovhSupport': True,
            'rules': [
                {
                    'method': 'GET', 'path': '/*'
                }, {
                    'method': 'POST', 'path': '/*'
                }, {
                    'method': 'PUT', 'path': '/*'
                }, {
                    'method': 'DELETE', 'path': '/*'
                }
            ],
            'expiration': '2016-08-04T17:47:33+02:00',
            'status': 'validated',
            'credentialId': 50000001,
            'applicationId': 20001,
            'creation': '2016-08-03T17:47:33+02:00',
            'lastUse': '2016-08-03T17:50:23+02:00'
        }
    ] if cred['applicationId'] == int(app_id)]


def get_application(app_id):
    return next((app for app in get_applications()
                 if app['applicationId'] == int(app_id)))


def get_credential(credential_id):
    return next((app for app in get_credentials('20001')
                 if app['credentialId'] == int(credential_id)))


def get_rules(credential_id):
    return next((app for app in get_credentials('20001')
                 if app['credentialId'] == int(credential_id)))['rules']
