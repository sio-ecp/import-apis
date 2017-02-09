import sqlModels


def insertvelibstation(values):
    """Creates and fill a velib Station line in the DB using provided values"""
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


def insertweather(values):
    """Creates and fill a weather information line in the DB using provided values"""
    weather = sqlModels.Weather()
    weather.weather_group = values['weather'][0]['main']  # TODO: is it the right data here?
    weather.temperature = values['main']['temp']
    weather.pressure = values['main']['pressure']
    weather.humidity_percentage = values['main']['humidity']
    weather.min_temperature = values['main']['temp_min']
    weather.max_temperature = values['main']['temp_max']
    weather.wind_speed = values['wind']['speed']
    if 'deg' in values['wind']:
        weather.wind_direction = values['wind']['deg']
    weather.cloudiness_percentage = values['clouds']['all']
    if 'rain' in values:
        weather.rain_quantity = values['rain']['3h']
    if 'snow' in values:
        weather.snow_quantity = values['snow']['3h']
    weather.sun_set = values['sys']['sunset']
    weather.sun_rise = values['sys']['sunrise']
    weather.calculation_time = values['dt']
    weather.latitude = values['coord']['lat']
    weather.longitude = values['coord']['lon']
    weather.city_name = values['name']
    weather.country_code = values['id']
    weather.save()


def insertstationelevation(values, station_number):
    """Creates and fill a stationelevation information line in the DB using provided values"""
    elevation = sqlModels.StationElevation()
    elevation.station_number = station_number
    elevation.latitude = values['results'][0]['location']['lat']
    elevation.longitude = values['results'][0]['location']['lng']
    elevation.elevation = values['results'][0]['elevation']
    if 'resolution' in values['results'][0]:
        elevation.resolution = values['results'][0]['resolution']
    elevation.save()


def doeselevationexist(station_number):
    """Check if this station's elevation number is already in the DB"""
    count = sqlModels.StationElevation.select().where(sqlModels.StationElevation.station_number == station_number).count()
    return count == 1


# Travis test
def doCommon(value):
    """To test Travis and nosetest correct behaviour"""
    if value:
        return "OK"
    else:
        return "KO"
