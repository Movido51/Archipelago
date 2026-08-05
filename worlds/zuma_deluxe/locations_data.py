from typing import Dict, TypedDict, List, Tuple, Type, Any, Set


class LocationDic(TypedDict):
    name: str
    id: int
    groups: List[str]

sub_level_locations_data: List[str] = [
    "Level Clear",
    "Ace Time",
]
sub_region_locations_data: List[str] = [
    "Full Clear",
    "Coins",
    "Chains",
    "Combo Max",
    "Combos",
    "Gaps",
]

levels_base_speed_adventure: Dict[str, float] = {
    "1-1": 0.50,
    "1-2": 0.50,
    "1-3": 0.60,
    "1-4": 0.60,
    "1-5": 0.60,

    "2-1": 0.75,
    "2-2": 0.75,
    "2-3": 0.80,
    "2-4": 0.80,
    "2-5": 0.55,

    "3-1": 0.85,
    "3-2": 0.90,
    "3-3": 0.90,
    "3-4": 0.90,
    "3-5": 0.60,


    "4-1": 0.70,
    "4-2": 0.70,
    "4-3": 0.75,
    "4-4": 0.75,
    "4-5": 0.55,
    "4-6": 0.70,

    "5-1": 0.75,
    "5-2": 0.80,
    "5-3": 0.80,
    "5-4": 0.85,
    "5-5": 0.64,
    "5-6": 0.85,

    "6-1": 0.90,
    "6-2": 0.95,
    "6-3": 0.90,
    "6-4": 0.90,
    "6-5": 0.65,
    "6-6": 0.90,


    "7-1": 0.70,
    "7-2": 0.70,
    "7-3": 0.75,
    "7-4": 0.75,
    "7-5": 0.60,
    "7-6": 0.75,
    "7-7": 0.85,

    "8-1": 0.80,
    "8-2": 0.85,
    "8-3": 0.85,
    "8-4": 0.85,
    "8-5": 0.60,
    "8-6": 0.90,
    "8-7": 0.90,

    "9-1": 0.90,
    "9-2": 0.90,
    "9-3": 0.95,
    "9-4": 0.90,
    "9-5": 0.70,
    "9-6": 0.90,
    "9-7": 0.90,


    "10-1": 0.75,
    "10-2": 0.75,
    "10-3": 0.80,
    "10-4": 0.80,
    "10-5": 0.60,
    "10-6": 0.85,
    "10-7": 0.90,

    "11-1": 0.90,
    "11-2": 0.90,
    "11-3": 0.95,
    "11-4": 0.95,
    "11-5": 0.65,
    "11-6": 0.95,
    "11-7": 0.95,

    "12-1": 1.00,
    "12-2": 1.00,
    "12-3": 1.00,
    "12-4": 1.00,
    "12-5": 0.78,
    "12-6": 0.95,
    "12-7": 0.95,

    "13-1": 0.85

}

locations_data: List[LocationDic] = [


]

locations_names_to_ids: Dict[str, int] = {}
locations_ids_to_names: Dict[int, str] = {}
location_name_groups: Dict[str, List[str]] = {}

for location in locations_data:
    locations_names_to_ids[location["name"]] = location["id"]
    locations_ids_to_names[location["id"]] = location["name"]

    for group in location["groups"]:
        location_name_groups.setdefault(group, []).append(location["name"])

