import requests
import json
import weatherCredentials
from importAPI.common import common

#Constants
API_KEY=weatherCredentials.APIKEY
API_URL='https://api.jcdecaux.com/vls/v1/stations' ### TODO Maj weather
DEFAULT_CONTRACT='Paris' ### TODO Maj weather


def importStationsStates(contract=DEFAULT_CONTRACT):
    # Build and send the request
    r = requests.get(API_URL, params={'apiKey': API_KEY, 'contract': contract})

    # Parse received JSON
    parsed_json = json.loads(r.text)

    for station in parsed_json:
        common.insertvelibstation(station)

