#!/usr/bin/env python3

import os
import requests
import argparse
import json
import re
import pyperclip
from sys import exit
from termcolor import colored

config_path = os.path.expanduser('~') + '/.shrt_config'
try:
    config = json.loads(open(config_path, 'r').read())
except FileNotFoundError:
    config = {
        'host': ''
    }

parser = argparse.ArgumentParser(description='Create shortlinks with shirt.')
parser.add_argument('url', type=str, help='The URL you want to shorten.')
parser.add_argument('--key', dest='key', default=None, help='Custom shirtlink key to use.')
parser.add_argument('--host', dest='host', default=config['host'], help='A custom host to upload links to, if necessary. Defaults to the address specified with shrt --set-host.')
parser.add_argument('--set-host', dest='set_host', default=False, action='store_true', help='Use to set the default shirt host.')

args = parser.parse_args()

if args.set_host:
    config['host'] = args.url
else: # Make a new link.
    data = {'url': args.url}

    if args.key is not None:
        data['key'] = args.key

    r = requests.post('%s/new' % args.host, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

    resp = r.json()

    if resp.get('error') is not None:
        print('The key %s is already taken.' % args.key)
    else:
        url = '%s/%s' % (args.host, resp['key'])
        print('\n    ' + colored('✓', 'green') + ' Link accessible at %s (copied.)\n' % colored(re.sub(r'^https?://(www\.)?', '', url), 'cyan'))
        pyperclip.copy(url)

open(config_path, 'w+').write(json.dumps(config))
