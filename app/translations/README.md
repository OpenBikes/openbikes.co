# Translations

- In the Python files wrap the generated text with `gettext()`.
- In the HTML files wrap the text with `{{ _(<text>) }}`.
- `pybabel extract -F app/translations/babel.cfg -o app/translations/messages.pot .`
- `pybabel init -i app/translations/messages.pot -d app/translations -l <lang>`
- Then use [Poedit](http://poedit.net/) to translate and compile the ``.po`` file.
- Update with `pybabel extract -F app/translations/babel.cfg -o app/translations/messages.pot .` for creating a new `.pot` file and then `pybabel update -i app/translations/messages.pot -d app/translations` to update each language's `.po` file.
