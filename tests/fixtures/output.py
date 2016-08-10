# -*- coding: utf-8 -*-

PLAIN_SIMPLE = {'name': 'john'}
PLAIN_NULL = {'foobar': None}
PLAIN_LIST = {'foobar': ['foo', 'bar']}
PLAIN_EMPTY_LIST = {'foobar': []}
PLAIN_DICT = {'foobar': {'foo': 'bar'}}
PLAIN_MULTIPLE = {'name': 'john', 'age': 45, 'city': 'Lille', 'country': 'FR'}

LIST_SIMPLE = [{'key1': 'foo1', 'key2': 'foo2'}, {'key1': 'bar1', 'key2': 'bar2'}]
LIST_TO_SORT = [{'key': 'a'}, {'key': 'c'}, {'key': 'd'}, {'key': 'b'}]
LIST_MISSING_FIELDS = [{'key1': 'foo1'}, {'key2': 'bar2'}]
LIST_NULL = [{'key': 'foo'}, {'key': None}]
LIST_EMPTY_LIST = [{'key': 'foo'}, {'key': []}]
LIST_NON_EMPTY_LIST = [{'key': 'foo'}, {'key': ['foo', 'bar']}]
LIST_DICT = [{'key': 'foo'}, {'key': {'foo': 'bar'}}]