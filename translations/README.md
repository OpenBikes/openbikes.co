# Translations

- In the Python files wrap the generated text with ``gettext()``
- In the HTML files wrap the text with ``{{ _(<text>) }}``. 
- ``pybabel extract -F config/babel.cfg -o config/messages.pot .``
- ``pybabel init -i config/messages.pot -d translations -l <lang>``
- Then use [Poedit](http://poedit.net/) to translate the ``.po`` file
- ``pybabel compile -d translations``