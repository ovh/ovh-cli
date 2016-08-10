OVH Cli
=======

OVH Command Line Interface.

.. code::

    $ ovh webhosting config mydomain.fr
    +---------+-------------+----------------+---------------+------+--------+----------+
    | #ID     | Environment | Engine version | Container     | Path | Engine | Firewall |
    +---------+-------------+----------------+---------------+------+--------+----------+
    | 1994114 | production  | 5.6            | stable        |      | php    | security |
    +---------+-------------+----------------+---------------+------+--------+----------+

    $ ovh webhosting config:update mydomain.fr --engine-version=7.0
    [*] The configuration will be updated in a few seconds.

    $ ovh webhosting config mydomain.fr
    +---------+-------------+----------------+---------------+------+--------+----------+
    | #ID     | Environment | Engine version | Container     | Path | Engine | Firewall |
    +---------+-------------+----------------+---------------+------+--------+----------+
    | 2023413 | production  | 7.0            | stable        |      | php    | security |
    +---------+-------------+----------------+---------------+------+--------+----------+

Installation
============

The OVH Cli works with Python 2.7+ and Python 3.3+.

The easiest way to get the latest stable release is to grab it from `pypi
<https://pypi.python.org/pypi/ovh-cli>`_ using ``pip``.

.. code:: bash

    pip install ovh-cli

Alternatively, you may get latest development version directly from Git.

.. code:: bash

    pip install -e git+https://github.com/ovh/ovh-cli.git#egg=ovh-cli

Getting started
===============

The Cli uses the public OVH API to manage the user products. A ``setup`` command
is provided to help you creating the required tokens :

.. code::

    $ ovh setup init
    Welcome to the OVH Cli.

    This tool uses the public OVH API to manage your products. In order to
    work, 3 tokens that you must generate are required :

    - the application key (AK)
    - the application secret (AS)
    - the consumer key (CK)

    What's your context :

        1) You already have the keys (AK, AS and CK)
        2) You just have AK and AS, the CK must be generated
        3) You have no keys

    Your choice [1]: 3

    [-] Please visit the following link to authenticate you and obtain your keys (AK, AS and CK) :
    [-] https://api.ovh.com/createToken/index.cgi?GET=/*&POST=/*&PUT=/*&DELETE=/*
    Press any key to continue ...

    Endpoint [ovh-eu]: ovh-eu
    Application key: <application key>
    Application secret: <application secret>
    Consumer key: <consumer key>
    [*] Configuration file created.

Commands help
=============

Each command and subcommand provides a ``--help`` parameter :

.. code::

    $ ovh webhosting --help
    Usage: ovh webhosting [OPTIONS] COMMAND [ARGS]...

      Manage and configure your WebHosting products.

    Options:
      --help  Show this message and exit.

    Commands:
      config          Display the ovhConfig information.
      config:update   Update the ovhConfig information.
      info            Display information about a service.
      info:countries  Display the service countries.
      info:quota      Display the service quota.
      list            List the services.
      users           List the users of a service.
      users:create    Add a new user to a service.
      users:remove    Remove a user from a service.
      users:show      Information about a user.
      users:update    Update an existing user.

JSON output
===========

By default, the OVH Cli displays the output in a pretty table representation. When it's possible, a ``--json`` parameter is provided to return the content as pure JSON :

.. code::

    $ ovh webhosting users mydomain.fr --full
    +-------------+------+-------+--------+-----------------+
    | Login       | Home | State | Ssh    | Primary account |
    +-------------+------+-------+--------+-----------------+
    | johndoe     | .    | rw    | active | True            |
    | johndoe-foo | foo  | rw    | none   | False           |
    +-------------+------+-------+--------+-----------------+

    $ ovh webhosting users mydomain.fr --full --json
    [{"iisRemoteRights": null, "sshState": "none", "webDavRights": null, "login": "johndoe-foo", "isPrimaryAccount": false, "state": "rw", "home": "foo"}, {"iisRemoteRights": null, "sshState": "active", "webDavRights": null, "login": "johndoe", "isPrimaryAccount": true, "state": "rw", "home": "."}]

Contributing
============

See `CONTRIBUTING.rst <https://github.com/ovh/ovh-cli/blob/master/CONTRIBUTING.rst>`_ for contribution guidelines.

License
=======

3-Clause BSD