from common import toolbox as tb
from common import files, settings
from tasks import update

# Providers file
providers = tb.read_json(files.providers)
# Predictions file
predictions = tb.read_json(files.predictions)

for provider, cities in providers.items():
    for city in cities:
        update(provider, city, predictions[city])
