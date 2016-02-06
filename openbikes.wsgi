import sys, os, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/OpenBikes')
os.chdir('/var/www/OpenBikes')
from app import app
application = app
