# distributor.api.tools
cli support toolset

~~~~shell
git clone https://github.com/dgordienko/distributor.api.tools.git
cd distributor.api.tools.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py --help
~~~~

You mast check .env file in appication folder, his view like this:

~~~shell
SYSTEM_CONTAINERS = ["rabbitmq", "mongo", "redis"]
APP_CONTAINERS = ["docorder.listener", "dockreturn.listener", "protocol.promo.listener", "protocol.doctax.listener","protocol.android.visit"]
~~~~

Sample

~~~shell
python dapi.py --help
Usage: dapi.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  docker-check    Check containers status
  docker-restart  Restart containers order
~~~