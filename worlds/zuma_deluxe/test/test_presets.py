from .bases import ZumaDeluxeTestBase

#from ..options import options_presets
# When writing a test, you'll first need to subclass unittest.TestCase.
# In our case, we'll subclass the APQuestTestBase we defined in bases.py.
#class TestExploringPresets(ZumaDeluxe):

 #   options = options_presets["exploring"]


#class TestHardProgressionPreset(APZumaDeluxe):
 #   options = options_presets["Hard Progression"]

class TestZumaDeluxeBaseGauntlet(ZumaDeluxeTestBase):

    options = {
        "game_mode": 1,
    }

class TestZumaDeluxeBaseADVENTRE(ZumaDeluxeTestBase):
    options = {
        "game_mode": 0,
    }


class TestZumaDeluxeBaseExplore(ZumaDeluxeTestBase):
    options = {
        "game_mode": 2,
    }
class TestZumaDeluxeBaseAceTime(ZumaDeluxeTestBase):
    options = {
        "ace_time": True,
    }