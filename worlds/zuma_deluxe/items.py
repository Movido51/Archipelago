from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from BaseClasses import Item, ItemClassification

from .items_data import item_data, sub_item_data, SubItemDict,ItemData,Union, FillerDict,extra_items
from .gameControl.enums import (
    ZumaDeluxeMode,
    ZumaDeluxeGauntletDifficulties
)



if TYPE_CHECKING:
    from .world import ZumaDeluxe


item_filler_names: List[str] = [
    
]

item_traps_names: List[str] = [

]

class ZumaDeluxeItem(Item):
    game = "Zuma Deluxe"



def get_random_filler_item_name(world: ZumaDeluxe) -> str:
    filler_item: FillerDict = world.random.choice(extra_items)
    return filler_item["name"]


def create_item_by_sub_name(world: ZumaDeluxe,sub_item:SubItemDict, name: str) -> ZumaDeluxeItem:
    item_dat: ItemData
    new_name: str = ""
    type_name: str = name.split()[0]
    lev_name = name.split("- ")[1]
    if sub_item["union"] == Union.PREFIX:
        new_name = type_name +" "+ sub_item["name"] +" " + lev_name
    elif sub_item["union"] == Union.SUFIX:
        new_name = lev_name + " ("+ sub_item["name"] + ")"
    item_dat = ItemData(
        name=new_name,
        classification=sub_item["classification"],
    )
    return create_item(world, item_dat)






def create_item(world: ZumaDeluxe,item_dat:ItemData) -> ZumaDeluxeItem:

    return ZumaDeluxeItem(item_dat["name"], item_dat["classification"],  world.item_name_to_id[item_dat["name"]],player = world.player)

def create_all_items(world: ZumaDeluxe) ->None:


    item_pool: List[ZumaDeluxeItem] = []
    for item in item_data:
        name = item["name"]
        amount:int  = 1
        if name  == "Progressive Lives":
            amount = world.maximum_lives
        if name == "Progressive Difficulty":
            if world.mode != ZumaDeluxeMode.ADVENTURE:
                if world.selected_gauntlet_difficulty is not None:
                    amount = list(ZumaDeluxeGauntletDifficulties).index(world.selected_gauntlet_difficulty)

                else:
                    amount = 0
            else:
                amount = 0
        if name == "Sun Idol":
            tot: int = world.sun_idols_total
            req: int = world.sun_idols_required
            use: int = world.sun_idols_helpers
            prog: int = (use+req+1)//2
            useful: int = max(use-req,tot//10)

            if useful+ prog > tot:
                useful = tot-prog
            fill: int = tot - useful - prog


            if item["classification"] == ItemClassification.progression:
                amount = prog

            elif item["classification"] == ItemClassification.useful:
                amount = useful

            else:
                amount = fill


        for _ in range(amount):
            item_pool.append(create_item(world,item))

    if world.mode != ZumaDeluxeMode.ADVENTURE:
        item_pool += generate_items_gauntlet(world)
    if world.mode != ZumaDeluxeMode.GAUNTLET:
        item_pool += generate_items_adventure(world)

    number_of_items = len(item_pool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_items = number_of_unfilled_locations - number_of_items

    item_pool += [world.create_filler() for _ in range(needed_items)]

    world.multiworld.itempool += item_pool

def generate_items_gauntlet(world: ZumaDeluxe) -> List[ZumaDeluxeItem]:
    gauntlet_items: List[ZumaDeluxeItem] = []
    for board in world.selected_gauntlet_levels:
        if board is None:
            continue
        board_name: str = board.value

        for board_item in sub_item_data:
            item: ZumaDeluxeItem = create_item_by_sub_name(world,board_item,board_name)
            if "Unlock" in board_item["name"] and board == world.selected_starter_gauntlet:
                world.push_precollected(item)
            else:
                gauntlet_items.append(item)
    if world.selected_goal_level_gauntlet is not None:
        if not world.selected_goal_level_gauntlet in world.selected_gauntlet_levels:
            for board_item in sub_item_data:
                item: ZumaDeluxeItem = create_item_by_sub_name(world,board_item,world.selected_goal_level_gauntlet.value)

                if "Unlock" in board_item["name"]:
                    gauntlet_items.append(item)

    return gauntlet_items
def generate_items_adventure(world: ZumaDeluxe) -> List[ZumaDeluxeItem]:
    adventure_items: List[ZumaDeluxeItem] = []
    for stage in world.selected_adventure_levels:
        if stage is None:
            continue
        stage_name: str = stage.value
        for stage_item in sub_item_data:
            item: ZumaDeluxeItem = create_item_by_sub_name(world,stage_item,stage_name)
            if "Unlock" in stage_item["name"] and stage == world.selected_starter_adventure:
                world.multiworld.push_precollected(item)
            else:
                adventure_items.append(item)

    if world.selected_goal_level_adventure is not None:
        for board_item in sub_item_data:
            item: ZumaDeluxeItem = create_item_by_sub_name(world, board_item, world.selected_goal_level_adventure.value)
            if "Unlock" in board_item["name"]:
                adventure_items.append(item)


    return adventure_items


def find_and_create_item(world: ZumaDeluxe, name)-> ZumaDeluxeItem:

    for dat in item_data:
        name_dat = dat["name"]
        if name_dat != name:
            continue
        return create_item(world, dat)
    for dat in extra_items:
        name_dat = dat["name"]
        if name_dat != name:
            continue
        return create_item(world, dat)
    for dat in sub_item_data:
        name_dat = dat["name"]
        if name_dat in name:
            item_dat: ItemData = ItemData(
                name = name,
                classification=dat["classification"],
            )
            return create_item(world, item_dat)


    return create_item(world, extra_items[0])