# -*- coding: utf8 -*-

import click

from ovhcli.cli import pass_ovh
from ovhcli.decorators import confirm_option, json_option
from ovhcli.modules.webhosting import webhosting
from ovhcli.modules.webhosting.utils import (display_services, display_quota,
                                             display_users, display_full_users,
                                             display_config)


# Constants
CONFIG_CONTAINERS = ['jessie.i386', 'legacy', 'stable', 'testing']
CONFIG_ENGINES = ['php', 'phpcgi']
CONFIG_ENGINE_VERSIONS = ['5.4', '5.5', '5.6', '7.0']
CONFIG_ENVIRONMENTS = ['development', 'production']
CONFIG_FIREWALL = ['none', 'security']


@webhosting.command('list', short_help='List the services.')
@json_option()
@pass_ovh
def list(ovh):
    """List your Web Hosting services."""
    services = ovh.webhosting.list()
    ovh.table(services, display_services)


@webhosting.command('info', short_help='Display information about a service.')
@click.argument('service')
@json_option()
@pass_ovh
def info(ovh, service):
    """Display information about a service."""
    service = ovh.webhosting.info(service)
    ovh.table(service, exclude=['countriesIp', 'phpVersions'])


@webhosting.command('info:quota', short_help='Display the service quota.')
@click.argument('service')
@json_option()
@pass_ovh
def quota(ovh, service):
    """Display the free and used quotas of a service."""
    quota = ovh.webhosting.quota(service)
    ovh.table(quota, display_quota)


@webhosting.command('info:countries',
                    short_help='Display the service countries.')
@click.argument('service')
@json_option()
@pass_ovh
def countries(ovh, service):
    """Display the countries of a service."""
    countries = ovh.webhosting.countries(service)
    ovh.table(countries, sort='country')


@webhosting.command('config', short_help='Display the .ovhconfig information.')
@click.argument('service')
@click.option('--historical', is_flag=True,
              help="Display the historical results.")
@click.option('--all', is_flag=True, help="Display all the results.")
@json_option()
@pass_ovh
def config(ovh, service, historical, all):
    """Display the .ovhconfig of a service."""
    configs = ovh.webhosting.config(
        service,
        historical,
        all
    )
    ovh.table(configs, display_config)


@webhosting.command('config:update',
                    short_help='Update the .ovhconfig information.')
@click.argument('service')
@click.option('--engine', type=click.Choice(CONFIG_ENGINES), default=None,
              help='Change the engine.')
@click.option('--engine-version', type=click.Choice(CONFIG_ENGINE_VERSIONS),
              default=None, help='Change the engine version.')
@click.option('--container', type=click.Choice(CONFIG_CONTAINERS),
              default=None, help='Change the container.')
@click.option('--environment', type=click.Choice(CONFIG_ENVIRONMENTS),
              default=None, help='Change the environment.')
@click.option('--firewall', type=click.Choice(CONFIG_FIREWALL),
              default=None, help='Change the http firewall.')
@confirm_option()
@pass_ovh
def update_config(ovh, service, container, engine, engine_version,
                  environment, firewall):
    """Update the .ovhconfig information."""
    task = ovh.webhosting.update_config(
        service=service,
        ovh_config=None,
        container=container,
        engine=engine,
        engine_version=engine_version,
        environment=environment,
        firewall=firewall
    )

    if task:
        ovh.success('The configuration will be updated in a few seconds.')

    return task


@webhosting.command('users', short_help='List the users of a service.')
@click.argument('service')
@click.option('--full', is_flag=True,
              help="Display all information about the users.")
@json_option()
@pass_ovh
def get_users(ovh, service, full):
    """Display the users of a service."""
    users = ovh.webhosting.get_users(service, full)
    output_func = display_full_users if full else display_users

    ovh.table(users, output_func)


@webhosting.command('users:show', short_help='Information about a user.')
@click.option('--login', '-l', help='Login of the user.', required=True)
@click.argument('service')
@json_option()
@pass_ovh
def get_user(ovh, service, login):
    """Display information about a user of a service."""
    user = ovh.webhosting.get_user(service, login)
    ovh.table(user)


@webhosting.command('users:create', short_help='Add a new user to a service.')
@click.argument('service')
@click.option('--login', '-l', help='Login for the new user.', required=True)
@click.option('--password', '-p', help='Password for the new user.',
              prompt=True, hide_input=True, confirmation_prompt=True)
@click.option('--home', '-h', help='Home directory.', default='.',
              show_default=True)
@click.option('--ssh', help='Enable the SSH.', is_flag=True)
@confirm_option()
@pass_ovh
def create_user(ovh, service, login, password, home, ssh):
    """Add a new user to a service."""
    task = ovh.webhosting.create_user(service, login, password, home, ssh)

    if task:
        ovh.success('User {} will be created in a few seconds.'.format(
            login
        ))


@webhosting.command('users:update', short_help='Update a user information.')
@click.argument('service')
@click.option('--login', '-l', help='Login of the user to update.',
              required=True)
@click.option('--home', '-h', help='Home directory.')
@click.option('--ssh', help='Enable the SSH.', is_flag=True)
@click.option('--enabled/--disabled', help='Enable or disable the user.')
@confirm_option()
@pass_ovh
def update_user(ovh, service, login, home, ssh, enabled):
    """Update a user information."""
    user = ovh.webhosting.update_user(ovh, service, login,
                                      home, ssh, enabled)

    if user:
        msg = 'Information about {} will be updated in a few seconds.'
        ovh.success(msg.format(login))


@webhosting.command('users:remove', short_help='Remove a user from a service.')
@click.argument('service')
@click.option('--login', '-l', help='Login of the user to remove.',
              required=True)
@confirm_option()
@pass_ovh
def remove_user(ovh, service, login):
    """Remove a user from a service."""
    task = ovh.webhosting.remove_user(ovh, service, login)

    if task:
        ovh.success('User {} will be removed in a few seconds.'.format(
            login
        ))
