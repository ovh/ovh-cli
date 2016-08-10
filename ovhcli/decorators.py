# -*- coding: utf8 -*-

from click.decorators import option


def confirm_option(*params_decls, **attrs):
    """This decorator adds a confirmation message for critical actions : it can
    be bypassed with a ``--confirm`` parameter or answering ``yes`` to the
    prompted message.

    All parameters are optionals.

    Example usage::

        @module.command('users:remove')
        @click.argument('username')
        @confirm_option(help='Do you really want to remove this user ?')
        @pass_ovh
        def remove_user(ovh, username):
            pass
    """
    def decorator(f):
        def callback(ctx, param, value):
            if not value:
                ctx.abort()

        attrs.setdefault('is_flag', True)
        attrs.setdefault('callback', callback)
        attrs.setdefault('expose_value', False)
        attrs.setdefault('prompt', 'Confirm this action ?')
        attrs.setdefault('help', 'Confirm the action')

        return option(*(params_decls or ('--confirm',)), **attrs)(f)

    return decorator


def json_option(*params_decls, **attrs):
    """This decorator adds a ``--json`` parameter which can be used to display
    the controller results in JSON format.

    It should be used with a function supporting it, for example the
    ``ovhcli.context.OvhContext.table`` function.

    Example usage::

        @module.command('users:list')
        @json_option()
        @pass_ovh
        def list_users(ovh):
            data = [{'username': 'john'}, {'username': 'bob'}]
            ovh.table(data)
    """
    def decorator(f):
        def callback(ctx, param, value):
            try:
                ctx.obj.json = value
            except AttributeError:
                pass

        attrs.setdefault('is_flag', True)
        attrs.setdefault('callback', callback)
        attrs.setdefault('expose_value', False)
        attrs.setdefault('help', 'Return the JSON value.')

        return option(*(params_decls or ('--json',)), **attrs)(f)

    return decorator
