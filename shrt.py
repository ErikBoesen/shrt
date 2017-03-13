#!/usr/bin/env python3

import os
import requests
import argparse
import json
import re
import pyperclip
from termcolor import colored

parser = argparse.ArgumentParser(description='Create shortlinks with shirt.')
parser.add_argument('url', type=str, help='The URL you want to shorten.')
parser.add_argument('--key', dest='key', default=None, help='Custom key to use.')
parser.add_argument('--host', dest='host', default=os.environ['SHIRT_HOST'], help='A custom host to upload links to, if necessary. Defaults to $SHIRT_HOST.')

args = parser.parse_args()

data = {'url': args.url}

if args.key is not None:
    data['key'] = args.key

r = requests.post('%s/new' % args.host, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

resp = r.json()

if resp.get('error') is not None:
    print('The key %s is already taken.' % args.key)
else:
    url = '%s/%s' % (args.host, resp['key'])
    print('\n    ' + colored('✓', 'green') + ' Shortlink accessible at %s (copied.)\n' % colored(re.sub(r'^https?://(www\.)?', '', url), 'cyan'))
    pyperclip.copy(url)
