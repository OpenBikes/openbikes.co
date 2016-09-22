const fs = require('fs')
const _ = require('lodash')
const request = require('request')
const dotenv = require('dotenv')

dotenv.load()

API_CITIES_URL = 'http://api.openbikes.co/cities'
CITIES_ENDPOINT = 'cities'
IMG_SIZE = '500x350'
MAPS_PATH = 'src/img/cityMapBackground'

var googleStaticMapAPI = (country, city, size) => `http://maps.googleapis.com/maps/api/staticmap?center=${city},+${country}&zoom=12&scale=2&size=${size}&maptype=terrain&format=png&visual_refresh=true&key=${process.env.GOOGLE_MAPS_STATIC_API}`

var fileDest = (country, city) => `${process.cwd()}/${MAPS_PATH}/${city}_${country}.png`

function queryOptions(queryUrl) {
  return { 
  	method: 'get', 
  	json: true, 
  	url: queryUrl 
  }
}

request(queryOptions(API_CITIES_URL), function (err, res, body) {
  if (!err && res.statusCode == 200) {
  	cities = body.cities
  	_.forEach(cities, function(dict) {
  		
      country = dict.country
  		city = dict.slug

		  downloadGoogleStaticMapAPI(country, city)
        .then( (metadata) => console.log(`[${metadata.country}] ${metadata.city} : file downloaded (no issues)`))
        .catch( (metadata, err) => console.error(`[${metadata.country}] ${metadata.city} : error encountered while downloading`, err))
	  })
  }
  return 
})


function downloadGoogleStaticMapAPI(country, city) {
  var mapsUrl = googleStaticMapAPI(country, city, IMG_SIZE)
  dest = fileDest(country, city)

  var file = fs.createWriteStream(dest)
  
  return new Promise((resolve, reject) => {

    var sendReq = request.get(mapsUrl)

    var metadata = { country, city }
    
    // verify response code
    sendReq.on('response', function(res) {
        if (res.statusCode !== 200) {
            return reject(metadata, `Response status was ${res.statusCode}`)
        }
    })

    // check for request errors
    sendReq.on('error', function (err) {
        fs.unlink(dest)

        if (err) {
            reject(metadata, err.message)
        }
    })

    sendReq.pipe(file)

    file.on('finish', function() {
        file.close()
        resolve(metadata)
    })

    file.on('error', function(err) {
        fs.unlink(dest)
        if (err) {
            reject(metadata, err.message)
        }
    })

  })
}