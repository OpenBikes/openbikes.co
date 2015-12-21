from sklearn.ensemble import RandomForestRegressor
from learning import save_regressor
from learning import load_regressor
from learning import munging


def fit(dataframe, target, city, station):
    ''' Train the random forest to predict bikes or spaces. '''
    X, Y = munging.split(dataframe, target)
    regressor = RandomForestRegressor(n_estimators=12, n_jobs=-1, max_depth=10)
    regressor.fit(X, Y)
    save_regressor(regressor, 'forest', target, city, station)


def predict(features, target, city, station):
    '''
    Make a prediction for the number of bikes or spaces for a station
    according to some variables.
    '''
    regressor = load_regressor('forest', target, city, station)
    prediction = regressor.predict(features)
    return prediction[0]
