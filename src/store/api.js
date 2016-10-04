import { fetchJson } from './util'

export const fetchStations = (city) => fetchJson('GET', `/api/geojson/${city}`)
