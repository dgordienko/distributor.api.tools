import json
import os

import docker
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def test_env():
    
    syscont = os.getenv('SYSTEM_CONTAINERS')
    appcont = os.getenv('APP_CONTAINERS')    
    syscont = json.loads(syscont)
    appcont = json.loads(appcont)
    client = docker.from_env()
    containers: list = client.containers.list()

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

    assert len(syscont) == 3

def test_docker():
    client = docker.from_env()
    containers: list = client.containers.list()
    for item in containers:
        contname = item.name
        if 'rabbitmq' in contname:
            client.containers.get(contname).restart()
        elif 'redis' in contname:
            client.containers.get(contname).restart()
        elif 'mongo' in contname:
            client.containers.get(contname).restart()

    assert len(containers) > 0
