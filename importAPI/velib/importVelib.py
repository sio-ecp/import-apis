import requests
import json
import velibCredentials
from importAPI.common import common

#Constants
API_KEY=velibCredentials.APIKEY
API_URL='https://api.jcdecaux.com/vls/v1/stations'
DEFAULT_CONTRACT='Paris'


def importStationsStates(contract=DEFAULT_CONTRACT):
    """Imports the current station information, for the provided contract (city)"""

    # Build and send the request
    r = requests.get(API_URL, params={'apiKey': API_KEY, 'contract': contract})

    # Parse received JSON
    parsed_json = json.loads(r.text)

    for station in parsed_json:
        common.insertvelibstation(station)

