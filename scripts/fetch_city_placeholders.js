const _ = require('lodash')
const dotenv = require('dotenv')
const fs = require('fs')
const request = require('request')

dotenv.load()

const IMG_SIZE = '500x350'
const MAPS_PATH = 'src/assets/city_placeholders'
const mapUrl = (country, city) => `http://maps.googleapis.com/maps/api/staticmap?center=${city},+${country}&zoom=12&scale=2&size=${IMG_SIZE}&maptype=terrain&format=png&visual_refresh=true&key=${process.env.GOOGLE_MAPS_STATIC_API}`

function downloadGoogleStaticMapAPI (country, city) {
  const dest = `${process.cwd()}/${MAPS_PATH}/${city}.png`
  const file = fs.createWriteStream(dest)

  return new Promise((resolve, reject) => {
    const sendReq = request.get(mapUrl(country, city))
    const payload = { country, city }

    sendReq.on('response', res => {
      if (res.statusCode !== 200) {
        return reject(payload, `Response status was ${res.statusCode}`)
      }
      return null
    })

    sendReq.on('error', err => {
      fs.unlink(dest)
      if (err) reject(payload, err.message)
    })

    sendReq.pipe(file)

    file.on('finish', () => {
      file.close()
      resolve(payload)
    })

    file.on('error', err => {
      fs.unlink(dest)
      if (err) reject(payload, err.message)
    })
  })
}

if (!fs.existsSync(MAPS_PATH)) { fs.mkdirSync(MAPS_PATH) }

// Download the placeholder map for each city
request({ method: 'GET', json: true, url: 'http://api.openbikes.co/cities' }, (err, res, cities) => {
  if (!err && res.statusCode === 200) {
    _.forEach(cities, city => {
      downloadGoogleStaticMapAPI(city.country, city.slug)
      .then(r => console.log(`[${r.country}] ${r.city} : file downloaded (no issues)`))
      .catch((r, e) => console.error(`[${r.country}] ${r.city} : downloading error`, e))
    })
  }
})
