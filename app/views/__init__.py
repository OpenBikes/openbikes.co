from common import toolbox as tb

settings = tb.read_json('common/settings.json')

informationFolder = settings['folders']['information']
geojsonFolder = settings['folders']['geojson']