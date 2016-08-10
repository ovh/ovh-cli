# -*- coding: utf8 -*-

from ovhcli.modules import OvhModule


class Me(OvhModule):

    @classmethod
    def info(cls):
        return cls.client.get('/me')

    @classmethod
    def get_application(cls, application_id):
        url = '/me/api/application/{}'.format(application_id)
        return cls.client.get(url)

    @classmethod
    def get_applications(cls):
        apps = [cls.get_application(app)
                for app in cls.client.get('/me/api/application')]

        return apps

    @classmethod
    def get_credential(cls, credential_id):
        url = '/me/api/credential/{}'.format(credential_id)
        return cls.client.get(url)

    @classmethod
    def get_credentials(cls, application_id=None):
        params = {}

        if application_id:
            # Check if this App exists
            app = cls.get_application(application_id)

            params['applicationId'] = app['applicationId']

        credentials = cls.client.get('/me/api/credential', **params)

        data = [cls.get_credential(credential) for credential in credentials]
        return data

    @classmethod
    def get_rules(cls, credential_id):
        credential = cls.get_credential(credential_id)
        return credential['rules']
