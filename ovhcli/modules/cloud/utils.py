# -*- coding: utf8 -*-

from terminaltables import AsciiTable

from ovhcli.utils import humanize_size


def display_projects(projects):
    """Display the user's projects."""
    data = [['Projects']]

    for project in sorted(projects):
        data.append([project])

    table = AsciiTable(data)

    return table.table


def display_instances(instances):
    """Display the project's instances."""
    data = [['Instances']]

    for instance in sorted(instances):
        data.append([instance])

    table = AsciiTable(data)

    return table.table


def display_flavors(flavors):
    """Display project's available flavors."""
    data = [['Name', 'vCPU', 'RAM', 'Disk']]

    for flavor in flavors:
        data.append([
            flavor['name'],
            flavor['vcpus'],
            humanize_size(flavor['ram']),
            '{:d} G'.format(flavor['disk'])
        ])

    table = AsciiTable(data)

    return table.table


def display_regions(regions):
    """Display project's available regions."""
    data = [['Region name']]

    for region in regions:
        data.append([region])

    table = AsciiTable(data)

    return table.table
