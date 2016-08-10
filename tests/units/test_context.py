# -*- coding: utf-8 -*-

import click

from ovhcli.cli import pass_ovh

from ..base import CliTestCase
from ..base import patch


class ContextTest(CliTestCase):

    def test_simple_echo(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.echo('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, 'foobar\n')

    def test_echo_with_prefix(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.echo('foobar', prefix='PREFIX')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[PREFIX] foobar\n')

    def test_echo_with_json(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.json = True
            ovh.echo('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '')

    def test_debug_no_activated(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.debug('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '')

    def test_debug_activated(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.debug_mode = True
            ovh.debug('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[debug] foobar\n')

    def test_success(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.success('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[*] foobar\n')

    def test_info(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.info('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[-] foobar\n')

    def test_warning(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.warning('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[warning] foobar\n')

    def test_error(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.error('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[error] foobar\n')

    @patch('ovhcli.context.strftime')
    def test_time_echo(self, mock_time):
        mock_time.return_value = '12:34:56'

        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.time_echo('foobar')

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '[12:34:56] foobar\n')

    def test_table(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.table({'username': 'john'})

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, """+----------+-------+
| Property | Value |
+----------+-------+
| username | john  |
+----------+-------+
""")

    def test_table_with_json(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.json = True
            ovh.table({'username': 'john'})

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, '{"username": "john"}\n')

    def test_table_with_custom_function(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            def output(data):
                return 'Username --> {}'.format(data['username'])

            ovh.table({'username': 'john'}, output)

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, 'Username --> john\n')

    def test_display_task(self):
        @click.command()
        @pass_ovh
        def cli(ovh):
            ovh.display_task({'function': 'foo', 'status': 'init'})
            ovh.display_task({'function': 'foo', 'status': 'todo'})
            ovh.display_task({'function': 'foo', 'status': 'doing'})
            ovh.display_task({'function': 'foo', 'status': 'done'})
            ovh.display_task({'function': 'foo', 'status': 'cancelled'})
            ovh.display_task({'function': 'foo', 'status': 'bar'})

        result = self.runner.invoke(cli)
        self.assertEqual(result.output, """\
[*] The task foo has been launched.
[*] The task foo has been launched.
[*] The task foo has been launched.
[*] The task foo is done.
[warning] The task foo has been cancelled.
[error] The task foo fell in an error state.
""")
