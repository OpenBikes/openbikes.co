# City bikes feeds

## Normalization

There are many providers that cover various cities throughout the world. Every provider has an API that possesses it's own standard and it's own variable names. The idea is that when the ``collect.py`` robot collects data it filters the data into a common file shape. The goal is to obtain the following from every API:

	{
		name: string,
        address: string (identical to name if not provided),
        lat: float,
        lon': float,
        status: string ('OPEN' or 'CLOSED'),
        bikes: integer,
        stands: integer,
        update: timestamp (ISO format)
    }

There is a script for every API in ``lib/providers/``. Every script contains a ``normalization(data)`` function.

## Providers

Some of the APIs do not return times for the latest update on the station. Guessing by taking the current time is not a good idea for more than one reason. Hence we only use APIs that provide update times and keep hoping the other APIs will include them in their service.

### With update times

#### JCDecaux

- Command line argument: ``jcdecaux``
- [Website](https://developer.jcdecaux.com/#/home)
- JSON
- API key

| City               | Country    |
|--------------------|------------|
| Amiens             | France     |
| Besancon           | France     |
| Bruxelles-Capitale | Belgium    |
| Cergy-Pontoise     | France     |
| Creteil            | France     |
| Dublin             | Irlande    |
| Goteborg           | Sweden     |
| Kazan              | Russia     |
| Lillestrom         | Norway     |
| Ljubljana          | Slovenia   |
| Lund               | Sweden     |
| Luxembourg         | Luxembourg |
| Lyon               | France     |
| Marseille          | France     |
| Mulhouse           | France     |
| Namur              | France     |
| Nancy              | France     |
| Nantes             | France     |
| Paris              | France     |
| Rouen              | France     |
| Seville            | Spain      |
| Stockholm          | Sweden     |
| Toulouse           | France     |
| Toyama             | Japan      |
| Valence            | Spain      |
| Vilnius            | Lithuania  |

#### Capital Bikeshare

- Command line argument: ``capitalbikeshare``
- [Website](https://www.capitalbikeshare.com/)
- XML

| City               | Country    |
|--------------------|------------|
| Washington-DC      | USA     	  |

#### Citibike

- Command line argument: ``citibike``
- [Website](https://www.citibikenyc.com/)
- JSON

| City               | Country    |
|--------------------|------------|
| New-York      	 | USA     	  |

#### Hubway

- Command line argument: ``hubway``
- [Website](http://www.thehubway.com/)
- XML

| City               | Country    |
|--------------------|------------|
| Boston             | USA        |

#### Nice Ride Minnesota

- Command line argument: ``niceride``
- [Website](https://www.niceridemn.org/)
- XML

| City               | Country    |
|--------------------|------------|
| Minneapolis        | USA        |

#### BIXI

Toronto is bugged and Ottawa doesn't seem to be working.

- Command line argument: ``bixi``
- [Website](https://montreal.bixi.com/)
- XML

| City               | Country    |
|--------------------|------------|
| Toronto            | Canada     |
| Montréal           | Canada     |
| Ottawa             | Canada     |

#### Keolis

- Command line argument: ``keolis``
- [Website](http://data.keolis-rennes.com/)
- JSON or XML
- API key

| City               | Country    |
|--------------------|------------|
| Rennes             | France     |

#### Kyoto Machikado Minaport

- Command line argument: ``machikado``
- [Website](http://minaport.ubweb.jp/station.html)
- XML

| City               | Country    |
|--------------------|------------|
| Kyoto Minaport     | Japan      |

### Without update times (useless for the moment)

Keep checking!

#### Divvy

- Command line argument: ``divvy``
- [Website](http://www.divvybikes.com/)
- JSON

| City               | Country    |
|--------------------|------------|
| Chicago            | USA        |

#### Bay Area bikeshare

- Command line argument: ``bayarea``
- [Website](http://www.bayareabikeshare.com/)
- JSON

| City               | Country    |
|--------------------|------------|
| San Francisco      | USA        |

#### Bike Chattanooga

- Command line argument: ``bikechattanooga``
- [Website](http://www.bikechattanooga.com/)
- JSON

| City               | Country    |
|--------------------|------------|
| Chattanooga        | USA        |

#### Santander

- Command line argument: ``santander``
- [Website](https://api-portal.tfl.gov.uk/docs)
- XML

| City               | Country    |
|--------------------|------------|
| London             | UK        |