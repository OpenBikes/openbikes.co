from routing import building

situation = {
    'city': 'Toulouse',
    'departure': (43.5609723, 1.4632229),
    'arrival': (43.60439865, 1.4433515801636),
    'people': 1,
    'time': [1450641457962]
}

#path = building.choose(situation, 'spaces', 'biking', 'biking', False)

path = {
    'mode': 'bicycling',
    'points': [
        {
            'lon': 1.4632229,
            'lat': 43.5609723
        },
        {
            'lon': 1.442101445768934,
            'lat': 43.605203861405954
        }
    ]
}

route = building.turn_by_turn(path)