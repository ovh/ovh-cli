# -*- coding: utf8 -*-

import click

from ovhcli.cli import pass_ovh
from ovhcli.modules.setup import setup
from ovhcli.modules.setup.utils import (check_choice, check_endpoint,
                                        config_file_exists, create_config_file,
                                        launch_setup_by_choice)


WELCOME_MESSAGE = '''Welcome to the OVH Cli.

This tool uses the public OVH API to manage your products. In order to
work, 3 tokens that you must generate are required :

- the application key (AK)
- the application secret (AS)
- the consumer key (CK)

What's your context :

    1) You already have the keys (AK, AS and CK)
    2) You just have AK and AS, the CK must be generated
    3) You have no keys
'''


@setup.command('init', short_help='Generate the configuration file.')
@click.option('--force', is_flag=True, help="Erase the existing file.")
@pass_ovh
def init(ovh, force):
    """Generate the configuration file."""
    if config_file_exists():
        if not force:
            ovh.error('A configuration file already exists '
                      '(use --force to erase it).')
            ovh.exit()
        else:
            ovh.warning('The configuration file will be erased.\n')

    # Display the welcome message
    ovh.echo(WELCOME_MESSAGE)

    # According to the choice, we launch the good def
    choice = click.prompt('Your choice', default=1, value_proc=check_choice)
    ovh.echo('')

    launch_setup_by_choice(ovh, choice)
