import json
import os

import docker
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def test_env():
    exception: Exception = None
    syscont = os.getenv('SYSTEM_CONTAINERS')
    appcont = os.getenv('APP_CONTAINERS')    
    syscont = json.loads(syscont)
    appcont = json.loads(appcont)
    client = docker.from_env()
    containers: list = client.containers.list()
    assert len(syscont) == 3
    try:
        # restart system containers
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, syscont))
            if(len(container) == 1):
                client.containers.get(contname).restart()
        # restart application containers       
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, appcont))
            if(len(container) == 1):
                client.containers.get(contname).restart()  
    except Exception as e:
        exception = e
    assert exception is None

