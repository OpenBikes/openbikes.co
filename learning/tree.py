from sklearn.tree import DecisionTreeRegressor
from learning import save_regressor
from learning import load_regressor
from learning import munging


def fit(dataframe, target, city, station):
    ''' Train the decision tree to predict bikes or spaces. '''
    X, Y = munging.split(dataframe, target)
    regressor = DecisionTreeRegressor()
    regressor.fit(X, Y)
    save_regressor(regressor, 'tree', target, city, station)


def predict(features, target, city, station):
    '''
    Make a prediction for the number of bikes or spaces for a station
    according to some variables.
    '''
    regressor = load_regressor('tree', target, city, station)
    prediction = regressor.predict(features)
    return prediction[0]
