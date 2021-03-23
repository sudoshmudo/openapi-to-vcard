import json
import os
import subprocess
import sys
from types import SimpleNamespace as Namespace

from fastapi import APIRouter, FastAPI
import requests
      
app = FastAPI()

CARD = '''BEGIN:VCARD
VERSION:3.0
N:{}
TITLE:{}
END:VCARD'''

@app.get("/{host}")
async def get(host):
    response = requests.get('http://{}/openapi.json'.format(host)).text
    parsed = json.loads(response, object_hook=lambda d: Namespace(**d))
    
    cards = []
    
    paths = vars(parsed.paths)
    for path_key in paths:
    	methods = vars(paths[path_key])
    	for method_key in methods:
    	    cards.append(CARD.format(methods[method_key].summary, path_key))
    	    
    return ''.join(cards)
