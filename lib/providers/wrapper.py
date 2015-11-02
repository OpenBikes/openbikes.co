from lib.providers import (
    jcdecaux,
    citibike,
    capitalbikeshare,
    hubway,
    niceride,
    bixi,
    keolis,
    machikado
)

def collect(provider, city):
    return eval(provider).stations(city)