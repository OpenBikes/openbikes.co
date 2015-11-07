from sklearn.ensemble import RandomForestRegressor
from lib import tools


def fit(dataframe, target, city, station):
    ''' Train the random forest to predict bikes or spaces. '''
    features = [column for column in dataframe.columns
                if column not in ['bikes', 'spaces']]
    X = dataframe[features]
    Y = dataframe[target]
    regressor = RandomForestRegressor(n_estimators=12, n_jobs=-1, max_depth=10)
    regressor.fit(X, Y)
    tools.save_predictor(regressor, 'forest', target, city, station)


def predict(features, target, city, station):
    '''
    Make a prediction for the number of bikes or spaces for a station
    according to some variables.
    '''
    regressor = tools.load_predictor('forest', target, city, station)
    prediction = regressor.predict(features)
    return prediction[0]
