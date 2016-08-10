# -*- coding: utf8 -*-

from ovhcli.modules import OvhModule


class Webhosting(OvhModule):

    @classmethod
    def list(cls):
        return cls.client.get('/hosting/web')

    @classmethod
    def info(cls, service):
        return cls.client.get('/hosting/web/{}'.format(
            service
        ))

    @classmethod
    def quota(cls, service):
        info = cls.info(service)
        quota = {
            'used': info['quotaUsed'],
            'size': info['quotaSize'],
        }

        return quota

    @classmethod
    def countries(cls, service):
        info = cls.info(service)
        return info['countriesIp']

    @classmethod
    def get_user(cls, service, username):
        url = '/hosting/web/{}/user/{}'.format(service, username)
        return cls.client.get(url)

    @classmethod
    def get_users(cls, service, full=False):
        usernames = cls.client.get('/hosting/web/{}/user'.format(
            service
        ))

        # Return only usernames by default
        if not full:
            return usernames

        # Otherwise fetch all information by user
        users = [cls.get_user(service, username) for username in usernames]

        return users

    @classmethod
    def create_user(cls, service, login, password, home, ssh):
        url = '/hosting/web/{}/user'.format(service)
        ssh = 'active' if ssh else 'none'

        params = {
            'home': home,
            'login': login,
            'password': password,
            'sshState': ssh
        }

        task = cls.client.post(url, **params)
        return task

    @classmethod
    def update_user(cls, ovh, service, login, home, ssh, state):
        url = '/hosting/web/{}/user/{}'.format(service, login)
        params = {}

        if home:
            params['home'] = home

        if ssh:
            ssh = 'active' if ssh else 'none'
            params['sshState'] = ssh

        if state:
            state = 'rw' if state else 'off'
            params['state'] = state

        cls.client.put(url, **params)
        return True

    @classmethod
    def remove_user(cls, ovh, service, login):
        url = '/hosting/web/{}/user/{}'.format(service, login)
        return cls.client.delete(url)

    @classmethod
    def config(cls, service, historical=False, all=False):
        configs = []
        params = {}

        if not all:
            if historical:
                params['historical'] = 'true'
            else:
                params['historical'] = 'false'

        conf_ids = cls.client.get('/hosting/web/{}/ovhConfig'.format(
            service,
        ), **params)

        for _id in conf_ids:
            conf = cls.client.get('/hosting/web/{}/ovhConfig/{}'.format(
                service,
                _id
            ))
            configs.append(conf)

        return configs

    @classmethod
    def update_config(cls, service, ovh_config=None, container=None,
                      engine=None, engine_version=None, environment=None,
                      firewall=None):
        params = {}

        # Get the last ovhConfig ID if not provided
        if not ovh_config:
            ovh_config = cls.config(service)[0]['id']

        if container:
            params['container'] = container

        if engine:
            params['engineName'] = engine

        if engine_version:
            params['engineVersion'] = engine_version

        if environment:
            params['environment'] = environment

        if firewall:
            params['httpFirewall'] = firewall

        # Change the service configuration
        url = '/hosting/web/{}/ovhConfig/{}/changeConfiguration'.format(
            service,
            ovh_config
        )

        task = cls.client.post(url, **params)
        return task
