from importAPI.common import common
from importAPI.velib import importVelib
from importAPI.weather import importWeather
from importAPI.common import sqlModels

# Old way -> Don't do it!
# import imp
# common = imp.load_source('common', '../importAPI/common/common.py')


def test_common():
    assert(common.doCommon(True) == "OK")
    assert(common.doCommon(False) == "KO")


def testweather():
    countBefore = sqlModels.Weather.select().count()
    importWeather.importWeatherState()
    countAfter = sqlModels.Weather.select().count()
    assert (countBefore < countAfter)


def testvelib():
    countBeforeV = sqlModels.Station.select().count()
    countBeforeE = sqlModels.StationElevation.select().count()

    importVelib.importStationsStates('Paris')

    countAfterV = sqlModels.Station.select().count()
    countAfterE = sqlModels.StationElevation.select().count()

    assert(countBeforeV < countAfterV)
    assert(countBeforeE < countAfterE) #TODO improve this test (counter will not necessarly be incremented)


