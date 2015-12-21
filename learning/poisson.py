import statsmodels.api as sm
import numpy as np
from patsy import dmatrices


def fit(dataframe, target, city, station):
    ''' Train the Poisson process to predict bikes or spaces. '''
    features = [column for column in dataframe.columns
                if column not in ['bikes', 'spaces']]
    # Create a GLM style formula (target ~ features)
    formula = '{0} ~ {1}'.format(target,
                                 ' + '.join(['C({}), Treatment'.format(feature)
                                             for feature in features]))
    y, X = dmatrices(formula, dataframe, return_type='dataframe')
    model = sm.Poisson(y, X)
    parameters = model.fit(disp=0).params
    estimatedLambda = np.exp(np.sum(parameters))
    return estimatedLambda
