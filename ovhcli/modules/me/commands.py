# -*- coding: utf8 -*-

import click

from ovhcli.cli import pass_ovh
from ovhcli.decorators import json_option
from ovhcli.modules.me import me


@me.command('info', short_help='Display your personal information.')
@json_option()
@pass_ovh
def info(ovh):
    """Get your personal information."""
    me = ovh.me.info()
    ovh.success('Welcome here %s' % me['firstname'])
    ovh.table(me, exclude=['companyNationalIdentificationNumber',
                           'nationalIdentificationNumber'])


@me.command('apps', short_help='List the applications.')
@json_option()
@pass_ovh
def applications(ovh):
    """List the applications."""
    applications = ovh.me.get_applications()
    ovh.table(applications, sort='-applicationId')


@me.command('apps:show',
            short_help='Display information about an application.')
@click.argument('applicationId')
@json_option()
@pass_ovh
def application(ovh, applicationid):
    """Display information about an application."""
    app = ovh.me.get_application(applicationid)
    ovh.table(app)


@me.command('apps:credentials',
            short_help='Get the credentials of an application.')
@click.argument('application_id')
@json_option()
@pass_ovh
def credentials(ovh, application_id):
    """Get the credentials of an application."""
    creds = ovh.me.get_credentials(application_id)
    ovh.table(creds, exclude=['applicationId', 'ovhSupport', 'rules'])


@me.command('apps:rules', short_help='Get the rules of a credential.')
@click.argument('credential_id')
@json_option()
@pass_ovh
def rules(ovh, credential_id):
    """Get the rules of a credential."""
    rules = ovh.me.get_rules(credential_id)
    ovh.table(rules)
