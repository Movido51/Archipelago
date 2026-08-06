
from typing import TypedDict,  List, Dict

from BaseClasses import ItemClassification
import enum

class Union(enum.Enum):
    PREFIX = -1
    SUFIX = 1

class Group(enum.Enum):
    TRAP = -1
    FILLER = 0
    USEFUL = 1

class ItemClass(TypedDict):
    name: str
    classification: ItemClassification

class SubItemDict(ItemClass):
        union: Union

class FillerDict(ItemClass):
    duration: float

class ItemDict(TypedDict):
    name: str
    id: int
    groups: List[str]



sub_item_data: List[SubItemDict] =[
    SubItemDict(
        name="Coin Points",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Gap Points",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Combo Points",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Chain Points",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Unlock:",
        union= Union.PREFIX,
        classification=ItemClassification.progression
    ),
]



item_data_classification: List[ItemClass] =[
    ItemClass(
        name = "Progressive Live",
        classification = ItemClassification.useful
    ),
    ItemClass(
        name = "Progressive Difficulty",
        classification = ItemClassification.progression
    ),
    ItemClass(
        name = "Sun Idol",
        classification= ItemClassification.progression
    ),
    ItemClass(
        name = "Sun Idol",
        classification= ItemClassification.useful
    ),
    ItemClass(
        name = "Sun Idol",
        classification= ItemClassification.filler
    ),

]



extra_items: Dict[str,FillerDict] = {
    "Happy Sun" : FillerDict(
        name = "Happy Sun",
        classification=ItemClassification.filler,
        duration = 0.5
    ),
    "Extra Live": FillerDict(
        name = "Extra Live",
        classification=ItemClassification.useful,
        duration = 0.5
    ),
    "Combo Killer": FillerDict(
        name = "Combo Killer",
        classification=ItemClassification.trap,
        duration = 0.5,
    ),
    "Chain Breaker": FillerDict(
        name = "Chain Breaker",
        classification=ItemClassification.trap,
        duration = 0.5,
    ),
    "Extra Coin": FillerDict(
        name="Extra Coin",
        classification=ItemClassification.useful,
        duration = 0.5,
    ),
    "Half Score": FillerDict(
        name="Half Score",
        classification=ItemClassification.trap,
        duration = 0.5,

    ),
    "Color Shift": FillerDict(
        name = "Color Shift",
        classification = ItemClassification.trap,
        duration = 10,
    ),
    "Rush": FillerDict(
        name = "Rush",
        classification=ItemClassification.trap,
        duration = 5,
    ),
    "Get a Break": FillerDict(
        name = "Get a Break",
        classification=ItemClassification.useful,
        duration= 10

    ),
    "Skip": FillerDict(
        name= "Skip",
        classification=ItemClassification.useful,
        duration = 0.5,
    )
}

items_data: List[ItemDict] = [
	ItemDict(
		name="Progressive Live",
		groups=["PROGRESSIVE ITEM","LIVE ITEM"],
		id=1
	),	ItemDict(
		name="Extra Live",
		groups=["EXTRA ITEM","USEFUL ITEM","LIVE ITEM"],
		id=2
	),	ItemDict(
		name="Progressive Difficulty",
		groups=["PROGRESSIVE ITEM"],
		id=3
	),	ItemDict(
		name="Sun Idol",
		groups=["PROGRESSIVE ITEM"],
		id=4
	),	ItemDict(
		name="Get a Break",
		groups=["EXTRA ITEM","USEFUL ITEM"],
		id=5
	),	ItemDict(
		name="Rush",
		groups=["EXTRA ITEM","TRAP ITEM"],
		id=6
	),	ItemDict(
		name="Half Score",
		groups=["EXTRA ITEM","TRAP ITEM"],
		id=7
	),	ItemDict(
		name="Color Shift",
		groups=["EXTRA ITEM","TRAP ITEM"],
		id=8
	),	ItemDict(
		name="Chain Breaker",
		groups=["EXTRA ITEM","TRAP ITEM"],
		id=9
	),	ItemDict(
		name="Extra Coin",
		groups=["EXTRA ITEM","USEFUL ITEM"],
		id=10
	),	ItemDict(
		name="Combo Killer",
		groups=["EXTRA ITEM","TRAP ITEM"],
		id=11
	),	ItemDict(
		name="Happy Sun",
		groups=["EXTRA ITEM","FILLER ITEM"],
		id=12
	),	ItemDict(
		name="Skip",
		groups=["EXTRA ITEM","USEFUL ITEM"],
		id=13
	),	ItemDict(
		name="Spiral of Doom (Coin Points)",
		groups=["SPIRAL OF DOOM ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=101
	),	ItemDict(
		name="Spiral of Doom (Gap Points)",
		groups=["SPIRAL OF DOOM ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=102
	),	ItemDict(
		name="Spiral of Doom (Combo Points)",
		groups=["SPIRAL OF DOOM ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=103
	),	ItemDict(
		name="Spiral of Doom (Chain Points)",
		groups=["SPIRAL OF DOOM ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=104
	),	ItemDict(
		name="Board Unlock: Spiral of Doom",
		groups=["SPIRAL OF DOOM ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=109
	),	ItemDict(
		name="Osprey Talon (Coin Points)",
		groups=["OSPREY TALON ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=2701
	),	ItemDict(
		name="Osprey Talon (Gap Points)",
		groups=["OSPREY TALON ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=2702
	),	ItemDict(
		name="Osprey Talon (Combo Points)",
		groups=["OSPREY TALON ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=2703
	),	ItemDict(
		name="Osprey Talon (Chain Points)",
		groups=["OSPREY TALON ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=2704
	),	ItemDict(
		name="Board Unlock: Osprey Talon",
		groups=["OSPREY TALON ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=2709
	),	ItemDict(
		name="Riverbed Mosaic (Coin Points)",
		groups=["RIVERBED MOSAIC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=5301
	),	ItemDict(
		name="Riverbed Mosaic (Gap Points)",
		groups=["RIVERBED MOSAIC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=5302
	),	ItemDict(
		name="Riverbed Mosaic (Combo Points)",
		groups=["RIVERBED MOSAIC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=5303
	),	ItemDict(
		name="Riverbed Mosaic (Chain Points)",
		groups=["RIVERBED MOSAIC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=5304
	),	ItemDict(
		name="Board Unlock: Riverbed Mosaic",
		groups=["RIVERBED MOSAIC ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=5309
	),	ItemDict(
		name="Breath of Ethecatl (Coin Points)",
		groups=["BREATH OF ETHECATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=7901
	),	ItemDict(
		name="Breath of Ethecatl (Gap Points)",
		groups=["BREATH OF ETHECATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=7902
	),	ItemDict(
		name="Breath of Ethecatl (Combo Points)",
		groups=["BREATH OF ETHECATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=7903
	),	ItemDict(
		name="Breath of Ethecatl (Chain Points)",
		groups=["BREATH OF ETHECATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=7904
	),	ItemDict(
		name="Board Unlock: Breath of Ethecatl",
		groups=["BREATH OF ETHECATL ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=7909
	),	ItemDict(
		name="Dark Vortex (Coin Points)",
		groups=["DARK VORTEX ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=10501
	),	ItemDict(
		name="Dark Vortex (Gap Points)",
		groups=["DARK VORTEX ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=10502
	),	ItemDict(
		name="Dark Vortex (Combo Points)",
		groups=["DARK VORTEX ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=10503
	),	ItemDict(
		name="Dark Vortex (Chain Points)",
		groups=["DARK VORTEX ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=10504
	),	ItemDict(
		name="Board Unlock: Dark Vortex",
		groups=["DARK VORTEX ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=10509
	),	ItemDict(
		name="SwitchBack (Coin Points)",
		groups=["SWITCHBACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=13101
	),	ItemDict(
		name="SwitchBack (Gap Points)",
		groups=["SWITCHBACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=13102
	),	ItemDict(
		name="SwitchBack (Combo Points)",
		groups=["SWITCHBACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=13103
	),	ItemDict(
		name="SwitchBack (Chain Points)",
		groups=["SWITCHBACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=13104
	),	ItemDict(
		name="Board Unlock: SwitchBack",
		groups=["SWITCHBACK ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=13109
	),	ItemDict(
		name="Long Range (Coin Points)",
		groups=["LONG RANGE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=15701
	),	ItemDict(
		name="Long Range (Gap Points)",
		groups=["LONG RANGE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=15702
	),	ItemDict(
		name="Long Range (Combo Points)",
		groups=["LONG RANGE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=15703
	),	ItemDict(
		name="Long Range (Chain Points)",
		groups=["LONG RANGE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=15704
	),	ItemDict(
		name="Board Unlock: Long Range",
		groups=["LONG RANGE ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=15709
	),	ItemDict(
		name="When Spirals Attack (Coin Points)",
		groups=["WHEN SPIRALS ATTACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=18301
	),	ItemDict(
		name="When Spirals Attack (Gap Points)",
		groups=["WHEN SPIRALS ATTACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=18302
	),	ItemDict(
		name="When Spirals Attack (Combo Points)",
		groups=["WHEN SPIRALS ATTACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=18303
	),	ItemDict(
		name="When Spirals Attack (Chain Points)",
		groups=["WHEN SPIRALS ATTACK ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=18304
	),	ItemDict(
		name="Board Unlock: When Spirals Attack",
		groups=["WHEN SPIRALS ATTACK ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=18309
	),	ItemDict(
		name="Mud Slide (Coin Points)",
		groups=["MUD SLIDE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=20901
	),	ItemDict(
		name="Mud Slide (Gap Points)",
		groups=["MUD SLIDE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=20902
	),	ItemDict(
		name="Mud Slide (Combo Points)",
		groups=["MUD SLIDE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=20903
	),	ItemDict(
		name="Mud Slide (Chain Points)",
		groups=["MUD SLIDE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=20904
	),	ItemDict(
		name="Board Unlock: Mud Slide",
		groups=["MUD SLIDE ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=20909
	),	ItemDict(
		name="Rorschach (Coin Points)",
		groups=["RORSCHACH ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=23501
	),	ItemDict(
		name="Rorschach (Gap Points)",
		groups=["RORSCHACH ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=23502
	),	ItemDict(
		name="Rorschach (Combo Points)",
		groups=["RORSCHACH ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=23503
	),	ItemDict(
		name="Rorschach (Chain Points)",
		groups=["RORSCHACH ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=23504
	),	ItemDict(
		name="Board Unlock: Rorschach",
		groups=["RORSCHACH ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=23509
	),	ItemDict(
		name="Mouth of Centeotl (Coin Points)",
		groups=["MOUTH OF CENTEOTL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=26101
	),	ItemDict(
		name="Mouth of Centeotl (Gap Points)",
		groups=["MOUTH OF CENTEOTL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=26102
	),	ItemDict(
		name="Mouth of Centeotl (Combo Points)",
		groups=["MOUTH OF CENTEOTL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=26103
	),	ItemDict(
		name="Mouth of Centeotl (Chain Points)",
		groups=["MOUTH OF CENTEOTL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=26104
	),	ItemDict(
		name="Board Unlock: Mouth of Centeotl",
		groups=["MOUTH OF CENTEOTL ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=26109
	),	ItemDict(
		name="Snake Pit (Coin Points)",
		groups=["SNAKE PIT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=28701
	),	ItemDict(
		name="Snake Pit (Gap Points)",
		groups=["SNAKE PIT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=28702
	),	ItemDict(
		name="Snake Pit (Combo Points)",
		groups=["SNAKE PIT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=28703
	),	ItemDict(
		name="Snake Pit (Chain Points)",
		groups=["SNAKE PIT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=28704
	),	ItemDict(
		name="Board Unlock: Snake Pit",
		groups=["SNAKE PIT ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=28709
	),	ItemDict(
		name="Sand Garden (Coin Points)",
		groups=["SAND GARDEN ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=31301
	),	ItemDict(
		name="Sand Garden (Gap Points)",
		groups=["SAND GARDEN ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=31302
	),	ItemDict(
		name="Sand Garden (Combo Points)",
		groups=["SAND GARDEN ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=31303
	),	ItemDict(
		name="Sand Garden (Chain Points)",
		groups=["SAND GARDEN ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=31304
	),	ItemDict(
		name="Board Unlock: Sand Garden",
		groups=["SAND GARDEN ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=31309
	),	ItemDict(
		name="Lair of The Mud Snake (Coin Points)",
		groups=["LAIR OF THE MUD SNAKE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=33901
	),	ItemDict(
		name="Lair of The Mud Snake (Gap Points)",
		groups=["LAIR OF THE MUD SNAKE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=33902
	),	ItemDict(
		name="Lair of The Mud Snake (Combo Points)",
		groups=["LAIR OF THE MUD SNAKE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=33903
	),	ItemDict(
		name="Lair of The Mud Snake (Chain Points)",
		groups=["LAIR OF THE MUD SNAKE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=33904
	),	ItemDict(
		name="Board Unlock: Lair of The Mud Snake",
		groups=["LAIR OF THE MUD SNAKE ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=33909
	),	ItemDict(
		name="Lan Ding Pad (Coin Points)",
		groups=["LAN DING PAD ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=36501
	),	ItemDict(
		name="Lan Ding Pad (Gap Points)",
		groups=["LAN DING PAD ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=36502
	),	ItemDict(
		name="Lan Ding Pad (Combo Points)",
		groups=["LAN DING PAD ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=36503
	),	ItemDict(
		name="Lan Ding Pad (Chain Points)",
		groups=["LAN DING PAD ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=36504
	),	ItemDict(
		name="Board Unlock: Lan Ding Pad",
		groups=["LAN DING PAD ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=36509
	),	ItemDict(
		name="Altar of Tlaloc (Coin Points)",
		groups=["ALTAR OF TLALOC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=39101
	),	ItemDict(
		name="Altar of Tlaloc (Gap Points)",
		groups=["ALTAR OF TLALOC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=39102
	),	ItemDict(
		name="Altar of Tlaloc (Combo Points)",
		groups=["ALTAR OF TLALOC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=39103
	),	ItemDict(
		name="Altar of Tlaloc (Chain Points)",
		groups=["ALTAR OF TLALOC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=39104
	),	ItemDict(
		name="Board Unlock: Altar of Tlaloc",
		groups=["ALTAR OF TLALOC ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=39109
	),	ItemDict(
		name="Code of Mixtec (Coin Points)",
		groups=["CODE OF MIXTEC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=41701
	),	ItemDict(
		name="Code of Mixtec (Gap Points)",
		groups=["CODE OF MIXTEC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=41702
	),	ItemDict(
		name="Code of Mixtec (Combo Points)",
		groups=["CODE OF MIXTEC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=41703
	),	ItemDict(
		name="Code of Mixtec (Chain Points)",
		groups=["CODE OF MIXTEC ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=41704
	),	ItemDict(
		name="Board Unlock: Code of Mixtec",
		groups=["CODE OF MIXTEC ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=41709
	),	ItemDict(
		name="Shrine of Quetzalcoatl (Coin Points)",
		groups=["SHRINE OF QUETZALCOATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=44301
	),	ItemDict(
		name="Shrine of Quetzalcoatl (Gap Points)",
		groups=["SHRINE OF QUETZALCOATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=44302
	),	ItemDict(
		name="Shrine of Quetzalcoatl (Combo Points)",
		groups=["SHRINE OF QUETZALCOATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=44303
	),	ItemDict(
		name="Shrine of Quetzalcoatl (Chain Points)",
		groups=["SHRINE OF QUETZALCOATL ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=44304
	),	ItemDict(
		name="Board Unlock: Shrine of Quetzalcoatl",
		groups=["SHRINE OF QUETZALCOATL ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=44309
	),	ItemDict(
		name="Mirror Serpent (Coin Points)",
		groups=["MIRROR SERPENT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=46901
	),	ItemDict(
		name="Mirror Serpent (Gap Points)",
		groups=["MIRROR SERPENT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=46902
	),	ItemDict(
		name="Mirror Serpent (Combo Points)",
		groups=["MIRROR SERPENT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=46903
	),	ItemDict(
		name="Mirror Serpent (Chain Points)",
		groups=["MIRROR SERPENT ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=46904
	),	ItemDict(
		name="Board Unlock: Mirror Serpent",
		groups=["MIRROR SERPENT ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=46909
	),	ItemDict(
		name="Sun Stone (Coin Points)",
		groups=["SUN STONE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=49501
	),	ItemDict(
		name="Sun Stone (Gap Points)",
		groups=["SUN STONE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=49502
	),	ItemDict(
		name="Sun Stone (Combo Points)",
		groups=["SUN STONE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=49503
	),	ItemDict(
		name="Sun Stone (Chain Points)",
		groups=["SUN STONE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=49504
	),	ItemDict(
		name="Board Unlock: Sun Stone",
		groups=["SUN STONE ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=49509
	),	ItemDict(
		name="Zumaic Exodus (Coin Points)",
		groups=["ZUMAIC EXODUS ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COIN POINTS ITEM"],
		id=52101
	),	ItemDict(
		name="Zumaic Exodus (Gap Points)",
		groups=["ZUMAIC EXODUS ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=52102
	),	ItemDict(
		name="Zumaic Exodus (Combo Points)",
		groups=["ZUMAIC EXODUS ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=52103
	),	ItemDict(
		name="Zumaic Exodus (Chain Points)",
		groups=["ZUMAIC EXODUS ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=52104
	),	ItemDict(
		name="Board Unlock: Zumaic Exodus",
		groups=["ZUMAIC EXODUS ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=52109
	),	ItemDict(
		name="Space (Gap Points)",
		groups=["SPACE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","GAP POINTS ITEM"],
		id=54702
	),	ItemDict(
		name="Space (Combo Points)",
		groups=["SPACE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","COMBO POINTS ITEM"],
		id=54703
	),	ItemDict(
		name="Space (Chain Points)",
		groups=["SPACE ITEM","GAUNTLET ITEM","POINTS ITEM","GAUNTLET POINTS ITEM","CHAIN POINTS ITEM"],
		id=54704
	),	ItemDict(
		name="Board Unlock: Space",
		groups=["SPACE ITEM","GAUNTLET ITEM","UNLOCK ITEM","GAUNTLET UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=54709
	),	ItemDict(
		name="Temple of Zukulkan 1 (Coin Points)",
		groups=["TEMPLE OF ZUKULKAN 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=57305
	),	ItemDict(
		name="Temple of Zukulkan 1 (Gap Points)",
		groups=["TEMPLE OF ZUKULKAN 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=57306
	),	ItemDict(
		name="Temple of Zukulkan 1 (Combo Points)",
		groups=["TEMPLE OF ZUKULKAN 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=57307
	),	ItemDict(
		name="Temple of Zukulkan 1 (Chain Points)",
		groups=["TEMPLE OF ZUKULKAN 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=57308
	),	ItemDict(
		name="Stage Unlock: Temple of Zukulkan 1",
		groups=["TEMPLE OF ZUKULKAN 1 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=57310
	),	ItemDict(
		name="Temple of Zukulkan 2 (Coin Points)",
		groups=["TEMPLE OF ZUKULKAN 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=57905
	),	ItemDict(
		name="Temple of Zukulkan 2 (Gap Points)",
		groups=["TEMPLE OF ZUKULKAN 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=57906
	),	ItemDict(
		name="Temple of Zukulkan 2 (Combo Points)",
		groups=["TEMPLE OF ZUKULKAN 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=57907
	),	ItemDict(
		name="Temple of Zukulkan 2 (Chain Points)",
		groups=["TEMPLE OF ZUKULKAN 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=57908
	),	ItemDict(
		name="Stage Unlock: Temple of Zukulkan 2",
		groups=["TEMPLE OF ZUKULKAN 2 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=57910
	),	ItemDict(
		name="Temple of Zukulkan 3 (Coin Points)",
		groups=["TEMPLE OF ZUKULKAN 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=58505
	),	ItemDict(
		name="Temple of Zukulkan 3 (Gap Points)",
		groups=["TEMPLE OF ZUKULKAN 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=58506
	),	ItemDict(
		name="Temple of Zukulkan 3 (Combo Points)",
		groups=["TEMPLE OF ZUKULKAN 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=58507
	),	ItemDict(
		name="Temple of Zukulkan 3 (Chain Points)",
		groups=["TEMPLE OF ZUKULKAN 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=58508
	),	ItemDict(
		name="Stage Unlock: Temple of Zukulkan 3",
		groups=["TEMPLE OF ZUKULKAN 3 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=58510
	),	ItemDict(
		name="Quetzal Quatl 1 (Coin Points)",
		groups=["QUETZAL QUATL 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=59105
	),	ItemDict(
		name="Quetzal Quatl 1 (Gap Points)",
		groups=["QUETZAL QUATL 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=59106
	),	ItemDict(
		name="Quetzal Quatl 1 (Combo Points)",
		groups=["QUETZAL QUATL 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=59107
	),	ItemDict(
		name="Quetzal Quatl 1 (Chain Points)",
		groups=["QUETZAL QUATL 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=59108
	),	ItemDict(
		name="Stage Unlock: Quetzal Quatl 1",
		groups=["QUETZAL QUATL 1 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=59110
	),	ItemDict(
		name="Quetzal Quatl 2 (Coin Points)",
		groups=["QUETZAL QUATL 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=59805
	),	ItemDict(
		name="Quetzal Quatl 2 (Gap Points)",
		groups=["QUETZAL QUATL 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=59806
	),	ItemDict(
		name="Quetzal Quatl 2 (Combo Points)",
		groups=["QUETZAL QUATL 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=59807
	),	ItemDict(
		name="Quetzal Quatl 2 (Chain Points)",
		groups=["QUETZAL QUATL 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=59808
	),	ItemDict(
		name="Stage Unlock: Quetzal Quatl 2",
		groups=["QUETZAL QUATL 2 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=59810
	),	ItemDict(
		name="Quetzal Quatl 3 (Coin Points)",
		groups=["QUETZAL QUATL 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=60505
	),	ItemDict(
		name="Quetzal Quatl 3 (Gap Points)",
		groups=["QUETZAL QUATL 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=60506
	),	ItemDict(
		name="Quetzal Quatl 3 (Combo Points)",
		groups=["QUETZAL QUATL 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=60507
	),	ItemDict(
		name="Quetzal Quatl 3 (Chain Points)",
		groups=["QUETZAL QUATL 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=60508
	),	ItemDict(
		name="Stage Unlock: Quetzal Quatl 3",
		groups=["QUETZAL QUATL 3 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=60510
	),	ItemDict(
		name="Popo Poyolli 1 (Coin Points)",
		groups=["POPO POYOLLI 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=61205
	),	ItemDict(
		name="Popo Poyolli 1 (Gap Points)",
		groups=["POPO POYOLLI 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=61206
	),	ItemDict(
		name="Popo Poyolli 1 (Combo Points)",
		groups=["POPO POYOLLI 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=61207
	),	ItemDict(
		name="Popo Poyolli 1 (Chain Points)",
		groups=["POPO POYOLLI 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=61208
	),	ItemDict(
		name="Stage Unlock: Popo Poyolli 1",
		groups=["POPO POYOLLI 1 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=61210
	),	ItemDict(
		name="Popo Poyolli 2 (Coin Points)",
		groups=["POPO POYOLLI 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=62005
	),	ItemDict(
		name="Popo Poyolli 2 (Gap Points)",
		groups=["POPO POYOLLI 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=62006
	),	ItemDict(
		name="Popo Poyolli 2 (Combo Points)",
		groups=["POPO POYOLLI 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=62007
	),	ItemDict(
		name="Popo Poyolli 2 (Chain Points)",
		groups=["POPO POYOLLI 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=62008
	),	ItemDict(
		name="Stage Unlock: Popo Poyolli 2",
		groups=["POPO POYOLLI 2 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=62010
	),	ItemDict(
		name="Popo Poyolli 3 (Coin Points)",
		groups=["POPO POYOLLI 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=62805
	),	ItemDict(
		name="Popo Poyolli 3 (Gap Points)",
		groups=["POPO POYOLLI 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=62806
	),	ItemDict(
		name="Popo Poyolli 3 (Combo Points)",
		groups=["POPO POYOLLI 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=62807
	),	ItemDict(
		name="Popo Poyolli 3 (Chain Points)",
		groups=["POPO POYOLLI 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=62808
	),	ItemDict(
		name="Stage Unlock: Popo Poyolli 3",
		groups=["POPO POYOLLI 3 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=62810
	),	ItemDict(
		name="Secret Shrine Of Zuma 1 (Coin Points)",
		groups=["SECRET SHRINE OF ZUMA 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=63605
	),	ItemDict(
		name="Secret Shrine Of Zuma 1 (Gap Points)",
		groups=["SECRET SHRINE OF ZUMA 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=63606
	),	ItemDict(
		name="Secret Shrine Of Zuma 1 (Combo Points)",
		groups=["SECRET SHRINE OF ZUMA 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=63607
	),	ItemDict(
		name="Secret Shrine Of Zuma 1 (Chain Points)",
		groups=["SECRET SHRINE OF ZUMA 1 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=63608
	),	ItemDict(
		name="Stage Unlock: Secret Shrine Of Zuma 1",
		groups=["SECRET SHRINE OF ZUMA 1 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=63610
	),	ItemDict(
		name="Secret Shrine Of Zuma 2 (Coin Points)",
		groups=["SECRET SHRINE OF ZUMA 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=64405
	),	ItemDict(
		name="Secret Shrine Of Zuma 2 (Gap Points)",
		groups=["SECRET SHRINE OF ZUMA 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=64406
	),	ItemDict(
		name="Secret Shrine Of Zuma 2 (Combo Points)",
		groups=["SECRET SHRINE OF ZUMA 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=64407
	),	ItemDict(
		name="Secret Shrine Of Zuma 2 (Chain Points)",
		groups=["SECRET SHRINE OF ZUMA 2 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=64408
	),	ItemDict(
		name="Stage Unlock: Secret Shrine Of Zuma 2",
		groups=["SECRET SHRINE OF ZUMA 2 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=64410
	),	ItemDict(
		name="Secret Shrine Of Zuma 3 (Coin Points)",
		groups=["SECRET SHRINE OF ZUMA 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COIN POINTS ITEM"],
		id=65205
	),	ItemDict(
		name="Secret Shrine Of Zuma 3 (Gap Points)",
		groups=["SECRET SHRINE OF ZUMA 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","GAP POINTS ITEM"],
		id=65206
	),	ItemDict(
		name="Secret Shrine Of Zuma 3 (Combo Points)",
		groups=["SECRET SHRINE OF ZUMA 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","COMBO POINTS ITEM"],
		id=65207
	),	ItemDict(
		name="Secret Shrine Of Zuma 3 (Chain Points)",
		groups=["SECRET SHRINE OF ZUMA 3 ITEM","ADVENTURE ITEM","POINTS ITEM","ADVENTURE POINTS ITEM","CHAIN POINTS ITEM"],
		id=65208
	),	ItemDict(
		name="Stage Unlock: Secret Shrine Of Zuma 3",
		groups=["SECRET SHRINE OF ZUMA 3 ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
		id=65210
	),        ItemDict(
                name="Stage Unlock: Space",
                groups=["SPACE STAGE ITEM","ADVENTURE ITEM","UNLOCK ITEM","ADVENTURE UNLOCK ITEM","PROGRESSIVE ITEM"],
                id=66011
        ),

]
items_names_to_ids: Dict[str, int] = {}
items_ids_to_names: Dict[int, str] = {}
item_name_groups: Dict[str, List[str]] = {}

for item in items_data:
    items_names_to_ids[item["name"]] = item["id"]
    items_ids_to_names[item["id"]] = item["name"]

    for group in item["groups"]:
        item_name_groups.setdefault(group, []).append(item["name"])

