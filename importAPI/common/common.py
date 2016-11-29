import sqlModels


def insertvelibstation(values):
    station = sqlModels.Station()
    station.station_number = values['number']
    station.station_name = values['contract_name']
    station.contract_name = values['name']
    station.address = values['address']
    station.banking = values['banking']
    station.bonus = values['bonus']
    station.status = values['status']
    station.operational_bike_stands = values['bike_stands']
    station.available_bike_stands = values['available_bike_stands']
    station.available_bikes = values['available_bikes']
    station.last_update = values['last_update']
    station.latitude = values['position']['lat']
    station.longitude = values['position']['lng']
    station.city_name = values['name']
    station.country_code = 'FR'
    station.save()


# Travis test
def doCommon(value):
    if value:
        return "OK"
    else:
        return "KO"
