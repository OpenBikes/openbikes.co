# Translations

- In the Python files wrap the generated text with ``gettext()``
- In the HTML files wrap the text with ``{{ _(<text>) }}``.
- ``pybabel extract -F translations/babel.cfg -o translations/messages.pot .``
- ``pybabel init -i translations/messages.pot -d translations -l <lang>``
- Then use [Poedit](http://poedit.net/) to translate the ``.po`` file
- ``pybabel compile -d translations``
