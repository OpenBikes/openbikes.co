import { fetchJson } from './util'

export const fetchCities = () => fetchJson('GET', '/api/cities')
export const fetchCity = (citySlug) => fetchJson('GET', `/api/cities?city_slug=${citySlug}`)
export const fetchStations = (citySlug) => fetchJson('GET', `/api/geojson/${citySlug}`)
