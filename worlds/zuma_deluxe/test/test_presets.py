from .bases import ZumaDeluxeTestBase

#from ..options import options_presets
# When writing a test, you'll first need to subclass unittest.TestCase.
# In our case, we'll subclass the APQuestTestBase we defined in bases.py.
#class TestExploringPresets(ZumaDeluxe):

 #   options = options_presets["exploring"]


#class TestHardProgressionPreset(APZumaDeluxe):
 #   options = options_presets["Hard Progression"]

class ZumaDeluxeTestBaseGauntlet(ZumaDeluxeTestBase):

    options = {
        "game_mode": 1,
    }

class ZumaDeluxeTestBaseADVENTRE(ZumaDeluxeTestBase):
    options = {
        "game_mode": 0,
    }


class ZumaDeluxeTestBaseExplore(ZumaDeluxeTestBase):
    options = {
        "game_mode": 2,
    }