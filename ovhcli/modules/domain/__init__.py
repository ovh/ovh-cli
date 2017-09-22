# -*- coding: utf8 -*-

import click


@click.group(short_help="Manage your Domain services.")
def domain():
    """Manage and configure your Domain products."""
