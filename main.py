import json
import os

import docker
import typer
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
app = typer.Typer()


@app.command()
def docker_restart():
    syscont = os.getenv('SYSTEM_CONTAINERS')
    appcont = os.getenv('APP_CONTAINERS')
    syscont = json.loads(syscont)
    appcont = json.loads(appcont)
    client = docker.from_env()
    containers: list = client.containers.list()

    # restart system containers
    logger.info("Try to restart system containers")
    for item in containers:
        contname = item.name
        container = list(filter(lambda x: x in contname, syscont))
        if (len(container) == 1):
            client.containers.get(contname).restart()
            logger.info('Restart {}'.format(contname))
    # restart application containers
    logger.info("Try to restart Distributor.Api protocols containers")
    for item in containers:
        contname = item.name
        container = list(filter(lambda x: x in contname, appcont))
        if (len(container) == 1):
            client.containers.get(contname).restart()
            logger.info('Restart {}'.format(contname))


if __name__ == "__main__":
    app()
