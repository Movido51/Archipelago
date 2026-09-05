from __future__ import annotations
import logging
from Options import OptionError
from typing import List, TYPE_CHECKING
from .gameControl.enums import (
    ZumaDeluxeBoards,
    ZumaDeluxeAPGoals,
    ZumaDeluxeMode,
    ZumaDeluxeStages
)

if TYPE_CHECKING:
    from .world import ZumaDeluxe

def pre_generate_gauntlet_levels(world: ZumaDeluxe) -> None:
    board_pool : List[ZumaDeluxeBoards] = list()
    minimum_boards: int = world.options.gauntlet_amount.range_start
    board_weights = world.options.gauntlet_levels.value
    population = list(board_weights.keys())
    weights = list(board_weights.values())
    k = min(world.gauntlet_amount, len([w for w in weights if w > 0]))
    for _ in range(k):
        choice = world.multiworld.random.choices(population=population, weights=weights, k=1)[0]
        idx = population.index(choice)
        board_pool.append(ZumaDeluxeBoards(choice))
        population.pop(idx)
        weights.pop(idx)
    board_pool = list(sorted(board_pool, key=lambda m: m.value))

    if len(board_pool) < minimum_boards:
        raise OptionError(
            f"Zuma Deluxe: {world.player_name} must have at least {minimum_boards} levels selected to play. "
            f"They only have {len(board_pool)} selected."
        )
    if world.gauntlet_amount > len(board_pool):
        world.gauntlet_amount = len(board_pool)
        logging.warning(
            f"Zuma Deluxe: {world.player_name} has a level count higher than their selected level pool for gauntlet. "
            "Adjusting level count to match the size of their level pool..."
        )
    world.random.shuffle(board_pool)

    board_pool = board_pool[:world.gauntlet_amount]

    if world.goal_mode != ZumaDeluxeMode.ADVENTURE:
        if world.goal == ZumaDeluxeAPGoals.SPACE:
            world.selected_goal_level_gauntlet = ZumaDeluxeBoards.Spc_22
            if ZumaDeluxeBoards.Spc_22 not in board_pool:
                board_pool = board_pool[:-1 ]
                board_pool.append(ZumaDeluxeBoards.Spc_22)
            else:
                board_pool.remove(ZumaDeluxeBoards.Spc_22)
                board_pool.append(ZumaDeluxeBoards.Spc_22)
        else:
            world.selected_goal_level_gauntlet = board_pool[-1]
            #board_pool = board_pool[:-1 ]
    else:
        world.selected_goal_level_gauntlet = None
    world.selected_gauntlet_levels = board_pool[:]
    if world.mode == ZumaDeluxeMode.BOTH:
        if world.goal_mode != ZumaDeluxeMode.GAUNTLET:
            world.selected_starter_gauntlet = board_pool[0]
        else:
            world.selected_starter_gauntlet = None
    else:
        world.selected_starter_gauntlet = board_pool[0]
    print(board_pool)

def pre_generate_adventure_levels(world: ZumaDeluxe) -> None:
    stage_pool: List[ZumaDeluxeStages] = list()
    minimum_stages: int = world.options.gauntlet_amount.range_start
    stage_weights = world.options.adventure_levels.value
    population = list(stage_weights.keys())
    weights = list(stage_weights.values())
    k = min(world.adventure_amount, len([w for w in weights if w > 0]))
    for _ in range(k):
        choice = world.multiworld.random.choices(population=population, weights=weights, k=1)[0]
        idx = population.index(choice)
        stage_pool.append(ZumaDeluxeStages(choice))
        population.pop(idx)
        weights.pop(idx)

    stage_pool = list(sorted(stage_pool, key=lambda m: m.value))

    if len(stage_pool) < minimum_stages:
        raise OptionError(
            f"Zuma Deluxe: {world.player_name} must have at least {minimum_stages} levels selected to play. "
            f"They only have {len(stage_pool)} selected."
        )
    if world.adventure_amount > len(stage_pool):
        world.adventure_amount = len(stage_pool)
        logging.warning(
            f"Zuma Deluxe: {world.player_name} has a level count higher than their selected level pool for adventure. "
            "Adjusting level count to match the size of their level pool..."
        )
    world.random.shuffle(stage_pool)

    stage_pool = stage_pool[:world.adventure_amount]

    if world.goal_mode != ZumaDeluxeMode.GAUNTLET:
        if world.goal == ZumaDeluxeAPGoals.SPACE:
            world.selected_goal_level_adventure = ZumaDeluxeStages.SSoZ_13
        else:
            world.selected_goal_level_adventure = stage_pool[-1]
            stage_pool = stage_pool[:-1]
    else:
        world.selected_goal_level_adventure = None
    world.selected_adventure_levels = stage_pool[:]
    if world.mode == ZumaDeluxeMode.BOTH:
        if world.goal_mode != ZumaDeluxeMode.ADVENTURE:
            world.selected_starter_adventure = stage_pool[0]
        else:
            world.selected_starter_adventure = None
    else:
        world.selected_starter_adventure = stage_pool[0]
