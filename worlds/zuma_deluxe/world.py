from collections.abc import Mapping
from typing import Any, Dict, List, Optional
import logging


from worlds.AutoWorld import World
from . import items, regions, rules, web_world, items_data, locations_data, generator
from . import options as zuma_deluxe_options

from .gameControl.enums import (
    ZumaDeluxeAPGoals,
    ZumaDeluxeMode,
    ZumaDeluxeStages,
    ZumaDeluxeBoards,
    ZumaDeluxeGauntletDifficulties

)

class ZumaDeluxe(World):
    """
    Deep in the jungle lie hidden temples bursting with traps and trickery, and it's up to you to uncover their treasures. 
    Fire magical balls from your stone frog idol to make matches of three or more and clear the deadly chain before it reaches
      the golden skull.
    """

    game = "Zuma Deluxe"

    web = web_world.ZumaDeluxeWebWorld()

    options_dataclass = zuma_deluxe_options.ZumaDeluxeOptions
    options: zuma_deluxe_options.ZumaDeluxeOptions

    item_name_to_id = items_data.items_names_to_ids
    location_name_to_id = locations_data.locations_names_to_ids

    item_name_groups = items_data.item_name_groups
    location_name_groups = locations_data.location_name_groups





    ### Options

    goal_mode_option: int
    sun_idols_required_option: int
    sun_idols_helpers_option: int



    #translate

    goal: ZumaDeluxeAPGoals
    goal_mode: ZumaDeluxeMode
    mode: ZumaDeluxeMode
    sun_idols_required: int
    sun_idols_helpers: int
    sun_idols_total: int

    include_ace_time: bool
    coins: int
    gaps: int
    combo: int
    max_combo: int
    chain: int

    target_ratios: int




    gauntlet_selection: Optional[Dict[ZumaDeluxeBoards, bool]]
    gauntlet_amount: int
    selected_gauntlet_difficulty: Optional[ZumaDeluxeGauntletDifficulties]

    adventure_selection: Optional[Dict[ZumaDeluxeStages, bool]]
    adventure_amount: int
    maximum_lives: int


    # # Generation

    selected_adventure_levels: List[ZumaDeluxeStages] = None
    selected_starter_adventure: Optional[ZumaDeluxeStages]
    selected_goal_level_adventure: Optional[ZumaDeluxeStages]

    selected_gauntlet_levels: List[ZumaDeluxeBoards] = None
    selected_starter_gauntlet: Optional[ZumaDeluxeBoards]

    selected_goal_level_gauntlet: Optional[ZumaDeluxeBoards]

    ut_can_gen_without_yaml: bool = True

    # Universal Tracker

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    ##early gen

    def generate_early(self) -> None:
        self.goal = ZumaDeluxeAPGoals(self.options.goal.value)
        self.mode = ZumaDeluxeMode(self.options.game_mode.value)
        if self.mode == ZumaDeluxeMode.BOTH:
            self.goal_mode_option = self.options.goal_mode.value
            if self.goal_mode_option == -1:
                self.goal_mode_option = self.random.randint(0,1)
        else:
            self.goal_mode_option =self.options.game_mode.value

        self.goal_mode = ZumaDeluxeMode(self.goal_mode_option)

        self.sun_idols_total = self.options.sun_idol.value

        self.sun_idols_required_option = self.options.sun_idol_unlock.value
        self.sun_idols_helpers_option = self.options.sun_idol_helpers.value
        self.sun_idols_required = (self.sun_idols_total * self.sun_idols_required_option) // 100
        self.sun_idols_helpers = (self.sun_idols_total * self.sun_idols_helpers_option) // 100
        if self.sun_idols_required_option >= self.sun_idols_helpers_option:
            self.sun_idols_helpers = self.sun_idols_required+1
            logging.warning(
                f"Zuma Deluxe: {self.player_name} has more required sun idols than total sun idols. "
                "Adjusting required sun idols to match total sun idols..."
            )

        self.include_ace_time = bool(self.options.ace_time.value)
        self.coins =self.options.coins.value
        self.gaps = self.options.gaps.value
        self.combo = self.options.combo.value
        self.max_combo = self.options.max_combo.value
        self.chain = self.options.chain.value
        self.maximum_lives = self.options.maximum_starting_lives.value
        self.target_ratios = self.options.clear_score_multiplier.value

        ## levels selection gauntlet
        if self.mode != ZumaDeluxeMode.ADVENTURE:
            self.gauntlet_amount = self.options.gauntlet_amount.value
            self.selected_gauntlet_difficulty = list(ZumaDeluxeGauntletDifficulties)[self.options.gauntlet_difficulty.value]
            generator.pre_generate_gauntlet_levels(self)

        else:
            self.gauntlet_amount = 0
            self.selected_starter_gauntlet = None
            self.selected_gauntlet_difficulty = None
            self.selected_goal_level_gauntlet = None
            self.selected_starter_gauntlet = None


        ## levels selection adventure
        if self.mode != ZumaDeluxeMode.GAUNTLET:
            self.adventure_amount = self.options.adventure_amount.value
            generator.pre_generate_adventure_levels(self)
        else:
            self.adventure_amount = 0
            self.selected_starter_adventure = None
            self.selected_goal_level_adventure = None




        adventure_selection: Dict[ZumaDeluxeStages, bool]
        adventure_amount: int

        if self.is_universal_tracker:
            self._apply_universal_tracker_passthrough()

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)


    def create_items(self) -> None:
        items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def create_item(self, name: str) -> items.ZumaDeluxeItem:

        return items.find_and_create_item(self, name)

    def set_rules(self) -> None:
        rules.set_completion_condition(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        slot_data: Dict[str,Any]  = self.options.as_dict(
            "game_mode",
            "goal",
            "goal_mode",
            "sun_idol",
            "sun_idol_unlock",
            "sun_idol_helpers",
            "ace_time",
            "coins",
            "gaps",
            "combo",
            "max_combo",
            "chain",
            "gauntlet_levels",
            "gauntlet_amount",
            "gauntlet_difficulty",
            "adventure_levels",
            "adventure_amount",
            "maximum_starting_lives",
            "clear_score_multiplier",
            "death_link",
        )
        #generated

        slot_data["sun_idols_required_amount"] = self.sun_idols_required
        slot_data["sun_idols_helpers_amount"] = self.sun_idols_helpers

        if self.mode != ZumaDeluxeMode.ADVENTURE:
            slot_data["gauntlet_selected_levels"] = [board.value for board in self.selected_gauntlet_levels]
        if self.selected_starter_gauntlet is not None:
            slot_data["gauntlet_stater_level"] = self.selected_starter_gauntlet.value
        if self.selected_goal_level_gauntlet is not None:
            slot_data["gauntlet_goal"] = self.selected_goal_level_gauntlet.value


        if self.mode != ZumaDeluxeMode.GAUNTLET:
            slot_data["adventure_selected_levels"] = [stage.value for stage in self.selected_adventure_levels]
        if self.selected_starter_adventure is not None:
            slot_data["adventure_stater_level"] = self.selected_starter_adventure.value
        if self.selected_goal_level_adventure is not None:
            slot_data["adventure_goal"] = self.selected_goal_level_adventure.value



        #corrected
        if slot_data["goal_mode"] != self.goal_mode_option:
            slot_data["goal_mode"] = self.goal_mode_option

        if slot_data["gauntlet_amount"] != self.gauntlet_amount:
            slot_data["gauntlet_amount"] = self.gauntlet_amount
        if slot_data["adventure_amount"] != self.adventure_amount:
            slot_data["adventure_amount"] = self.adventure_amount



        return slot_data

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Zuma Deluxe" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Zuma Deluxe"]

            self.mode = ZumaDeluxeMode(passthrough["game_mode"])
            self.goal_mode_option = passthrough["goal_mode"]
            self.goal_mode = ZumaDeluxeMode(self.goal_mode_option)

            self.sun_idols_total = passthrough["sun_idol"]
            self.sun_idols_required_option = passthrough["sun_idol_unlock"]
            self.sun_idols_helpers_option = passthrough["sun_idol_helpers"]
            self.sun_idols_required = (self.sun_idols_total * self.sun_idols_required_option) // 100
            self.sun_idols_helpers = (self.sun_idols_total * self.sun_idols_helpers_option) // 100

            self.include_ace_time = passthrough["ace_time"]
            self.coins = passthrough["coins"]
            self.gaps = passthrough["gaps"]
            self.combo = passthrough["combo"]
            self.max_combo = passthrough["max_combo"]
            self.chain = passthrough["chain"]
            self.maximum_lives = passthrough["maximum_starting_lives"]
            self.target_ratios = passthrough["clear_score_multiplier"]



            # set de niveles Gauntlet

            self.gauntlet_amount = passthrough["gauntlet_amount"]
            self.selected_gauntlet_difficulty = list(ZumaDeluxeGauntletDifficulties)[passthrough["gauntlet_difficulty"]]
            try:
                self.selected_starter_gauntlet = ZumaDeluxeBoards(passthrough["gauntlet_stater_level"])
            except Exception:
                pass
            try:
                self.selected_goal_level_gauntlet = ZumaDeluxeBoards(passthrough["gauntlet_goal"])
            except Exception:
                pass

            self.selected_gauntlet_levels = [ ZumaDeluxeBoards(board) for board in passthrough["gauntlet_selected_levels"]]


            # adventure

            self.adventure_amount = passthrough["adventure_amount"]
            try:
                self.selected_starter_adventure = ZumaDeluxeStages(passthrough["adventure_stater_level"])
            except Exception:
                pass
            try:
                self.selected_goal_level_adventure = ZumaDeluxeStages(passthrough["adventure_goal"])
            except Exception:
                pass

            self.selected_adventure_levels = [ ZumaDeluxeStages(stage) for stage in passthrough["adventure_selected_levels"]]

