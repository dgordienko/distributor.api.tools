# distributor.api.tools
cli support toolset

~~~~shell
git clone https://github.com/dgordienko/distributor.api.tools.git
cd distributor.api.tools.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
~~~~

You mast check .env file in appication folder, his view like this:

~~~shell
SYSTEM_CONTAINERS = ["rabbitmq", "mongo", "redis"]
APP_CONTAINERS = ["docorder.listener", "dockreturn.listener", "protocol.promo.listener", "protocol.doctax.listener","protocol.android.visit"]
~~~~