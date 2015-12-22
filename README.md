# [OpenBikes Website](http://openbikes.co/)

[![License](https://poser.pugx.org/automattic/jetpack/license.svg)](http://www.gnu.org/licenses/gpl-2.0.html)

![Logo](app/static/img/OpenBikes.png)

OpenBikes is a project for visualizing bike stations in real time. It also includes a prediction system in order to propose faultless trips to users. This repository includes everything relative to the database and the website.

## Structure

The application is designed with the microservices architecture in mind. As such, it is divided into mutually exclusive components that interact through a common folder and a database. For installing all the requirements, refer to the [``setup/`` folder](setup/README.md). The instructions for adding other languages to the website can be found in the [``translations/`` folder](translations/README.md).

### [collecting](collecting/README.md)

Contains the scripts for grabbing the data from the providers who put to disposition an API.

### [learning](learning/README.md)

Contains the statistical algorithms for predicting the number of bikes/stands.

### [mongo](mongo/README.md)

Contains the code for managing the two databases:

- A timeseries database which stores every update for every single bike station.
- A geographical database for performing spatial queries.

### [routing](routing/README.md)

Contains the logic for choosing optimal paths.

### [app](app/README.md)

Contains the templates and the static files for the website.

### [common](app/README.md)

Contains the files through which the application's components interact.


## Tools, libraries, APIs

- [Leaflet](http://leafletjs.com/)
- [Flask](http://flask.pocoo.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [MongoDB](https://www.mongodb.org/)
- [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/)
- [Google Maps Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/)
- [Google Maps Elevation API](https://developers.google.com/maps/documentation/elevation/intro)
- [Digital Ocean](https://www.digitalocean.com/)