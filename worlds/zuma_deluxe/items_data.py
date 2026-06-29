
from typing import TypedDict,  List, Dict
from BaseClasses import ItemClassification
import enum

from worlds.tloz.Items import useful, filler


class Union(enum.Enum):
    PREFIX = -1
    SUFIX = 1

class Group(enum.Enum):
    TRAP = -1
    FILLER = 0
    USEFUL = 1





class ItemData(TypedDict):
    name: str
    classification: ItemClassification

class SubItemDict(ItemData):
        union: Union

class FillerDict(ItemData):

    group: Group


sub_item_data: List[SubItemDict] =[
    SubItemDict(
        name="Coins",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Gaps",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Combos",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Chains",
        union= Union.SUFIX,
        classification=ItemClassification.progression
    ),
    SubItemDict(
        name="Unlock:",
        union= Union.PREFIX,
        classification=ItemClassification.progression
    ),
]

item_data: List[ItemData] =[
    ItemData(
        name = "Progressive Lives",
        classification = ItemClassification.useful
    ),
    ItemData(
        name = "Progressive Difficulty",
        classification = ItemClassification.progression
    ),
    ItemData(
        name = "Sun Idol",
        classification= ItemClassification.progression
    ),
    ItemData(
        name = "Sun Idol",
        classification= ItemClassification.useful
    ),
    ItemData(
        name = "Sun Idol",
        classification= ItemClassification.filler
    ),


]

extra_items: List[FillerDict] = [
    FillerDict(
        name = "Happy Sun",
        group = Group.FILLER,
        classification=ItemClassification.filler
    ),
    FillerDict(
        name = "Extra Live",
        group = Group.USEFUL,
        classification=ItemClassification.useful
    ),

    FillerDict(
        name = "Combo Killer Trap",
        group = Group.TRAP,
        classification=ItemClassification.trap
    ),
    FillerDict(
        name="Extra Coin",
        group = Group.USEFUL,
        classification=ItemClassification.useful
    ),
    FillerDict(
        name="Half Score Trap",
        group = Group.TRAP,
        classification=ItemClassification.trap
    ),
    FillerDict(
        name = "Color Shift Trap",
        group = Group.TRAP,
        classification = ItemClassification.trap
    ),
    FillerDict(
        name = "Rush Trap",
        group = Group.TRAP,
        classification=ItemClassification.trap
    ),
    FillerDict(
        name = "Get a Break",
        group = Group.USEFUL,
        classification=ItemClassification.useful
    ),
]

items_name_to_ids: Dict[str,int] = {
    "Progressive Lives": 1,
    "Progressive Difficulty": 2,
    "Sun Idol": 3,
    "Happy Sun": 4,
    "Extra Live": 5,
    "Combo Killer Trap": 6,
    "Extra Coin": 7,
    "Half Score Trap": 8,
    "Color Shift Trap": 9,
    "Rush Trap": 10,
    "Get a Break": 11,
    "Spiral of Doom (Coins)": 101,
    "Spiral of Doom (Gaps)": 102,
    "Spiral of Doom (Combos)": 103,
    "Spiral of Doom (Chains)": 104,
    "Board Unlock: Spiral of Doom": 109,
    "Osprey Talon (Coins)": 2701,
    "Osprey Talon (Gaps)": 2702,
    "Osprey Talon (Combos)": 2703,
    "Osprey Talon (Chains)": 2704,
    "Board Unlock: Osprey Talon": 2709,
    "Riverbed Mosaic (Coins)": 5301,
    "Riverbed Mosaic (Gaps)": 5302,
    "Riverbed Mosaic (Combos)": 5303,
    "Riverbed Mosaic (Chains)": 5304,
    "Board Unlock: Riverbed Mosaic": 5309,
    "Breath of Ethecatl (Coins)": 7901,
    "Breath of Ethecatl (Gaps)": 7902,
    "Breath of Ethecatl (Combos)": 7903,
    "Breath of Ethecatl (Chains)": 7904,
    "Board Unlock: Breath of Ethecatl": 7909,
    "Dark Vortex (Coins)": 10501,
    "Dark Vortex (Gaps)": 10502,
    "Dark Vortex (Combos)": 10503,
    "Dark Vortex (Chains)": 10504,
    "Board Unlock: Dark Vortex": 10509,
    "SwitchBack (Coins)": 13101,
    "SwitchBack (Gaps)": 13102,
    "SwitchBack (Combos)": 13103,
    "SwitchBack (Chains)": 13104,
    "Board Unlock: SwitchBack": 13109,
    "Long Range (Coins)": 15701,
    "Long Range (Gaps)": 15702,
    "Long Range (Combos)": 15703,
    "Long Range (Chains)": 15704,
    "Board Unlock: Long Range": 15709,
    "When Spirals Attack (Coins)": 18301,
    "When Spirals Attack (Gaps)": 18302,
    "When Spirals Attack (Combos)": 18303,
    "When Spirals Attack (Chains)": 18304,
    "Board Unlock: When Spirals Attack": 18309,
    "Mud Slide (Coins)": 20901,
    "Mud Slide (Gaps)": 20902,
    "Mud Slide (Combos)": 20903,
    "Mud Slide (Chains)": 20904,
    "Board Unlock: Mud Slide": 20909,
    "Rorschach (Coins)": 23501,
    "Rorschach (Gaps)": 23502,
    "Rorschach (Combos)": 23503,
    "Rorschach (Chains)": 23504,
    "Board Unlock: Rorschach": 23509,
    "Mouth of Centeotl (Coins)": 26101,
    "Mouth of Centeotl (Gaps)": 26102,
    "Mouth of Centeotl (Combos)": 26103,
    "Mouth of Centeotl (Chains)": 26104,
    "Board Unlock: Mouth of Centeotl": 26109,
    "Snake Pit (Coins)": 28701,
    "Snake Pit (Gaps)": 28702,
    "Snake Pit (Combos)": 28703,
    "Snake Pit (Chains)": 28704,
    "Board Unlock: Snake Pit": 28709,
    "Sand Garden (Coins)": 31301,
    "Sand Garden (Gaps)": 31302,
    "Sand Garden (Combos)": 31303,
    "Sand Garden (Chains)": 31304,
    "Board Unlock: Sand Garden": 31309,
    "Lair of The Mud Snake (Coins)": 33901,
    "Lair of The Mud Snake (Gaps)": 33902,
    "Lair of The Mud Snake (Combos)": 33903,
    "Lair of The Mud Snake (Chains)": 33904,
    "Board Unlock: Lair of The Mud Snake": 33909,
    "Lan Ding Pad (Coins)": 36501,
    "Lan Ding Pad (Gaps)": 36502,
    "Lan Ding Pad (Combos)": 36503,
    "Lan Ding Pad (Chains)": 36504,
    "Board Unlock: Lan Ding Pad": 36509,
    "Altar of Tlaloc (Coins)": 39101,
    "Altar of Tlaloc (Gaps)": 39102,
    "Altar of Tlaloc (Combos)": 39103,
    "Altar of Tlaloc (Chains)": 39104,
    "Board Unlock: Altar of Tlaloc": 39109,
    "Code of Mixtec (Coins)": 41701,
    "Code of Mixtec (Gaps)": 41702,
    "Code of Mixtec (Combos)": 41703,
    "Code of Mixtec (Chains)": 41704,
    "Board Unlock: Code of Mixtec": 41709,
    "Shrine of Quetzalcoatl (Coins)": 44301,
    "Shrine of Quetzalcoatl (Gaps)": 44302,
    "Shrine of Quetzalcoatl (Combos)": 44303,
    "Shrine of Quetzalcoatl (Chains)": 44304,
    "Board Unlock: Shrine of Quetzalcoatl": 44309,
    "Mirror Serpent (Coins)": 46901,
    "Mirror Serpent (Gaps)": 46902,
    "Mirror Serpent (Combos)": 46903,
    "Mirror Serpent (Chains)": 46904,
    "Board Unlock: Mirror Serpent": 46909,
    "Sun Stone (Coins)": 49501,
    "Sun Stone (Gaps)": 49502,
    "Sun Stone (Combos)": 49503,
    "Sun Stone (Chains)": 49504,
    "Board Unlock: Sun Stone": 49509,
    "Zumaic Exodus (Coins)": 52101,
    "Zumaic Exodus (Gaps)": 52102,
    "Zumaic Exodus (Combos)": 52103,
    "Zumaic Exodus (Chains)": 52104,
    "Board Unlock: Zumaic Exodus": 52109,
    "Space (Coins)": 54701,
    "Space (Gaps)": 54702,
    "Space (Combos)": 54703,
    "Space (Chains)": 54704,
    "Board Unlock: Space": 54709,
    "Temple of Zukulkan 1 (Coins)": 57305,
    "Temple of Zukulkan 1 (Gaps)": 57306,
    "Temple of Zukulkan 1 (Combos)": 57307,
    "Temple of Zukulkan 1 (Chains)": 57308,
    "Stage Unlock: Temple of Zukulkan 1": 57310,
    "Temple of Zukulkan 2 (Coins)": 57905,
    "Temple of Zukulkan 2 (Gaps)": 57906,
    "Temple of Zukulkan 2 (Combos)": 57907,
    "Temple of Zukulkan 2 (Chains)": 57908,
    "Stage Unlock: Temple of Zukulkan 2": 57910,
    "Temple of Zukulkan 3 (Coins)": 58505,
    "Temple of Zukulkan 3 (Gaps)": 58506,
    "Temple of Zukulkan 3 (Combos)": 58507,
    "Temple of Zukulkan 3 (Chains)": 58508,
    "Stage Unlock: Temple of Zukulkan 3": 58510,
    "Quetzal Quatl 1 (Coins)": 59105,
    "Quetzal Quatl 1 (Gaps)": 59106,
    "Quetzal Quatl 1 (Combos)": 59107,
    "Quetzal Quatl 1 (Chains)": 59108,
    "Stage Unlock: Quetzal Quatl 1": 59110,
    "Quetzal Quatl 2 (Coins)": 59805,
    "Quetzal Quatl 2 (Gaps)": 59806,
    "Quetzal Quatl 2 (Combos)": 59807,
    "Quetzal Quatl 2 (Chains)": 59808,
    "Stage Unlock: Quetzal Quatl 2": 59810,
    "Quetzal Quatl 3 (Coins)": 60505,
    "Quetzal Quatl 3 (Gaps)": 60506,
    "Quetzal Quatl 3 (Combos)": 60507,
    "Quetzal Quatl 3 (Chains)": 60508,
    "Stage Unlock: Quetzal Quatl 3": 60510,
    "Popo Poyolli 1 (Coins)": 61205,
    "Popo Poyolli 1 (Gaps)": 61206,
    "Popo Poyolli 1 (Combos)": 61207,
    "Popo Poyolli 1 (Chains)": 61208,
    "Stage Unlock: Popo Poyolli 1": 61210,
    "Popo Poyolli 2 (Coins)": 62005,
    "Popo Poyolli 2 (Gaps)": 62006,
    "Popo Poyolli 2 (Combos)": 62007,
    "Popo Poyolli 2 (Chains)": 62008,
    "Stage Unlock: Popo Poyolli 2": 62010,
    "Popo Poyolli 3 (Coins)": 62805,
    "Popo Poyolli 3 (Gaps)": 62806,
    "Popo Poyolli 3 (Combos)": 62807,
    "Popo Poyolli 3 (Chains)": 62808,
    "Stage Unlock: Popo Poyolli 3": 62810,
    "Secret Shrine Of Zuma 1 (Coins)": 63605,
    "Secret Shrine Of Zuma 1 (Gaps)": 63606,
    "Secret Shrine Of Zuma 1 (Combos)": 63607,
    "Secret Shrine Of Zuma 1 (Chains)": 63608,
    "Stage Unlock: Secret Shrine Of Zuma 1": 63610,
    "Secret Shrine Of Zuma 2 (Coins)": 64405,
    "Secret Shrine Of Zuma 2 (Gaps)": 64406,
    "Secret Shrine Of Zuma 2 (Combos)": 64407,
    "Secret Shrine Of Zuma 2 (Chains)": 64408,
    "Stage Unlock: Secret Shrine Of Zuma 2": 64410,
    "Secret Shrine Of Zuma 3 (Coins)": 65205,
    "Secret Shrine Of Zuma 3 (Gaps)": 65206,
    "Secret Shrine Of Zuma 3 (Combos)": 65207,
    "Secret Shrine Of Zuma 3 (Chains)": 65208,
    "Stage Unlock: Secret Shrine Of Zuma 3": 65210,
    "Stage Unlock: Space": 66011,
}

items_ids_to_names: Dict[int, str] = {ids: name   for name, ids in items_name_to_ids.items()}