# -*- coding: utf8 -*-

import os

import click
import ovh
from click.exceptions import UsageError
from ovh.client import ENDPOINTS

from ovhcli.settings import CONFIG_PATH, CONFIG_TEMPLATE, CREATE_TOKEN_LINK


def check_choice(value):
    """Check if the given choice is in the allowed range."""
    if value not in ['1', '2', '3']:
        raise UsageError('Choice must be 1, 2 or 3')

    return int(value)


def check_endpoint(value):
    """Check if the given endpoint is in the allowed ones."""
    endpoints = ENDPOINTS.keys()

    if value not in endpoints:
        raise UsageError('This endpoint does not exist ({})'.format(
            ', '.join(sorted(endpoints))
        ))

    return value


def config_file_exists():
    """Check if the configuration file already exists."""
    return os.path.isfile(CONFIG_PATH)


def create_config_file(endpoint, application_key,
                       application_secret, consumer_key):
    """
    Create the configuration file.
    :param endpoint:
    :param application_key:
    :param application_secret:
    :param consumer_key:
    :return:
    """
    template = CONFIG_TEMPLATE.replace('{ENDPOINT}', endpoint)
    template = template.replace('{AK}', application_key)
    template = template.replace('{AS}', application_secret)
    template = template.replace('{CK}', consumer_key)

    with open(CONFIG_PATH, 'w') as f:
        f.write(template)

    return True


def get_ck_validation(endpoint, application_key, application_secret):
    """Return a validation request with full access to the API."""
    client = ovh.Client(endpoint=endpoint, application_key=application_key,
                        application_secret=application_secret)
    ck = client.new_consumer_key_request()
    ck.add_recursive_rules(ovh.API_READ_WRITE, '/')
    validation = ck.request()

    return validation


def launch_setup_1(ctx):
    """Choice 1 : user already has the 3 tokens (AK, AS and CK)."""
    endpoint = click.prompt('Endpoint', default='ovh-eu',
                            value_proc=check_endpoint)
    application_key = click.prompt('Application key')
    application_secret = click.prompt('Application secret')
    consumer_key = click.prompt('Consumer key')

    create_config_file(endpoint, application_key,
                       application_secret, consumer_key)

    ctx.success('Configuration file created.')


def launch_setup_2(ctx):
    """Choice 1 : user has the AK and AS tokens. We generate for him a link to
    validate the CK token."""
    endpoint = click.prompt('Endpoint', default='ovh-eu',
                            value_proc=check_endpoint)
    application_key = click.prompt('Application key')
    application_secret = click.prompt('Application secret')

    ctx.echo('')
    validation = get_ck_validation(endpoint, application_key,
                                   application_secret)
    ctx.info("Please visit the following link to authenticate you and "
             "validate the token :")
    ctx.info(validation['validationUrl'])
    click.pause()

    create_config_file(endpoint, application_key,
                       application_secret, validation['consumerKey'])

    ctx.success('Configuration file created.')


def launch_setup_3(ctx):
    """Choice 3 : the user does not have key, we provide him a link to
    generate it."""
    ctx.info("Please visit the following link to authenticate you and "
             "obtain your keys (AK, AS and CK) :")
    ctx.info(CREATE_TOKEN_LINK)
    click.pause()
    ctx.echo('')

    launch_setup_1(ctx)


def launch_setup_by_choice(ctx, choice):
    """Call the good setup process."""
    choices = {
        1: launch_setup_1,
        2: launch_setup_2,
        3: launch_setup_3
    }

    # Launch the good process
    try:
        choices[choice](ctx)
    except KeyError:
        ctx.error('Invalid choice')
