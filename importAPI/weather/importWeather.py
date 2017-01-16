import requests
import json
import weatherCredentials
from importAPI.common import common

#Constants
API_KEY=weatherCredentials.APIKEY
API_URL='http://api.openweathermap.org/data/2.5/weather'
DEFAULT_CITY='paris,fr'


def importWeatherState(city=DEFAULT_CITY):
    """Imports the current weather information, for the provided city"""

    # Build and send the request
    r = requests.get(API_URL, params={'APPID': API_KEY, 'q': city})

    # Parse received JSON
    parsed_json = json.loads(r.text)

    common.insertweather(parsed_json)

