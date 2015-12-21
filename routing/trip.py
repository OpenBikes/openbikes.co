from copy import deepcopy
from common import toolbox as tb
from routing.building import choose, turn_by_turn


def take_bike(situation):
    path = choose(situation, 'bikes', 'walking', 'walking', False)
    route = turn_by_turn(path)
    return [route]


def drop_bike(situation):
    path = choose(situation, 'spaces', 'bicycling', 'bicycling', False)
    route = turn_by_turn(path)
    return [route]


def full_trip(situation):
    ''' We can use the previous functions. '''
    # Find the route from the departure to the departure station
    situationOne = deepcopy(situation)
    situationOne['arrival'] = situationOne['departure']
    firstPath = choose(situationOne, 'bikes', 'walking', 'walking', False)
    # Find the route from the arrival station to the arrival
    situationTwo = deepcopy(situation)
    situationTwo['departure'] = situationTwo['arrival']
    secondPath = choose(situationTwo, 'spaces', 'walking', 'walking', True)
    # Find the route between both stations
    firstStation = firstPath['points'][1]
    secondStation = secondPath['points'][0]
    A = [firstStation['lat'], firstStation['lon']]
    B = [secondStation['lat'], secondStation['lon']]
    intermediatePath = tb.reshape('bicycling', A, B)
    # Generate the routes
    routes = [
        turn_by_turn(firstPath),
        turn_by_turn(intermediatePath),
        turn_by_turn(secondPath)
    ]
    return routes
