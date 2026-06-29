from test.bases import WorldTestBase

from ..world import ZumaDeluxe


class ZumaDeluxeTestBase(WorldTestBase):
    game = "Zuma Deluxe"
    world: ZumaDeluxe

