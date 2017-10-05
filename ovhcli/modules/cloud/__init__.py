# -*- coding: utf8 -*-

import click


@click.group(short_help="Manage your public cloud instances.")
def cloud():
    """Manage and configure your public cloud instances."""
