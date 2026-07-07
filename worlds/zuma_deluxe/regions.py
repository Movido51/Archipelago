from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional


from BaseClasses import Region, ItemClassification
from rule_builder.rules import *
from .locations_data import sub_region_locations_data,sub_level_locations_data
from .locations import ZumaDeluxeLocation
from .items import ZumaDeluxeItem

from .gameControl.enums import (
    ZumaDeluxeGauntletDifficulties,
    ZumaDeluxeBoards,
ZumaDeluxeStages,
ZumaDeluxeMode
)

if TYPE_CHECKING:
    from .world import ZumaDeluxe

def create_and_connect_regions(world: ZumaDeluxe) -> None:
    create_all_regions(world)




def create_all_regions(world: ZumaDeluxe) -> None:
    regions: List[Region] =[]
    player = world.player
    multiworld = world.multiworld
    ## start and end
    region_menu: Region = Region("Menu", world.player, world.multiworld)

    regions.append(region_menu)

    region_endgame: Region = Region("Endgame", world.player, world.multiworld)
    regions.append(region_endgame)
    victory_location: ZumaDeluxeLocation = ZumaDeluxeLocation(
        world.player,
        "Victory location",
        None,
        region_endgame,
    )

    victory_location.place_locked_item(
        ZumaDeluxeItem(
            "Victory",
            ItemClassification.progression,
            None,
            world.player,
        )
    )

    region_endgame.locations.append(victory_location)

    rule_to_end: Optional[Rule] = None
    #gauntlet
    if world.selected_goal_level_gauntlet is not None:
        rule_to_end = Has(f"Board Unlock: {world.selected_goal_level_gauntlet.value.split('- ', 1)[1]}")
    if world.selected_goal_level_adventure is not None:
        if rule_to_end is not None:
            rule_to_end = Or(rule_to_end,Has(f"Stage Unlock: {world.selected_goal_level_adventure.value.split('- ', 1)[1]}"))
        else:
            rule_to_end = Has(f"Stage Unlock: {world.selected_goal_level_adventure.value.split('- ', 1)[1]}")


    if rule_to_end is not None:
        rule_to_end = And(rule_to_end,Has("Sun Idol",world.sun_idols_required))
    else:
        rule_to_end = Has("Sun Idol", world.sun_idols_required)

    region_menu.connect(
        region_endgame,
        rule = rule_to_end,
    )

    #Gauntlet
    if world.mode != ZumaDeluxeMode.ADVENTURE:
        regions.extend(regions_for_boards(world, region_menu))
    #Adventure
    if world.mode != ZumaDeluxeMode.GAUNTLET:
        regions.extend(regions_for_stages(world, region_menu))

    world.multiworld.regions += regions

def regions_for_boards(world: ZumaDeluxe, region_menu: Region)->List[Region]:
    board_regions: List[Region] = []
    for board in world.selected_gauntlet_levels:

        if board is None:
            continue
        board_region: Region = Region(
            board.value,
            world.player,
            world.multiworld,
        )
        board_name: str = board.value.split("- ", 1)[1]
        progressive_amount: int = 0
        for board_difficulty in ZumaDeluxeGauntletDifficulties:

            board_dif_name: str = board_name +" - "+ board_difficulty.value
            board_dif_region: Region = Region(
                board_dif_name,
                world.player,
                world.multiworld,
            )
            if world.selected_gauntlet_difficulty == board_difficulty:
                break
            for board_location_data in sub_region_locations_data:
                board_location_name:str = board_dif_name + " ("+board_location_data+")"
                location: ZumaDeluxeLocation = ZumaDeluxeLocation(
                    world.player,
                    board_location_name,
                    world.location_name_to_id[board_location_name],
                    board_dif_region,
                )
                board_dif_region.locations.append(location)
            for i in range(1, 8):
                for level_location_data in sub_level_locations_data:
                    if  not world.include_ace_time and level_location_data == "Ace Time":
                        continue
                    level_location_name:str = board_dif_name +f"{i}"+ " ("+level_location_data+")"
                    location: ZumaDeluxeLocation = ZumaDeluxeLocation(
                        world.player,
                        level_location_name,
                        world.location_name_to_id[level_location_name],
                        board_dif_region,
                    )
                    if level_location_data == "Ace Time":
                        rule = HasAny(
                            board_name+" (Coins)",
                            board_name + " (Combos)",
                            board_name + " (Chains)",
                        )
                        world.set_rule(location,rule)
                    board_dif_region.locations.append(location)

            if progressive_amount >0:
                board_region.connect(
                    board_dif_region,
                    rule = Has("Progressive Difficulty",count = progressive_amount)
                )
            else:
                board_region.connect(board_dif_region)
            board_dif_region.connect(board_region)
            board_regions.append(board_dif_region)

            progressive_amount= progressive_amount + 1


        region_menu.connect(
            board_region,
            rule = Has(f"Board Unlock: {board_name}")
        )
        board_region.connect(region_menu)
        board_regions.append(board_region)


    #goal Gauntlet
    if world.selected_goal_level_gauntlet is not None:
        goal_board: ZumaDeluxeBoards = world.selected_goal_level_gauntlet
        connect_to_region: Region = region_menu
        goal_rule: Rule | None = None
        board_name: str = goal_board.value.split("- ", 1)[1]
        if goal_board in world.selected_gauntlet_levels:
            for board_region_search in board_regions:
                if board_region_search.name == goal_board.value:
                    connect_to_region = board_region_search
        else:
            goal_rule = Has(f"Board Unlock: {board_name}")

        board_dif: str = board_name + " - "+world.selected_gauntlet_difficulty.value
        goal_region: Region = Region(
            board_dif,
            world.player,
            world.multiworld,
        )
        goal_loc_name: str = board_dif + " (Goal)"
        goal_location: ZumaDeluxeLocation = ZumaDeluxeLocation(
            world.player,
            goal_loc_name,
            world.location_name_to_id[goal_loc_name],
            goal_region,
        )

        goal_region.locations.append(goal_location)

        amount = world.options.gauntlet_difficulty.value

        if goal_rule is not None:

            connect_to_region.connect(
                goal_region,
                rule = And(goal_rule,Has("Sun Idol", world.sun_idols_required), Has("Progressive Difficulty",amount))
            )
        else:
            connect_to_region.connect(
                goal_region,
                rule = And(Has("Sun Idol", world.sun_idols_required),Has("Progressive Difficulty",amount))
            )
        goal_region.connect(goal_region)
        world.options.exclude_locations.value.add(goal_loc_name)
        board_regions.append(goal_region)


    return board_regions

def regions_for_stages(world: ZumaDeluxe, region_menu: Region)->List[Region]:
    stage_regions: List[Region] = []
    board_list: List[ZumaDeluxeBoards] = list(ZumaDeluxeBoards)
    for stage in world.selected_adventure_levels:

        if stage is None:
            continue
        stage_region: Region = Region(
            stage.value,
            world.player,
            world.multiworld,
        )
        stage_number: int = int(stage.value.split()[1])-1
        stage_name: str = stage.value.split("- ", 1)[1]

        for stage_location_data in sub_region_locations_data:
            stage_location_name:str = stage_name + " ("+stage_location_data+")"
            location: ZumaDeluxeLocation = ZumaDeluxeLocation(
                world.player,
                stage_location_name,
                world.location_name_to_id[stage_location_name],
                stage_region,
            )
            stage_region.locations.append(location)

        amount_of_levels: int = min(5 + (stage_number//3),7)
        starting_board: int = (stage_number % 3)*7
        for i in range(amount_of_levels):
            stage_board: str = stage_name + " - " + board_list[starting_board+i].value.split("- ", 1)[1]

            for level_location_data in sub_level_locations_data:
                if  not world.include_ace_time and level_location_data == "Ace Time":
                    continue
                level_location_name:str = stage_board + " ("+level_location_data+")"
                location: ZumaDeluxeLocation = ZumaDeluxeLocation(
                    world.player,
                    level_location_name,
                    world.location_name_to_id[level_location_name],
                    stage_region,
                )
                if level_location_data == "Ace Time":
                    rule = HasAny(
                        stage_name+" (Coins)",
                        stage_name + " (Combos)",
                        stage_name + " (Chains)",
                    )
                    world.set_rule(location,rule)
                stage_region.locations.append(location)

        region_menu.connect(
            stage_region,
            rule = Has(f"Stage Unlock: {stage_name}")
        )
        stage_region.connect(region_menu)
        stage_regions.append(stage_region)


    #goal adventure
    if world.selected_goal_level_adventure is not None:
        goal_stage: ZumaDeluxeStages = world.selected_goal_level_adventure
        connect_to_region: Region
        if goal_stage in world.selected_adventure_levels:
            connect_to_region = world.get_region(goal_stage.value)
        else:
            connect_to_region = region_menu
        stage_name: str = goal_stage.value.split("- ", 1)[1]
        goal_region: Region = Region(
            stage_name,
            world.player,
            world.multiworld,
        )
        goal_loc_name: str = stage_name + " (Goal)"
        goal_location: ZumaDeluxeLocation = ZumaDeluxeLocation(
            world.player,
            goal_loc_name,
            world.location_name_to_id[goal_loc_name],
            goal_region,
        )
        goal_region.locations.append(goal_location)
        connect_to_region.connect(
            goal_region,
            rule = And(
                Has("Sun Idol", world.sun_idols_required),
                Has(f"Stage Unlock: {stage_name}")
            )
        )
        goal_region.connect(goal_region)
        world.options.exclude_locations.value.add(goal_loc_name)
        stage_regions.append(goal_region)
    return stage_regions


