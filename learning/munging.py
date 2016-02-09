import pandas as pd


def split(dataframe, target):
    ''' Split the features from the target. '''
    features = [column for column in dataframe.columns
                if column not in ['bikes', 'spaces']]
    X = dataframe[features]
    Y = dataframe[target].reshape(-1, 1)
    return X, Y


def temporal_features(timestamp):
    ''' Extract relevant time information from a list of timestamps. '''
    features = {
        'hour': timestamp.hour,
        'minute': timestamp.minute,
        'weekday': timestamp.weekday()
        # Season?
        # Holiday?
    }
    return features


def prepare(dataframe):
    ''' Extract features and label them as categorical or numerical. '''
    # Just to be sure, drop the duplicates
    dataframe = dataframe.groupby(dataframe.index).first()
    # Extract temporal features
    temporalFeatures = [temporal_features(timestamp) for timestamp
                        in dataframe.index]
    temporalFeatures = pd.DataFrame(temporalFeatures)
    temporalFeatures = temporalFeatures.set_index(dataframe.index)
    dataframe = dataframe.join(temporalFeatures)
    # Interpolate the missing values
    # dataframe = dataframe.interpolate(method='time')
    return dataframe
