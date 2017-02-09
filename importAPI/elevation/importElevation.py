import requests
import json
import elevationCredentials
from importAPI.common import common

# Constants
API_KEY=elevationCredentials.APIKEY
API_URL='https://maps.googleapis.com/maps/api/elevation/json'


def importElevation(lat, lng):
    """Imports the elevation for provided location"""
    location = str(lat)+","+str(lng)
    # Build and send the request
    r = requests.get(API_URL, params={'key': API_KEY, 'locations': location})

    # Parse received JSON
    parsed_json = json.loads(r.text)
    if parsed_json['status'] == 'OVER_QUERY_LIMIT':
        return False

    return parsed_json

