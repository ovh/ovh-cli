# -*- coding: utf8 -*-

import click

from ovhcli.cli import pass_ovh
from ovhcli.decorators import confirm_option, json_option
from ovhcli.modules.domain import domain
from ovhcli.modules.webhosting.utils import (display_services)


# Constants
CONFIG_CONTAINERS = ['jessie.i386', 'legacy', 'stable', 'testing']
CONFIG_ENGINES = ['php', 'phpcgi']
CONFIG_ENGINE_VERSIONS = ['5.4', '5.5', '5.6', '7.0']
CONFIG_ENVIRONMENTS = ['development', 'production']
CONFIG_FIREWALL = ['none', 'security']


@domain.command('list', short_help='List the services.')
@json_option()
@pass_ovh
def list(ovh):
    """List your Domain services."""
    services = ovh.domain.list()
    ovh.table(services, display_services)

