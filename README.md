# [OpenBikes Website](http://openbikes.co/)

For working on the project with a local computer, refer to [the installation guide](setup/README.md).

The ``lib`` folder is where all the heavy lifting is done, there are individual ``README.md`` files for each module.

## Add and remove cities

The ``manage.py`` script is a command-line tool for adding and removing cities from the data collection process and the website vizualisation. The ``addcities.sh`` script adds all the cities possible. More details can be found [here](lib/providers/README.md).

- ``python3 manage.py add <provider> <city> <city_real_name> <country> <country_real_name>``
- ``python3 manage.py remove <provider> <city> <city_real_name> <country> <country_real_name>``

## Maintenance

For some modifications you might have to reboot the server with ``sudo shutdown -r now``. Sometimes it can solve a lot of ununderstable problems.

### GitHub

``cd /var/www`` before anything.

- Fresh install with
```sh
sudo git clone https://github.com/MaxHalford/OpenBikes-Website
sudo mv OpenBikes-Website/ OpenBikes
sudo chmod 777 -R OpenBikes/
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

## Languages

- In the Python files wrap the generated text with ``gettext()``
- In the HTML files wrap the text with ``{{ _(<text>) }}``. 
- ``pybabel extract -F config/babel.cfg -o config/messages.pot .``
- ``pybabel init -i config/messages.pot -d translations -l <lang>``
- Then use [Poedit](http://poedit.net/) to translate the ``.po`` file
- ``pybabel compile -d translations``


## Style

### Colors

- Green: ``#66e066``
- Sky blue: ``#66b2ff``
- Cadet blue: ``#576a7f``
- Dark blue: ``#384452``

### Images

All bike images were found here : [WikiMedia](https://commons.wikimedia.org/wiki/Bicycle#/)