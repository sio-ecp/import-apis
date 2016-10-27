from importAPI.common import common

# Old way -> Don't do it!
# import imp
# common = imp.load_source('common', '../importAPI/common/common.py')


def test_common():
    assert(common.doCommon(True) == "OK")
    assert(common.doCommon(False) == "KO")


