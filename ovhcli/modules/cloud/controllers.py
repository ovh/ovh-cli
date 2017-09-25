# -*- coding: utf8 -*-

from ovhcli.modules import OvhModule


class Cloud(OvhModule):

    @classmethod
    def projects(cls):
        return cls.client.get('/cloud/project')

    @classmethod
    def instances(cls, project):
        return cls.client.get('/cloud/project/{}/instance'.format(
            project
        ))

    @classmethod
    def flavors(cls, project, region):
        url = '/cloud/project/{}/flavor'.format(
            project
        )

        params = {}
        if region:
            params['region'] = region

        return cls.client.get(url, **params)

    @classmethod
    def regions(cls, project):
        return cls.client.get('/cloud/project/{}/region'.format(
            project
        ))
