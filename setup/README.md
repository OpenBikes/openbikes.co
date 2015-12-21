# Installation guide

Whatever you do, run ``addcities.sh`` if you want things to work. Then you will be able to run ``collect.py`` and ``serve.py``. You also have to add a ``keys.json`` file in the ``config/`` folder for the various APIs, the required keys and the links to get them are the following:

	{
		"valhalla": https://mapzen.com/projects/valhalla,
		"google-elevation": https://developers.google.com/maps/documentation/elevation/intro,
		"mapbox-distance": https://www.mapbox.com/developers/api/distance/,
		"jcdecaux": https://developer.jcdecaux.com/#/opendata/vls?page=getstarted,
		"keolis": https://data.keolis-rennes.com/fr/accueil.html,
		"lacub": http://data.bordeaux-metropole.fr/apicub
	}

## Server

Refer to the ``setup.sh`` script.

## Linux

- [Install MongoDB](http://docs.mongodb.org/master/administration/install-on-linux/).
- Install Python3 if you do not have it. You can install the necessary libraries with the system's Python but this is never recommended. You have two more secure options:
	- With a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) which will create a folder containing a Python interpreter which you can "activate" to avoid using the system's Python interpreter:
		- ``pip3 install virtualenv``
		- ``virtualenv venv``
		- ``source venv/bin/activate``
	- With [Anaconda](https://store.continuum.io/cshop/anaconda/), which acts as a big virtual envirnoment containing everything. Once it is [installed](http://docs.continuum.io/anaconda/install) the Python commands such as ``pip` in the shell will be linked to Anaconda's Python interpreter
- ``pip install -r requirements.txt`` for installing the Python libraries. 
- ``./addcities.sh`` for adding the cities to the geographical database and generating necessary files for the website.

## Mac

- Installing MongoDB with Brew is recommended, however it's a bit complicated to figure out how to make it work properly:
	- ``brew update``
	- ``brew install mongodb``
	- ``sudo mkdir -p /data/db``
	- ``sudo chown <USERNAME> /data/db``
	- ``ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents``
	- ``launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist``
	- Just to make sure reboot your computer.
- Install Python3 if you do not have it. You can install the necessary libraries with the system's Python but this is never recommended. You have two more secure options:
	- With a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) which will create a folder containing a Python interpreter which you can "activate" to avoid using the system's Python interpreter:
		- ``pip3 install virtualenv``
		- ``virtualenv venv``
		- ``source venv/bin/activate``
	- With [Anaconda](https://store.continuum.io/cshop/anaconda/), which acts as a big virtual envirnoment containing everything. Once it is [installed](http://docs.continuum.io/anaconda/install) the Python commands such as ``pip` in the shell will be linked to Anaconda's Python interpreter
- ``pip install -r requirements.txt`` for installing the Python libraries. 
- ``./addcities.sh`` for adding the cities to the geographical database and generating necessary files for the website.

## Windows

To do.

## Management

## Adding and removing cities

The ``manage.py`` script is a command-line tool for adding and removing cities from the data collection process and the website vizualisation. The ``setup/addcities.sh`` script adds all the cities possible. More details can be found [here](lib/providers/README.md).

- ``python3 manage.py add <provider> <city> <city_real_name> <country> <country_real_name> <predict>``
- ``python3 manage.py remove <provider> <city> <city_real_name> <country> <country_real_name> <predict>``

### GitHub

``cd /var/www`` before anything.

- Fresh install with
```sh
sudo git clone https://github.com/OpenBikes/Website
sudo mv Website/ OpenBikes/
sudo chmod 777 -R OpenBikes/
touch OpenBikes/config/keys.json
```
- Update with
```sh
cd OpenBikes
git reset --hard
git pull origin master
cd ..
sudo chmod -R 777 OpenBikes/
```

### Data collection robot

- Start with ``sudo start ob-collect``
- Stop with ``sudo stop ob-collect``
- Restart with ``sudo restart ob-collect``

### Learning robot

- Start with ``sudo start ob-learn``
- Stop with ``sudo stop ob-learn``
- Restart with ``sudo restart ob-learn``

### Restart robot

- Start with ``sudo start ob-restart``
- Stop with ``sudo stop ob-restart``
- Restart with ``sudo restart ob-restart``

### Website

- Start with
```sh
sudo a2ensite OpenBikes
service apache2 reload
```
- Stop with
```sh
sudo a2dissite OpenBikes
service apache2 reload
```