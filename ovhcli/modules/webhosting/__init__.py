# -*- coding: utf8 -*-

import click


@click.group(short_help="Manage your WebHosting services.")
def webhosting():
    """Manage and configure your WebHosting products."""
