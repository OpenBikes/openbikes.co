from np.random import uniform

def split(dataframe, trainRatio=0.8):
    ''' Split a dataframe in two in order to perform cross-validation. '''
    dataframe['train'] = uniform(0, 1, len(dataframe)) <= trainRatio
    train = dataframe[dataframe['train'] == True]
    test = dataframe[dataframe['train'] == False]
    return train, test

def cross_validate(dataframe, features, target, method):
    ''' Return an accuracy score between 0 and 1. '''
    train, test = split(dataframe)
    regressor = method.train(dataframe, target)
    return 'to do'