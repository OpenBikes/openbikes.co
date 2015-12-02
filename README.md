# [OpenBikes Website](http://openbikes.co/)

[![License](https://poser.pugx.org/automattic/jetpack/license.svg)](http://www.gnu.org/licenses/gpl-2.0.html)

![Logo](static/img/OpenBikes.png)

OpenBikes is a project for visualizing bike stations in real time. It also includes a prediction system in order to propose safer trips to users. This repository includes everything relative to the database and the main website.

## How to naviguate through the repository

- For installing all the requirements, please refer to the [``setup/`` folder](setup/README.md).
- The [``lib/`` folder](lib/README.md) is where all the heavy lifting is done, we are trying to document it as well as possible.
- The ``collect.py`` script is meant to retrieve data from all the bike sharing APIs. Because the APIs are not similar, there is an individual script for each API in the [``lib/providers/`` folder](lib/providers/README.md).
- The ``learn.py`` script is used to update the predictors in ``predictors/`` folder. There is more information about this in the [``lib/learning/`` folder](lib/learning/README.md).
- The [``maintenance/`` folder](maintenance/README.md) contains tools to add/remove cities from the website and to update the metadata used throughout the project.
- The ``static/`` and ``templates/`` folders are where all the HTML, CSS, and JavaScript are contained.
- The instructions to add another language to the website are in the [``translations/`` folder](translations/README.md).