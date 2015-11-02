import pandas as pd

def rename_columns(dataframe):
    '''
    The data is stored in MongoDB with shortcuts for the attributes in order
    to save memory. This function renames the columns appropriately.
    '''
    shortcuts = {
        'b': 'bikes',
        's': 'spaces'
    }
    dataframe.rename(columns=shortcuts, inplace=True)
    return dataframe

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
    # Extract time features
    timeFeatures = [temporal_features(timestamp) for timestamp
                    in dataframe.index]
    timeFeatures = pd.DataFrame(timeFeatures)
    timeFeatures = timeFeatures.set_index(dataframe.index)
    dataframe = dataframe.join(timeFeatures)
    # Interpolate the missing values
    dataframe = dataframe.interpolate(method='time')
    return dataframe