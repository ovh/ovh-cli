# -*- coding: utf8 -*-

import click

from ovhcli.command import ModuleCollection
from ovhcli.context import OvhContext
from ovhcli.settings import MODULES_FOLDER


context = OvhContext
pass_ovh = click.make_pass_decorator(context, ensure=True)


@click.command(cls=ModuleCollection, module_folder=MODULES_FOLDER)
@click.version_option(prog_name='OVH Cli')
@click.option('-d', '--debug', is_flag=True, help='Enable the debug mode.')
@pass_ovh
def cli(ovh, debug):
    """OVH Command Line Interface"""
    ovh.debug_mode = debug
