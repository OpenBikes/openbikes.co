from common import toolbox as tb
from common import files, settings
from tasks import learn

city = 'Toulouse'
# Stations file
stations = tb.read_json(files.stations)

for station in stations[city]:
    learn(city, station)
