# Installation guide

Whatever you do, run ``setup/refresh_cities.sh`` from the root if you want things to work. Then you will be able to run ``collect.py`` and ``serve.py``. You also have to add a ``keys.json`` file in the ``config/`` folder for the various APIs, the required keys and the links to get them are the following:

	{
		"google-directions": https://mapzen.com/projects/valhalla,
		"google-elevation": https://developers.google.com/maps/documentation/elevation/intro,
		"google-distance": https://www.mapbox.com/developers/api/distance/,
		"jcdecaux": https://developer.jcdecaux.com/#/opendata/vls?page=getstarted,
		"keolis": https://data.keolis-rennes.com/fr/accueil.html,
		"lacub": http://data.bordeaux-metropole.fr/apicub
	}

If your Google Developers account is properly setup you'll only require one API key for all Google API services.

Refer to the ``setup.sh`` script for installation procedures.

## Management

### Adding and removing cities

The ``add.py`` and ``remove.py`` scripts are command-line tools for adding and removing cities from the data collection process and the website visualization. The ``setup/refresh_cities.sh`` script adds all the cities possible. More details can be found [here](lib/providers/README.md).

- ``python3 manage.py add <provider> <city> <city_real_name> <country> <country_real_name> <predict>``
- ``python3 manage.py remove <provider> <city> <city_real_name> <country> <country_real_name> <predict>``

### GitHub management

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
sudo chown max -R .
```

### Task management

The task management is done with [Celery](http://www.celeryproject.org/). You can run the tasks with `celery -A tasks worker -B`. The tasks are defined in `tasks.py` and Celery is configured in `celery_config.py`.

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
