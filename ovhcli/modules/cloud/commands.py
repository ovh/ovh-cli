# -*- coding: utf8 -*-

import click

from ovhcli.cli import pass_ovh
from ovhcli.decorators import json_option
from ovhcli.modules.cloud import cloud
from ovhcli.modules.cloud.utils import (display_instances, display_projects, display_flavors,
                                        display_regions)


@cloud.command('projects', short_help='List the projects.')
@json_option()
@pass_ovh
def projects(ovh):
    """List your Public Cloud projects."""
    projects = ovh.cloud.projects()
    ovh.table(projects, display_projects)


@cloud.command('instances', short_help='List project\'s instances.')
@click.option('--project', help='Project identifier.', required=True)
@json_option()
@pass_ovh
def instances(ovh, project):
    """List your Public Cloud instances."""
    instances = ovh.cloud.instances(project)
    ovh.table(instances, display_instances)


@cloud.command('flavors', short_help='Show flavors')
@click.option('--project', help='Project identifier.', required=True)
@click.option('--region', help='Filter results by region.')
@json_option()
@pass_ovh
def flavors(ovh, project, region):
    """List available Public Cloud flavors."""
    flavors = ovh.cloud.flavors(project, region)
    ovh.table(flavors, display_flavors)


@cloud.command('regions', short_help='Show regions')
@click.option('--project', help='Project identifier.', required=True)
@json_option()
@pass_ovh
def regions(ovh, project):
    """List available Public Cloud regions."""
    regions = ovh.cloud.regions(project)
    ovh.table(regions, display_regions)
