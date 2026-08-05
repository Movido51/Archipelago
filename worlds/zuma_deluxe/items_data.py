
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
        name = "Progressive Lives",
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


]
items_names_to_ids: Dict[str, int] = {}
items_ids_to_names: Dict[int, str] = {}
item_name_groups: Dict[str, List[str]] = {}

for item in items_data:
    items_names_to_ids[item["name"]] = item["id"]
    items_ids_to_names[item["id"]] = item["name"]

    for group in item["groups"]:
        item_name_groups.setdefault(group, []).append(item["name"])

