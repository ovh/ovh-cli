# -*- coding: utf8 -*-

import importlib
import os

from click import CommandCollection
from ovh.exceptions import APIError

from ovhcli.settings import MODULES_FOLDER


def is_module(module):
    """Check if a given string is an existing module contained in the
    ``MODULES_FOLDER`` constant."""
    if (os.path.isdir(os.path.join(MODULES_FOLDER, module)) and
            not module.startswith('_')):
            return True

    return False


class ModuleCollection(CommandCollection):
    """A module collection is a command collection that fetch the commands
    specified in a module folder.

    A module folder has the following structure :

        modules/
        ├── foo/
        │   ├── __init__.py
        │   ├── commands.py
        │   ├── controllers.py
        │   └── utils.py
        ├── ...

    The main command is defined in ``modules/foo/__init__.py``. Its subcommands
    are defined in ``modules/foo/commands.py``.
    """

    def __init__(self, name=None, module_folder=None, **attrs):
        CommandCollection.__init__(self, name, **attrs)
        self.module_folder = module_folder

    def list_commands(self, ctx):
        """List the modules contained in the ``MODULES_FOLDER`` constant."""
        commands = [
            module for module
            in sorted(os.listdir(self.module_folder))
            if is_module(module)
        ]

        return commands

    def get_command(self, ctx, name):
        """List the commands for a specific module."""
        try:
            # Import the module
            mod = importlib.import_module('ovhcli.modules.{}'.format(name))

            # Import the commands
            importlib.import_module('ovhcli.modules.{}.commands'.format(name))

            return getattr(mod, name)

        except ImportError:
            pass

    def invoke(self, ctx):
        """Call the command. If an error in the OVH API is raised, display a
        message with the corresponding error."""
        try:
            super(ModuleCollection, self).invoke(ctx)
        except APIError as e:

            # Debug mode
            if ctx.obj.debug_mode:
                raise

            ctx.obj.error(e)
