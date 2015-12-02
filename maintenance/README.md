# Maintenance

## Adding and removing cities

The ``manage.py`` script is a command-line tool for adding and removing cities from the data collection process and the website vizualisation. The ``setup/addcities.sh`` script adds all the cities possible. More details can be found [here](lib/providers/README.md).

- ``python3 manage.py add <provider> <city> <city_real_name> <country> <country_real_name> <predict>``
- ``python3 manage.py remove <provider> <city> <city_real_name> <country> <country_real_name> <predict>``

## GitHub

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

## Data collection robot

- Start with ``sudo start ob-collect``
- Stop with ``sudo stop ob-collect``
- Restart with ``sudo restart ob-collect``

## Learning robot

- Start with ``sudo start ob-learn``
- Stop with ``sudo stop ob-learn``
- Restart with ``sudo restart ob-learn``

## Website

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