# -*- coding: utf8 -*-

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'modules')
)

CONFIG_PATH = os.path.join(os.path.expanduser("~"), '.ovh.conf')
CONFIG_TEMPLATE = '''[default]
endpoint={ENDPOINT}

[{ENDPOINT}]
application_key={AK}
application_secret={AS}
consumer_key={CK}

[ovh-cli]
'''

CREATE_TOKEN_LINK = 'https://api.ovh.com/createToken/index.cgi?GET=/*&' \
                    'POST=/*&PUT=/*&DELETE=/*'
