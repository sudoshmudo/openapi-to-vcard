import json
import os
import subprocess
import sys
from types import SimpleNamespace as Namespace

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI
import requests

load_dotenv()

ICON_SERVER = os.environ['ICON_SERVER']
      
app = FastAPI()

CARD = '''BEGIN:VCARD
VERSION:3.0
N:{}
TITLE:{}
PHOTO;ENCODING=b;TYPE=image/png:{}
END:VCARD'''

@app.get("/{host}")
async def get(host):
    response = requests.get('http://{}/openapi.json'.format(host)).text
    parsed = json.loads(response, object_hook=lambda d: Namespace(**d))
    
    cards = []
    images = {}

    for tag in parsed.tags:
        images[tag.name] = requests.get('{}/icons/{}'.format(ICON_SERVER, tag.name)).text[1:-1]

    paths = vars(parsed.paths)
    for path_key in paths:
        methods = vars(paths[path_key])
        for method_key in methods:
            cards.append(CARD.format(methods[method_key].summary, path_key, images[methods[method_key].tags[0]]))
    return ''.join(cards)
