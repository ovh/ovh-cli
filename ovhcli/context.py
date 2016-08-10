# -*- coding: utf8 -*-

import importlib
import json as _json
import os
from time import strftime

import click
import ovh
from ovh.exceptions import APIError, InvalidRegion

from ovhcli.command import is_module
from ovhcli.output import Output
from ovhcli.settings import MODULES_FOLDER


class OvhContext(click.Context):
    def __init__(self):
        self.debug_mode = False
        self.commit = False
        self._json = False
        self._controllers = {}

        if not self._controllers:
            self.load_controllers()

    def __getattribute__(self, item):
        """Used to dynamically call the method of a controller in a command
        function. If the specified controller does not exist, just return
        the class attribute.

        For example, the line ``ovh.foo.bar()`` in the following command
        calls the ``modules.foo.controllers.Foo.bar`` method :

            @foo.command('bar')
            @pass_ovh
            def bar(ovh):
                data = ovh.foo.bar()
        """
        if item in object.__getattribute__(self, '_controllers'):
            cls = object.__getattribute__(self, '_controllers')[item]

            # The setup module does not require a client instance
            if item != 'setup':
                client = self.get_ovh_client()
                cls.client = client

            return cls

        return object.__getattribute__(self, item)

    def get_ovh_client(self):
        """Get the OVH client."""
        try:
            client = ovh.Client()
        except InvalidRegion:
            self.error('The configuration was not found.')
            self.error('Please use `ovh setup init` to create it.')
            self.exit()

        return client

    def load_controllers(self):
        """Load the controllers for each module specified in the
        ``MODULE_FOLDER`` constant.

        If a module can't be imported for any reason, we do not display it."""
        modules = [
            module for module
            in sorted(os.listdir(MODULES_FOLDER))
            if is_module(module)
        ]

        for module in modules:
            try:
                controller = importlib.import_module(
                    'ovhcli.modules.{}.controllers'.format(module)
                )

                self._controllers[module] = getattr(
                    controller,
                    module.capitalize()
                )
            except ImportError:
                # Do not raise error if the controller is not provided
                # Some modules does not require one
                pass

    def echo(self, message, prefix='', color='white'):
        """Print a message with a colored prefix unless the ``--json``
        parameter is specified."""
        try:
            json = self.json
        except AttributeError:
            json = False

        if not json:
            if prefix:
                prefix = '[{}] '.format(click.style(prefix, fg=color))
            click.echo(u"{}{}".format(prefix, message))

    def debug(self, message):
        """Print a debug message if the debug mode is enabled."""
        if self.debug_mode:
            self.echo(message, 'debug', 'blue')

    def info(self, message):
        """Print an information message."""
        self.echo(message, '-', 'cyan')

    def time_echo(self, message):
        """Print an information message with a formatted date."""
        self.echo(message, strftime('%H:%M:%S'), 'cyan')

    def success(self, message):
        """Print a success message."""
        self.echo(message, '*', 'green')

    def warning(self, message):
        """Print a warning message."""
        self.echo(message, 'warning', 'yellow')

    def error(self, message):
        """Print an error message."""
        self.echo(message, 'error', 'red')

    def table(self, data, custom_func=None, exclude=[], sort=None):
        """
        Print a pretty table unless the ``--json`` parameter is specified.

        If no custom function is given, use the ``Output`` class to generate
        the table."""
        try:
            json = self.json
        except AttributeError:
            json = False

        # Print the result as json
        if json:
            click.echo(_json.dumps(data))
            return

        # Use the custom function if provided
        if custom_func:
            self.echo(custom_func(data))
            return

        # Otherwise, print the table with Output class
        table = Output(data, exclude=exclude, sort=sort)
        self.echo(table.convert())

    def display_task(self, task):
        """Print a task status."""
        name = task['function']

        if task['status'] in ['init', 'todo', 'doing']:
            self.success(
                'The task {} has been launched.'.format(name)
            )
        elif task['status'] == 'done':
            self.success(
                'The task {} is done.'.format(name)
            )
        elif task['status'] == 'cancelled':
            self.warning(
                'The task {} has been cancelled.'.format(name)
            )
        else:
            self.error(
                'The task {} fell in an error state.'.format(name)
            )
