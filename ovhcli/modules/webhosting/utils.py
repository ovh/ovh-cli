# -*- coding: utf8 -*-

from terminaltables import AsciiTable


def display_services(services):
    """Display the user services."""
    data = [['Services']]

    for service in sorted(services):
        data.append([service])

    table = AsciiTable(data)

    return table.table


def display_quota(quota):
    """Display the quota for a service."""
    used = '{} {}'.format(
        "%.2f" % quota['used']['value'],
        quota['used']['unit']
    )
    size = '{} {}'.format(
        "%.2f" % quota['size']['value'],
        quota['size']['unit']
    )

    table = AsciiTable([["Used", used], ["Size", size]])

    return table.table


def display_users(users):
    """Display the list of users by their username."""
    data = [['Users']]

    for user in sorted(users):
        data.append([user])

    table = AsciiTable(data)

    return table.table


def display_full_users(users):
    """Display the list of users with all information."""
    data = [['Login', 'Home', 'State', 'Ssh', 'Primary account']]

    # Sort the list of users by login
    users = sorted(users, key=lambda k: k['login'])

    for user in users:
        data.append([
            user['login'],
            user['home'],
            user['state'],
            user['sshState'],
            user['isPrimaryAccount']
        ])

    table = AsciiTable(data)

    return table.table


def display_config(configs):
    """Display the .ovhconfig file information."""
    data = [['#ID', 'Environment', 'Engine version', 'Container', 'Path',
             'Engine', 'Firewall']]

    for config in configs:
        data.append([
            config['id'],
            config['environment'],
            config['engineVersion'],
            config['container'],
            config['path'],
            config['engineName'],
            config['httpFirewall']
        ])

    table = AsciiTable(data)

    return table.table
