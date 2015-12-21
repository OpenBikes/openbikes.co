# MongoDB

## Explanation

## Schemes

### Time series database

    {
        ...
        city: string
        {
            _id: date (yyyy-mm-dd)
            updates (u): [
                ...
                {
                    station name (n): string
                    information (i): [
                        ...
                        {
                            update time (m): time (hh:mm:ss)
                            available bikes (b): integer
                            available bike stands (s): integer
                            celsius temperature (t): integer
                            humidity percentage (h): integer
                            wind speed in kilometers (w): integer
                            cloud coverage percentage (c): integer
                        }
                        ...
                    ]
                }
                ...
            ]
        }
        ...
    }

### Geographical database
    
    {
        ...
        city: string
        {
            _id: station name
            altitude (a): float
            position: [
                longitude: float
                latitude: float
            ]
        }
        ...
    }

## Abbreviations

The databases uses abbreviations in order to save memory.

### Time series database

| Abbreviation | Signification          |
|--------------|------------------------|
| u            | Updates                |
| i            | Information            |
| m            | Moment (hh:mm:ss)      |
| b            | Bikes                  |
| s            | Stands                 |
| t            | Temperature in celsius |
| h            | Humidity percentage    |
| w            | Wind speed             |
| c            | Cloudiness percentage  |

### Geographical database

| Abbreviation | Signification |
|--------------|---------------|
| p            | Position      |
| a            | Altitude      |