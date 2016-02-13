from os.path import dirname, basename, isfile
import glob

# Get all the modules in the current folder
modules = glob.glob(dirname(__file__)+"/*.py")
# Assign them to __all__ for automatic import
__all__ = [basename(f).split('.')[0] for f in modules if isfile(f)]
