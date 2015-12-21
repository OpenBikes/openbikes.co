from os.path import dirname, basename, isfile
import os
import glob
import pickle
from zipfile import ZipFile
from common import toolbox as tb

# Get all the modules in the current folder
modules = glob.glob(dirname(__file__)+"/*.py")
# Assign them to __all__ for automatic import
__all__ = [basename(f).split('.')[0] for f in modules if isfile(f)]

# Define where to save the regressors
settings = tb.read_json('common/settings.json')
folder = settings['folders']['regression']


def save_regressor(predictor, method, target, city, station):
    '''
    Save a regressor. The function starts by making a pickle
    file and then makes a zipfile. Finally it deletes the
    pickle file.
    '''
    directory = '{0}/{1}/{2}/{3}'.format(folder, method, target, city)
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = '{0}/{1}'.format(directory, station.replace('/', '_'))
    # Destroy the zipfile if it already exists
    try:
        os.remove('{0}.zip'.format(path))
    except:
        pass
    # Save the predictor
    with open('{0}.pkl'.format(path), 'wb') as outfile:
        pickle.dump(predictor, outfile)
    # Zip it
    with ZipFile('{0}.zip'.format(path), 'w') as zipped:
        zipped.write('{0}.pkl'.format(path))
    # Destroy it
    os.remove('{0}.pkl'.format(path))


def load_regressor(method, target, city, station):
    ''' Load a regressor in memory. '''
    path = '{0}/{1}/{2}/{3}/{4}'.format(folder, method, target, city,
                                        station.replace('/', '_'))
    with ZipFile('{0}.zip'.format(path)) as zf:
        zf.extractall()
    with open('{0}.pkl'.format(path), 'rb') as infile:
        os.remove('{0}.pkl'.format(path))
        predictor = pickle.load(infile)
        return predictor
