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
    """Represents the database in which data will be inserted, for peewee use"""
    class Meta:
        database = db


class Station(BaseModel):
    """Represents the Station SQL table"""
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
    """Represents the Weather SQL table"""
    id_weather = PrimaryKeyField()
    weather_group = CharField(255)
    pressure = IntegerField()
    humidity_percentage = FloatField()
    temperature = FloatField()
    min_temperature = FloatField()
    max_temperature = FloatField()
    wind_speed = FloatField()
    wind_direction = FloatField(default=-1.0) # Default is negative (wind direction not provided)
    cloudiness_percentage = IntegerField()
    rain_quantity = IntegerField(default=0)
    snow_quantity = IntegerField(default=0)
    sun_set = BigIntegerField()
    sun_rise = BigIntegerField()
    calculation_time = BigIntegerField()
    latitude = FloatField()
    longitude = FloatField()
    city_name = CharField(255)
    country_code = CharField(255)


# Create Tables if no exist
# -> Tells peewee to create the tables if they do not exist in the DB
db.create_tables([Station], safe=True)
db.create_tables([Weather], safe=True)