# -*- coding: utf8 -*-

from ovhcli.modules import OvhModule


class Domain(OvhModule):

    @classmethod
    def list(cls):
        return cls.client.get('/domain')


