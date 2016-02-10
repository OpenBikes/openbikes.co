# Time series database

## Scheme

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
                        }
                        ...
                    ]
                }
                ...
            ]
        }
        ...
    }

## Abbreviations

| Abbreviation | Signification          |
|--------------|------------------------|
| u            | Updates                |
| i            | Information            |
| m            | Moment (hh:mm:ss)      |
| b            | Bikes                  |
| s            | Stands                 |
