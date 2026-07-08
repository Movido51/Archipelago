from dataclasses import dataclass
from itertools import chain

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionDict

from .gameControl.enums import (
    ZumaDeluxeBoards,
    ZumaDeluxeStages,
    ZumaDeluxeGauntletDifficulties


)
## game and goal setup

class GameMode(Choice):
    """
    Choose the game mode where you will be playing.
    Adventure: Enables Adventure mode.
    Gauntlet: Enables Gauntlet mode both Survival and Practice.
    Explorer: Play Both Modes.
    """
    display_name = "Game Mode"
    option_adventure = 0
    option_gauntlet = 1
    option_explorer = 2
    default = option_explorer


class Goal(Choice):
    """
    Choose the Level to complete for your Goal
    Space: Beat the level Space
    Random: picks a random lvl of the list
    """

    display_name = "Goal"
    option_space = 0
    option_random_level = 1
    #option_Sun = 2

    default = option_random_level

class GoalMode(Choice):
    """"
    When the exploration Mode is played, picks to what mode will be the goal level assigned.

    When picking option both:
    space Goal,  allows the player to goal by beating either version.
    random, will pick a random level for each mode,

    random One will select one of the modes to have the goal

    """
    display_name = "Goal Level Mode"
    option_adventure = 0
    option_gauntlet = 1
    option_both = 2
    option_random_one = -1
    default = option_random_one


class SunIdol(Range):
    """
    The amount of Sun Idols that will be Scattered around the multiworld.

    Will be cap depending on the amount of final checks.
    Max around adventure ~100~
    Max around gauntlet ~200~
    """
    display_name = "Sun Idols"
    range_start = 10
    range_end = 250
    default = 50

class SunIdolUnlock(Range):
    """
    The percentage of Sun Idols required to goal by beating the goal level.
    Will unlock space in adventure.
    Will let you play the goal difficulty for the level in gauntlet.

    Max will be one less than the amount of Sun Idols.
    """

    display_name = "Required Sun Idols"
    range_start = 0
    range_end = 99
    default = 50

class SunIdolHelpers(Range):
    """
    After you unlock the goal level, each extra SunIdol will make the level easier until the selected percentage.

    At this amount of Sun idols:
    Space will have the vanilla requirement in adventure.
    Gauntlet will goal at the first level of goal difficulty

    if smaller than the required Sun idols, will be set to one higher
    """
    display_name = "Useful Sun Idols"
    range_start = 1
    range_end = 100
    default = 75




## Section Setup

class AceTime(Toggle):
    """
    Add the Ace-Time of each level as locations.
    """
    display_name = "Ace Time"
class Coins(Range):
    """
    Choose the multiplier percentage to the amount of coins needed per Section (Board Difficulty or Stage) to send the location.

    The base amount is calculated on the amount of levels per Section, 7 in gauntlet, 5-7 in adventure.

    For reference decimals will go up.
    50% : 4 gauntlet 3-4 adventure
    150% : 11 gauntlet 8-11 adventure
    Minimum will be 1 coin.

    """
    display_name = "Coins per Section"
    range_start = 1
    range_end = 200
    default = 100

class Gaps(Range):
    """
    Amount of gaps shots for each Section.
    The base amount is calculated on the amount of levels per Section, 7 in gauntlet, 5-7 in adventure.

    For reference decimals will go up.
    50% : 4 gauntlet 3-4 adventure
    150% : 11 gauntlet 8-11 adventure
    Minimum will be 1 gap shot.
    """
    display_name = "Gaps per Section"
    range_start = 1
    range_end = 300
    default = 100

class Combo(Range):
    """
    Amount of combos shots for each Section. (groups destroyed after a shot)
    The base amount is calculated on the amount of levels per Section, 7 in gauntlet, 5-7 in adventure.

    For reference decimals will go up.
    50% : 4 gauntlet 3-4 adventure
    150% : 11 gauntlet 8-11 adventure
    Minimum will be 1 combos shot.
    """
    display_name = "Combos per Section"
    range_start = 1
    range_end = 500
    default = 200

class MaxCombo(Range):
    """
    The amount of Combos to made with one shot required to send the check.
    """
    display_name = "Max Combo requirement"
    range_start = 2
    range_end = 5
    default = 3

class Chain(Range):
    """
    The length of the chain to made required to send the check.
    """

    display_name = "Chain length"
    range_start = 5
    range_end = 10
    default = 6


### gauntlet options

class GauntletLevels(OptionDict):
    """
    Determines which Boards from Gauntlet can be considered for inclusion in the multiworld.

    Set any Level you don't want to possibly play to false.

    A minimum of 5 Levels must be selected to play.

    If space is selected as goal but not here, only clearing the goal will be the only check in space
    """
    display_name = " Gauntlet Level Selection"

    valid_keys = {level.value: True for level in list(ZumaDeluxeBoards)[:-1]}

    default = valid_keys

class GauntletLevelAmount(Range):
    """
    Determines how many levels will be picked from your selection from Gauntlet to include in the multiworld.
    """
    display_name = "Gauntlet Levels Amount"
    range_start = 5
    range_end = 22
    default = 12

class GauntletDifficulty(Choice):
    """
    Determines the Goal difficulty for the Gauntlet.
    Each lower difficulty will be location.
    """

    option_eagle = 1
    option_jaguar = 2
    option_sun_god = 3
    default = option_jaguar

## Adventure Options

class AdventureLevels(OptionDict):
    """
    Determines which stages from adventure can be considered for inclusion in the multiworld.

    Set any Level you don't want to possibly play to false.

    A minimum of 4 Levels must be selected to play.
    """
    display_name = "Adventure Level Selection"

    valid_keys = {level.value: True for level in list(ZumaDeluxeStages)[:-1]}

    default = valid_keys


class AdventureLevelAmount(Range):
    """
    Determines how many levels will be picked from your selection from Gauntlet to include in the multiworld.
    """
    display_name = "Adventure Levels Amount"
    range_start = 4
    range_end = 12
    default = 9

## Useful Items Options

class ClearScoreMultiplier(Range):
    """
    Multiplier percentage for scores needed to beat each level
    """
    display_name = "Clear Score Multiplier"
    range_start = 10
    range_end = 300
    default = 100


class MaximumStartingLives(Range):
    """
    Number of lives you will start after receiving all Progressive Lives.
    """
    display_name = "Maximum Starting Lives"
    range_start = 2
    range_end = 10
    default = 3

class DeathLink(Choice):
    """
    When you lose a live or get game over, the other player will also die.
    the opposite is also true.
    """
    display_name = "Death Link"
    option_off = 0
    option_toggle = 1
    option_on = 2
    default = 0


# dataclass

@dataclass
class ZumaDeluxeOptions(PerGameCommonOptions):

    game_mode: GameMode
    goal: Goal
    goal_mode: GoalMode
    sun_idol: SunIdol
    sun_idol_unlock: SunIdolUnlock
    sun_idol_helpers: SunIdolHelpers
    ace_time: AceTime
    coins: Coins
    gaps: Gaps
    combo: Combo
    max_combo: MaxCombo
    chain: Chain
    gauntlet_levels: GauntletLevels
    gauntlet_amount: GauntletLevelAmount
    gauntlet_difficulty: GauntletDifficulty
    adventure_levels: AdventureLevels
    adventure_amount: AdventureLevelAmount
    maximum_starting_lives: MaximumStartingLives
    clear_score_multiplier: ClearScoreMultiplier
    death_link: DeathLink


option_groups = [
    OptionGroup(
        "Goal Options",
        [
            GameMode,
            Goal,
            GoalMode,
            SunIdol,
            SunIdolUnlock,
            SunIdolHelpers,
            DeathLink
        ]
    ),
    OptionGroup(
        "Level Options",
        [
            AceTime,
            Coins,
            Gaps,
            Combo,
            MaxCombo,
            Chain,
        ]
    ),
    OptionGroup(
        "Gauntlet Options",
        [
            GauntletLevels,
            GauntletLevelAmount,
            GauntletDifficulty,
        ]
    ),
    OptionGroup(
        "Adventure Options",
        [
            AdventureLevels,
            AdventureLevelAmount,

        ]
    ),
    OptionGroup(
        "Useful Options",
        [
            ClearScoreMultiplier,
            MaximumStartingLives,
        ]
    )
]
