import json
import os

import docker
from dotenv import load_dotenv
from loguru import logger

load_dotenv()  # take environment variables from .env.


def test_workflow_full():
    """
    Test and debug workflow
    """
    exception: Exception = None
    syscont = os.getenv('SYSTEM_CONTAINERS')
    appcont = os.getenv('APP_CONTAINERS')
    syscont = json.loads(syscont)
    appcont = json.loads(appcont)
    client = docker.from_env()
    containers: list = client.containers.list()
    try:
        # restart system containers
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, syscont))
            if (len(container) == 1):
                client.containers.get(contname).restart()
        # restart application containers
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, appcont))
            if (len(container) == 1):
                client.containers.get(contname).restart()
    except Exception as e:
        exception = e
    assert exception is None


def test_workflow_check():
    exception: Exception = None
    try:
        syscont = os.getenv('SYSTEM_CONTAINERS')
        appcont = os.getenv('APP_CONTAINERS')
        syscont = json.loads(syscont)
        appcont = json.loads(appcont)
        client = docker.from_env()
        containers: list = client.containers.list()
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, syscont))
            if (len(container) == 1):
                cont = client.containers.get(contname)
                _status = cont.status
                _name = cont.name
                _id = cont.short_id
                logger.info('{} {} {}'.format(_id, _name, _status))
        # restart application containers
        for item in containers:
            contname = item.name
            container = list(filter(lambda x: x in contname, appcont))
            if (len(container) == 1):
                cont = client.containers.get(contname)
                _status = cont.status
                _name = cont.name
                _id = cont.short_id
                logger.info('{} {} {}'.format(_id, _name, _status))            
    except Exception as e:
        exception: Exception = e
    assert exception == None
