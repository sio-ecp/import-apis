import sqlCredentials
from peewee import *

# Constants
DBname=sqlCredentials.DB
DBuser=sqlCredentials.USER
DBpassword=sqlCredentials.PASSWORD
DBport=sqlCredentials.PORT
DBhost=sqlCredentials.HOST

# Db connection
db = MySQLDatabase(DBname, host=DBhost, port=DBport, user=DBuser, passwd=DBpassword)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Station(BaseModel):
    id_station = PrimaryKeyField()
    station_number = IntegerField()
    station_name = CharField(255)
    contract_name = CharField(255)
    address = CharField(255)
    banking = BooleanField()
    bonus = BooleanField()
    status = BooleanField()
    operational_bike_stands = IntegerField()
    available_bike_stands = IntegerField()
    available_bikes = IntegerField()
    last_update = BigIntegerField()
    latitude = FloatField()
    longitude = FloatField()
    city_name = CharField(255)
    country_code = CharField(255)

class Weather(BaseModel):
    id_weather = PrimaryKeyField()
    weather_group = CharField(255)
    pressure = IntegerField()
    humidity_percentage = FloatField()
    temperature = FloatField()
    min_temperature = FloatField()
    max_temperature = FloatField()
    wind_speed = FloatField()
    wind_direction = FloatField()
    cloudiness_percentage = IntegerField()
    rain_quantity = IntegerField()
    snow_quantity = IntegerField()
    sun_set = BigIntegerField()
    sun_rise = BigIntegerField()
    calculation_time = BigIntegerField()
    latitude = FloatField()
    longitude = FloatField()
    city_name = CharField(255)
    country_code = CharField(255)

# Create Tables if no exist
db.create_tables([Station], safe=True)
db.create_tables([Weather], safe=True)