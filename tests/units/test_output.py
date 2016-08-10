# -*- coding: utf-8 -*-

from ovhcli.output import Output

from ..base import CliTestCase
from ..fixtures import output


class OutputTest(CliTestCase):

    def test_plain_simple(self):
        out = Output(output.PLAIN_SIMPLE)
        self.assertEqual(out.convert(), """+----------+-------+
| Property | Value |
+----------+-------+
| name     | john  |
+----------+-------+""")

    def test_plain_with_null(self):
        out = Output(output.PLAIN_NULL)
        self.assertEqual(out.convert(), """+----------+-------+
| Property | Value |
+----------+-------+
| foobar   |       |
+----------+-------+""")

    def test_plain_with_list(self):
        out = Output(output.PLAIN_LIST)
        self.assertEqual(out.convert(), """+----------+----------------+
| Property | Value          |
+----------+----------------+
| foobar   | ['foo', 'bar'] |
+----------+----------------+""")

    def test_plain_with_empty_list(self):
        out = Output(output.PLAIN_EMPTY_LIST)
        self.assertEqual(out.convert(), """+----------+-------+
| Property | Value |
+----------+-------+
| foobar   |       |
+----------+-------+""")

    def test_plain_with_dict(self):
        out = Output(output.PLAIN_DICT)
        self.assertEqual(out.convert(), """+----------+----------------+
| Property | Value          |
+----------+----------------+
| foobar   | {"foo": "bar"} |
+----------+----------------+""")

    def test_plain_multiple(self):
        out = Output(output.PLAIN_MULTIPLE)
        self.assertEqual(out.convert(), """+----------+-------+
| Property | Value |
+----------+-------+
| age      | 45    |
| city     | Lille |
| country  | FR    |
| name     | john  |
+----------+-------+""")

    def test_plain_multiple_with_excludes(self):
        out = Output(output.PLAIN_MULTIPLE, exclude=['city', 'age'])
        self.assertEqual(out.convert(), """+----------+-------+
| Property | Value |
+----------+-------+
| country  | FR    |
| name     | john  |
+----------+-------+""")

    def test_list_simple(self):
        out = Output(output.LIST_SIMPLE)
        self.assertEqual(out.convert(), """+------+------+
| key1 | key2 |
+------+------+
| foo1 | foo2 |
| bar1 | bar2 |
+------+------+""")

    def test_list_multiple_with_excludes(self):
        out = Output(output.LIST_SIMPLE, exclude=['key2'])
        self.assertEqual(out.convert(), """+------+
| key1 |
+------+
| foo1 |
| bar1 |
+------+""")

    def test_list_sort(self):
        out = Output(output.LIST_TO_SORT, sort='key')
        self.assertEqual(out.convert(), """+-----+
| key |
+-----+
| a   |
| b   |
| c   |
| d   |
+-----+""")

    def test_list_reverse_sort(self):
        out = Output(output.LIST_TO_SORT, sort='-key')
        self.assertEqual(out.convert(), """+-----+
| key |
+-----+
| d   |
| c   |
| b   |
| a   |
+-----+""")

    def test_list_missing_keys(self):
        out = Output(output.LIST_MISSING_FIELDS)
        self.assertEqual(out.convert(), """+------+------+
| key1 | key2 |
+------+------+
| foo1 |      |
|      | bar2 |
+------+------+""")

    def test_list_with_null(self):
        out = Output(output.LIST_NULL)
        self.assertEqual(out.convert(), """+-----+
| key |
+-----+
| foo |
|     |
+-----+""")

    def test_list_with_empty_list(self):
        out = Output(output.LIST_EMPTY_LIST)
        self.assertEqual(out.convert(), """+-----+
| key |
+-----+
| foo |
|     |
+-----+""")

    def test_list_with_list(self):
        out = Output(output.LIST_NON_EMPTY_LIST)
        self.assertEqual(out.convert(), """+----------------+
| key            |
+----------------+
| foo            |
| ['foo', 'bar'] |
+----------------+""")

    def test_list_with_dict(self):
        out = Output(output.LIST_DICT)
        self.assertEqual(out.convert(), """+----------------+
| key            |
+----------------+
| foo            |
| {"foo": "bar"} |
+----------------+""")
