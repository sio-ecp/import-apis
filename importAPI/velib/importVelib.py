import requests
import json
import velibCredentials
from importAPI.elevation import importElevation
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

    # Init elevation API indicator to know whereas to call or not
    elevationAPIOK = True
    maxPerImport = 5 # In order not to reach the API limit

    for station in parsed_json:
        common.insertvelibstation(station)

        stationNumber = station['number']
        contractName = station['contract_name']
        if elevationAPIOK and maxPerImport > 0:
            if not common.doeselevationexist(stationNumber, contractName):
                maxPerImport -= 1
                lat = station['position']['lat']
                lng = station['position']['lng']
                elevation = importElevation.importElevation(lat, lng)
                if not elevation:
                    elevationAPIOK = False
                else:
                    common.insertstationelevation(elevation, stationNumber, contractName)

