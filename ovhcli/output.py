# -*- coding: utf8 -*-

import json

from terminaltables import AsciiTable


class Output:
    """
    This module can be used to convert a simple JSON value in a pretty table
    representation.

    Two representations can be converted : a ``plain`` JSON or a ``list`` :

        >>> from ovhcli.output import Output
        >>> output = Output({'username': 'john', 'country': 'US'})
        >>> print(output.convert())
        +----------+-------+
        | Property | Value |
        +----------+-------+
        | country  | US    |
        | username | john  |
        +----------+-------+
        >>> output = Output([{'username': 'john', 'country': 'US'},
        ... {'username': 'nico', 'country': 'FR'}])
        >>> print(output.convert())
        +---------+----------+
        | country | username |
        +---------+----------+
        | US      | john     |
        | FR      | nico     |
        +---------+----------+
    """
    def __init__(self, data, exclude=[], sort=None):
        self._data = data
        self.exclude = exclude
        self.sort = sort
        self._json = None

    @property
    def json(self):
        if not self._json:
            self._json = self._data

        return self._json

    def iter_list(self, data):
        """Iterate over a list data."""

        def get_dict_value(l, key):
            try:
                value = l[key]
            except KeyError:
                return ''

            if not value and not isinstance(value, bool):
                return ''
            elif (isinstance(value, list)) and len(value) == 0:
                return ''
            elif isinstance(value, list):
                return value
            elif isinstance(value, dict):
                return json.dumps(value, sort_keys=True, ensure_ascii=False)

            return str(value)

        # Get all headers
        headers = sorted(
            list({k for d in data for k in d.keys() if k not in self.exclude})
        )

        # Sort the data
        if self.sort:
            reverse = False

            if self.sort.startswith('-'):
                reverse = True
                self.sort = self.sort[1:]

            data = sorted(data, key=lambda k: k[self.sort], reverse=reverse)

        # Convert the data in rows
        rows = [[get_dict_value(row, header) for header in headers]
                for row in data]

        rows.insert(0, headers)

        table = AsciiTable(rows)
        return table.table

    def iter_plain(self, data):
        """Iterate over a plain data."""

        def get_value(value):
            if not value and not isinstance(value, bool):
                return ''
            elif (isinstance(value, list)) and len(value) == 0:
                return ''
            elif isinstance(value, list):
                return value
            elif isinstance(value, dict):
                return json.dumps(value, sort_keys=True, ensure_ascii=False)

            return str(value)

        d = [[k, get_value(v)]
             for k, v in sorted(data.items())
             if k not in self.exclude]

        d.insert(0, ['Property', 'Value'])

        table = AsciiTable(d)

        return table.table

    def convert(self):
        """Dispatch the conversion if the JSON value is an instance of list
        or an instance of dict."""
        if isinstance(self.json, list):
            return self.iter_list(self.json)

        if isinstance(self.json, dict):
            return self.iter_plain(self.json)

        return self.json
