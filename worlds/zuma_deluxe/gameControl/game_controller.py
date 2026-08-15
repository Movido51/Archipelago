from typing import Dict, List, Optional, Set, Tuple, Union

import collections
import logging

import enum

import math

from worlds.cv64 import filler_item_names
from .enums import (
    ZumaDeluxeGameState,
    ZumaDeluxeInLevel,
    ZumaDeluxeAPGoals,
    ZumaDeluxeBoards,
    ZumaDeluxeStages,
    ZumaDeluxeGauntletDifficulties,
    ZumaDeluxeMode
)

from ..items_data import extra_items, Group

from .game_state_manager import GameStateManager, GameState

from ..locations_data import levels_base_speed_adventure

class SectionState(enum.Enum):
    NoneSelected = -1
    Blocked = 0
    Unlocked = 1
    GoalLocked = -10
    GoalUnlocked = 10
    GoalIncomplete =-20

class GameController:
    logger: Optional[logging.Logger]

    received_items: Dict[str,int]
    completed_locations: Set[str]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    #options Lecture




    #Game direction state
    game_state_in_level: Optional[ZumaDeluxeInLevel]
    game_state_current_game_state: Optional[ZumaDeluxeGameState]
    game_state_current_level: Optional[int]
    game_state_last_level: Optional[int]
    game_state_current_gauntlet_level: Optional[int]
    game_state_gauntlet_board: Optional[int]
    game_state_got_ace_time: bool

    game_score: int = 0
    game_balls: int = 0
    game_coins: int = 0
    game_gaps: int = 0

    game_total_combo:int = 0
    game_chains: int = 0
    last_death_message: str = ""

    game_missing_score: int = 0
    game_last_score:int = 0
    game_base_score:int = 0
    game_last_balls: int = 0
    game_last_coins: int = 0
    game_last_gaps: int = 0
    game_last_actual_combo:int = 0
    game_last_total_combo:int = 0
    game_last_chains:int = 0

    game_area_coins:int = 0
    game_area_total_combo:int = 0
    game_area_chains:int = 0
    game_area_gaps:int = 0
    game_area_max_combo = 0



    last_game_state_gauntlet_board: int = 0
    game_difficulty: ZumaDeluxeGauntletDifficulties

    #Game Front data

    game_state_current_game_mode: Optional[ZumaDeluxeMode]

    game_actual_section: None | ZumaDeluxeBoards | ZumaDeluxeStages
    game_last_section: None | ZumaDeluxeBoards | ZumaDeluxeStages
    game_action_list: collections.deque
    moved_up: bool


    game_actual_level: str = ""
    game_actual_area: str = ""
    game_actual_sub_level: str = ""
    game_up_level: str = ""
    game_up_area: str = ""

    #Generation options


    goal: Optional[ZumaDeluxeAPGoals]
    goal_mode: Optional[ZumaDeluxeMode]
    mode: Optional[ZumaDeluxeMode]
    sun_idols_required: Optional[int]
    max_combo: Optional[int]
    chain: Optional[int]
    sun_idols_helpers: Optional[int]
    sun_idols_total: Optional[int]

    include_ace_time: Optional[bool]
    coins: Optional[int]
    gaps: Optional[int]
    combo: Optional[int]

    target_ratios: Optional[int]

    maximum_lives: Optional[int]

    deathlink_option = Optional[int]
    deathlink: bool

    level_speed: float

    check_goal_level_clear: int

    # # Generation Data

    selected_adventure_levels: Optional[List[ZumaDeluxeStages]]
    selected_starter_adventure: Optional[ZumaDeluxeStages]
    selected_goal_level_adventure: Optional[ZumaDeluxeStages]

    selected_gauntlet_levels: Optional[List[ZumaDeluxeBoards]]
    selected_starter_gauntlet: Optional[ZumaDeluxeBoards]
    selected_goal_level_gauntlet: Optional[ZumaDeluxeBoards]
    selected_gauntlet_difficulty: Optional[int]

    adventure_selection: Optional[Dict[ZumaDeluxeStages, List[SectionState]]]
    gauntlet_selection: Optional[Dict[ZumaDeluxeBoards, List[SectionState]]]

    #items check

    filler_items_times: Dict[str,float]
    checked_clear: bool
    death_has_come:bool
    send_death:bool
    last_live: int
    lost_a_live: bool


    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()
        self.game_state_manager = GameStateManager()
        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state_in_level = None
        self.game_state_current_game_state= None
        self.game_state_current_level= None
        self.game_state_current_gauntlet_level= None
        self.game_state_gauntlet_board= None
        self.game_state_got_ace_time = False

        self.last_game_state_gauntlet_board = 0
        self.game_difficulty: ZumaDeluxeGauntletDifficulties =ZumaDeluxeGauntletDifficulties.RABBIT
        self.game_last_difficulty:ZumaDeluxeGauntletDifficulties = self.game_difficulty

        # Game Front data

        self.game_state_current_game_mode = None
        self.game_actual_section = None
        self.game_last_section = None
        self.game_action_list = collections.deque()
        self.moved_up = False
        self.game_state_last_level = 0
        self.level_speed = 0.0

        #Generation Options
        self.goal = None
        self.goal_mode  = None
        self.mode  = None
        self.sun_idols_required  = None
        self.sun_idols_helpers  = None
        self.sun_idols_total  = None

        self.include_ace_time  = None
        self.coins  = None
        self.gaps  = None
        self.combo  = None
        self.max_combo  = None
        self.chain = None

        self.target_ratios = None

        self.gauntlet_selection = None
        self.gauntlet_amount = None
        self.selected_gauntlet_difficulty = None

        self.adventure_selection = None
        self.adventure_amount = None
        self.maximum_lives = None
        self.deathlink_option = None
        self.deathlink = False
        self.checked_clear = False
        self.check_goal_level_clear = 0

        # # Generation Data

        self.selected_adventure_levels = None
        self.selected_starter_adventure = None
        self.selected_goal_level_adventure = None

        self.selected_gauntlet_levels = None
        self.selected_starter_gauntlet = None

        self.selected_goal_level_gauntlet = None

        self.filler_items_times = {}

        self.death_has_come = False
        self.send_death = False
        self.last_live = -1
        self.lost_a_live = False


    def log(self, message)->None:
        if self.logger:
            self.logger.info(message)

    def log_debug(self, message)->None:
        if self.logger:
            self.logger.debug(message)

    def open_process_handle(self)->bool:
        return self.game_state_manager.open_process_handle()

    def close_process_handle(self)->bool:
        return self.game_state_manager.close_process_handle()

    def is_process_running(self)->bool:
        return self.game_state_manager.is_process_still_running()

    def update(self, dt:float):
        if self.game_state_manager.is_process_still_running():
            try:

                self._refresh_game_state()
                self._apply_conditional_game_state()
                self.back_setup()
                self.death_linker(dt)
                self.score_control()
                self.check_for_completed_locations()
                self.process_received_items()
                self.process_useful_and_traps(dt)
                self.harder_goal()
                self._check_for_victory()

                #

                #
                # self._check_for_completed_locations()
                # self._process_received_items()
                #
                # self._check_for_victory()w
            except Exception:
                import traceback

                with open("zuma_deluxe_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def _refresh_game_state(self)->None:
        game_state: GameState = self.game_state_manager.get_game_state()

        self.game_state_in_level = game_state.playing

        self.game_state_current_game_state  = game_state.game_state_in_game

        if game_state.current_level is not None and self.game_state_current_game_state == ZumaDeluxeGameState.PLAYING:
            self.game_state_current_level = game_state.current_level

        if game_state.gauntlet_level is not None:
            self.game_state_current_gauntlet_level = game_state.gauntlet_level
        self.game_state_gauntlet_board =game_state.gauntlet_board

        self.game_base_score = game_state.base_score
        self.game_score = game_state.actual_score
        if self.game_last_score < game_state.base_score:
            self.game_last_score = game_state.base_score
        self.game_balls = game_state.destroyed_balls
        self.game_coins = game_state.coins
        self.game_gaps = game_state.gaps
        self.game_total_combo = game_state.combos_total
        self.game_chains = game_state.chains
        self.level_speed = game_state.level_speed

        self.game_state_got_ace_time = game_state.ace_time_bool

        self.moved_up = False
        self.check_goal_level_clear = -1

        if game_state.actual_live == -1:
            self.last_live = game_state.actual_live
        if self.last_live > game_state.actual_live:
            self.lost_a_live = True
        else:
            self.lost_a_live = False
        self.last_live = game_state.actual_live

    def _apply_conditional_game_state(self)->None:
        if not self.game_state_manager.are_all_temples_unlocked():
            self.game_state_manager.unlock_all_temples()



    def back_setup(self)->None:

        if self.game_state_in_level == ZumaDeluxeInLevel.LEVEL:
            if self.game_state_current_game_mode is None:
                return


            if self.game_state_current_gauntlet_level != 0:
                self.game_state_current_game_mode = ZumaDeluxeMode.GAUNTLET
            if self.game_state_current_game_mode == ZumaDeluxeMode.ADVENTURE:

                if self.game_state_current_game_state != ZumaDeluxeGameState.PLAYING and ZumaDeluxeGameState.DANGER != self.game_state_current_game_state:
                    self.reset_level()
                    return
                self.checked_clear = False


                base_level = self.game_state_current_level
                if base_level is None:
                    base_level = 0

                stage_number:int
                level_number: int
                board_number: int
                if base_level < 15:
                    stage_number = base_level // 5
                    level_number = (base_level % 5) + 1

                elif base_level < 33:
                    stage_number = ((base_level - 15) // 6) + 3
                    level_number = ((base_level - 15) % 6) + 1
                else:

                    stage_number = ((base_level - 33) // 7) + 6
                    level_number = ((base_level - 33) % 7) + 1

                board_number = (stage_number%3) * 7 + level_number - 1

                self.game_actual_section = list(ZumaDeluxeStages)[stage_number]

                self.game_actual_level = " Lvl "+ (stage_number+1).__str__() +"-"+level_number.__str__() + " " + list(ZumaDeluxeBoards)[board_number].value.split("- ")[1]
                self.game_actual_area = self.game_actual_section.value.split("- ")[1]
                self.game_actual_sub_level = self.game_actual_area + " - " +list(ZumaDeluxeBoards)[board_number].value.split("- ")[1]
                self.game_state_last_level = self.game_state_current_level
            else:

                self.game_actual_section = list(ZumaDeluxeBoards)[self.last_game_state_gauntlet_board]


                lev = self.game_state_current_level
                if lev is None:
                    lev = 0

                gaunt_lev = self.game_state_current_gauntlet_level

                lev_int_difficulty = lev//7
                lev_dif_dif = 0
                if self.selected_gauntlet_difficulty is not None and self.selected_gauntlet_difficulty < lev_int_difficulty:
                    lev_dif_dif = 7 * (lev_int_difficulty - self.selected_gauntlet_difficulty)
                    lev_int_difficulty = self.selected_gauntlet_difficulty

                self.game_difficulty = list(ZumaDeluxeGauntletDifficulties)[lev_int_difficulty]

                lev_str = ((lev %7)+1).__str__()



                if lev != self.game_state_last_level:
                    if self.game_state_last_level is None:
                        self.game_state_last_level = lev
                    print(f"{lev} {self.game_state_last_level}")
                    if lev - self.game_state_last_level <=2:
                        self.moved_up = True
                    self.checked_clear = False
                    #self.reset_level()
                    self.game_up_area = self.game_actual_area
                    self.game_up_level = self.game_actual_sub_level
                    self.game_state_last_level = self.game_state_current_level
                    self.game_last_score = self.game_score
                    self.ready_level = False
                    self.speed_multiplier = 1
                    self.death_has_come = False
                    ### gauntlet changing level


                if self.game_last_difficulty != self.game_difficulty:
                    self.reset_area()
                self.game_actual_level = " " + self.game_difficulty.value + " - " + lev_str
                self.game_actual_area = self.game_actual_section.value.split("- ")[1] + " - " + self.game_difficulty.value
                self.game_actual_sub_level = self.game_actual_area + lev_str



            if self.game_state_current_game_state == ZumaDeluxeGameState.PLAYING:
                if self.game_actual_section != self.game_last_section:
                    self.reset_area()



        else:

            if self.game_state_gauntlet_board is None:
                self.game_state_current_game_mode = ZumaDeluxeMode.ADVENTURE
                self.game_actual_section = None
            else:
                self.game_state_current_game_mode = ZumaDeluxeMode.GAUNTLET
                if self.game_state_gauntlet_board is not None:
                    self.last_game_state_gauntlet_board = (self.game_state_gauntlet_board-1) % 23

                    self.game_actual_section = list(ZumaDeluxeBoards)[self.last_game_state_gauntlet_board]
            self.reset_level()
            self.reset_area()
            self.game_state_last_level = None
            self.game_up_area = ""
            self.game_actual_area = ""
            self.game_up_level = ""
            self.game_actual_sub_level = ""
            self.game_actual_level = ""
            self.game_difficulty = ZumaDeluxeGauntletDifficulties.RABBIT


    def score_control(self):
        if self.game_state_in_level != ZumaDeluxeInLevel.LEVEL:
            return
        if self.game_state_current_game_state != ZumaDeluxeGameState.PLAYING and self.game_state_current_game_state != ZumaDeluxeGameState.DANGER:
            return
        if self.game_state_current_game_mode is None:
            return
        if self.game_last_score == self.game_score:
            return
        if SectionState.Unlocked not in self.check_difficulty_state():
            return


        dif_score: int = self.game_score - self.game_last_score
        dif_score += self.game_missing_score
        self.game_missing_score = 0

        calculated_score: int = 0
        ignored_score: int = 0

        dif_balls: int = self.game_balls - self.game_last_balls

        dif_coins:int = self.game_coins-self.game_last_coins
        dif_gaps:int = self.game_gaps-self.game_last_gaps
        dif_combos: int = self.game_total_combo - self.game_last_total_combo
        dif_chains: int = self.game_chains-self.game_last_chains

        self.game_action_list.append(f"{dif_balls} destroyed BALLS, {dif_coins} coins," +
                                     f"{dif_gaps} gaps, {dif_combos} combos, {dif_chains} chains")
        self.game_action_list.append(f"{self.game_balls} bolas totales")

        if dif_balls > 0:
            score_balls: int = dif_balls * 10
            self.game_action_list.append(f"{dif_balls} destroyed BALLS for {score_balls} points")
            calculated_score += score_balls


        if dif_coins > 0:
            mult:int = self.game_state_manager.get_coin_value()
            if mult<200:
                mult = 500
            score_coins: int = dif_coins * mult
            self.game_action_list.append(f"{dif_coins} coins for {score_coins} points")
            calculated_score += score_coins
            if not self.have_coins():
                ignored_score -= score_coins
            self.game_area_coins += dif_coins

        if dif_chains > 0 and self.game_chains >= 5:
            #100 +10
            base_chains:int = 0
            count_chains:int
            if self.game_last_chains > self.game_chains or self.game_last_chains < 4:
                count_chains = self.game_chains - 4
            else:
                count_chains = dif_chains
                base_chains =self.game_last_chains-4
            score_chains: int = count_chains * 100
            for i in range(count_chains):
                score_chains += 10*i+base_chains*10
            self.game_action_list.append(f"{count_chains} chains, last {base_chains} for {score_chains} points")
            calculated_score += score_chains
            if not self.have_chains():
                ignored_score -= score_chains
            if self.game_chains >self.game_area_chains:
                self.game_area_chains = self.game_chains


        if dif_combos > 0:
            # 100+ per combo
            base_combos: int = 0
            count_combos:int
            #if self.game_last_actual_combo > self.game_actual_combo:
             #   count_combos = self.game_actual_combo
            #else:
            count_combos = dif_combos
            base_combos =self.game_last_actual_combo
            score_combos: int = count_combos * 100
            for i in range(count_combos):
                score_combos += 100*i+base_combos*100
            self.game_action_list.append(f"{count_combos} combos, last {base_combos} for {score_combos} points")
            calculated_score += score_combos
            self.game_last_actual_combo += dif_combos
            while dif_score < calculated_score:
                self.game_last_actual_combo -=1
                calculated_score -= 100

            if not self.have_combos():
                ignored_score -= score_combos
            if self.game_last_actual_combo > self.game_area_max_combo:
                self.game_area_max_combo = self.game_last_actual_combo
            self.game_area_total_combo += dif_combos

        else:
            self.game_last_actual_combo = 0

        if dif_gaps > 0:
            max_gap: int = dif_gaps * 500
            score_gaps: int
            if dif_score - calculated_score > max_gap:
                score_gaps = max_gap
            else:
                score_gaps = dif_score - calculated_score
            calculated_score += score_gaps
            if not self.have_gaps():
                ignored_score -= score_gaps
            self.game_area_gaps += dif_gaps

        self.game_state_manager.add_to_score(ignored_score)
        if calculated_score > dif_score:

            self.game_action_list.append(f"something went wrong we take to much {calculated_score} points for {dif_score}")
        if dif_score > calculated_score:

            self.game_missing_score = dif_score - calculated_score
            self.game_action_list.append(f"something went wrong we take to little {calculated_score} points for {dif_score}")
        if dif_score == calculated_score:
            self.game_action_list.append(
                f"we took just enough {calculated_score} points for {dif_score}")




        self.game_last_score = self.game_score+ignored_score
        self.game_last_balls = self.game_balls
        self.game_last_coins = self.game_coins
        self.game_last_gaps = self.game_gaps
        self.game_last_total_combo = self.game_total_combo
        self.game_last_chains = self.game_chains


    def have_item_su_type(self, item_type:str)->bool:
        if self.game_actual_section is not None:
            stage_name: str = self.game_actual_section.value.split("- ")[1]
            item_name:str = stage_name +" (" + item_type + ")"
            if item_name in self.received_items:
                if self.received_items[item_name] != 0:
                    return True
                else:
                    return False
            else:
                self.received_items[item_name] = 0
                return False

        else:
            return False

    def toggle_item_su_type(self, item_type:str):
        if self.game_actual_section is None:
            return
        stage_name: str = self.game_actual_section.value.split("- ")[1]
        item_name: str = stage_name + " (" + item_type + ")"
        if self.have_item_su_type(item_type):
            self.received_items[item_name] = 0
        else:
            self.received_items[item_name] = 1

    def have_coins(self)->bool:
        return self.have_item_su_type("Coins")
    def have_gaps(self)->bool:
        return self.have_item_su_type("Gaps")
    def have_combos(self)->bool:
        return self.have_item_su_type("Combos")
    def have_chains(self)->bool:
        return self.have_item_su_type("Chains")

    speed_multiplier: float = 1


    def death_linker(self,delta: float):


        if self.game_state_in_level != ZumaDeluxeInLevel.LEVEL:
            self.death_has_come = False
            return
        if SectionState.Unlocked not in self.check_difficulty_state() and SectionState.GoalUnlocked not in self.check_difficulty_state():
            return
        if not self.deathlink:
            return
        if self.speed_multiplier > 1:
            self.speed_multiplier += delta
            self.death_has_come = True
        else:
            if not self.death_has_come:

                if self.game_state_current_game_state == ZumaDeluxeGameState.GAME_OVER or self.lost_a_live:
                    self.send_death = True
                    self.death_has_come = True
            else:
                if self.game_state_current_game_state == ZumaDeluxeGameState.PLAYING:
                    self.death_has_come = False
        if self.game_state_current_game_state == ZumaDeluxeGameState.GAME_OVER or self.lost_a_live:
            self.reset_level()





    def check_for_completed_locations(self):
        if self.game_state_in_level != ZumaDeluxeInLevel.LEVEL:
            return
        if self.game_state_current_game_mode is None:
            return
        if self.game_actual_section is None:
            return
        if self.game_state_current_level is None:
            return

        if self.moved_up and SectionState.Unlocked in self.check_state():
            the_last_was_true = (self.game_state_current_level-1) // 7 <= self.check_item("Progressive Difficulty")
            print("unlocked difficulty?")
            if the_last_was_true:
                print("unlocked difficulty")
                if self.game_state_current_game_mode == ZumaDeluxeMode.GAUNTLET:
                    clear: str = self.game_up_level + " (Level Clear)"
                    print(clear)

                    self.send_location(clear)
                    if self.game_up_area != self.game_actual_area:
                        full_clear: str = self.game_up_area + " (Full Clear)"

                        self.send_location(full_clear)

                    self.check_goal_level_clear = self.game_state_current_level-1 if self.game_state_current_level is not None else -1


        if  SectionState.Unlocked not in self.check_difficulty_state() and SectionState.GoalUnlocked not in self.check_difficulty_state():
            return


        stage_name: str = self.game_actual_section.value.split("- ")[1]
        # if self.game_curren
        #

        if self.game_area_coins >= self.coins:
            self.send_location(self.game_actual_area + " (Coins)")
        if self.game_area_gaps >= self.gaps:
            self.send_location(self.game_actual_area + " (Gaps)")
        if self.game_area_total_combo >= self.combo:
            self.send_location(self.game_actual_area + " (Combos)")
        if self.game_area_max_combo+1 >= self.max_combo:
            self.send_location(self.game_actual_area + " (Combo Max)")
        if self.game_area_chains >= self.chain:
            self.send_location(self.game_actual_area + " (Chains)")
        if (self.game_state_current_game_state == ZumaDeluxeGameState.CLEAR_MENU
                and not self.checked_clear):
            clear: str = self.game_actual_sub_level + " (Level Clear)"
            print("entering checker")
            self.send_location(clear)
            lev = self.game_state_current_level
            area_clear: bool
            if lev < 15:
                area_clear = (lev + 1) % 5 == 0
            elif lev < 33:
                area_clear = (lev - 14) % 6 == 0
            else:
                area_clear = (lev - 32) % 7 == 0
            if area_clear:
                full_clear: str = self.game_actual_area + " (Full Clear)"
                self.send_location(full_clear)
            print(self.game_state_got_ace_time)
            if self.include_ace_time and self.game_state_got_ace_time:
                self.send_location(self.game_actual_sub_level + " (Ace Time)")
            self.check_goal_level_clear = self.game_state_current_level if self.game_state_current_level is not None else -1
            self.checked_clear = True



    def send_location(self, location:str):
        if location not in self.completed_locations and location not in self.completed_locations_queue:
            self.completed_locations.add(location)
            self.completed_locations_queue.append(location)


    def process_received_items(self):
        while len(self.received_items_queue) > 0:

            item: str = self.received_items_queue.popleft()
            print(item)

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

            is_unlock: bool = "Unlock" in item
            if is_unlock:
                level: str = item.split()[0]
                name: str = item.split(": ")[1]

                if level == "Stage" and self.adventure_selection is not None:

                    for stage in self.adventure_selection:

                        if name in stage.value:
                            if SectionState.Blocked in self.adventure_selection[stage]:
                                self.adventure_selection[stage].remove(SectionState.Blocked)
                                self.adventure_selection[stage].append(SectionState.Unlocked)
                            if SectionState.GoalLocked in self.adventure_selection[stage]:
                                self.adventure_selection[stage].remove(SectionState.GoalLocked)
                                self.adventure_selection[stage].append(SectionState.GoalIncomplete)

                            continue
                else:
                    if self.gauntlet_selection is not None:
                        for board in self.gauntlet_selection:
                            if name in board.value:
                                if SectionState.Blocked in self.gauntlet_selection[board]:
                                    self.gauntlet_selection[board].remove(SectionState.Blocked)
                                    self.gauntlet_selection[board].append(SectionState.Unlocked)
                                if SectionState.GoalLocked in self.gauntlet_selection[board]:
                                    self.gauntlet_selection[board].remove(SectionState.GoalLocked)
                                    self.gauntlet_selection[board].append(SectionState.GoalIncomplete)
                            continue

            if item in "Progressive Lives" and self.game_state_in_level == ZumaDeluxeInLevel.LEVEL:
                self.game_state_manager.add_lives(1)

            if item in extra_items:
                print(item)
                if item not in self.filler_items_times:
                    self.filler_items_times[item] = 0.0
                duration = extra_items[item]["duration"]
                self.filler_items_times[item] += duration
                if self.filler_items_times[item] > 60:
                    self.filler_items_times[item] = 60



    def process_useful_and_traps(self, df:float):

        if self.game_state_in_level != ZumaDeluxeInLevel.LEVEL:
            return
        if self.game_state_current_game_state != ZumaDeluxeGameState.PLAYING and self.game_state_current_game_state != ZumaDeluxeGameState.DANGER:
            return
        if self.game_state_current_game_mode is None:
            return
        if  SectionState.Unlocked not in self.check_difficulty_state() and SectionState.GoalUnlocked not in self.check_difficulty_state():
            return
        if self.game_actual_section is None or self.game_state_current_level is None:
            return
        to_remove = []
        actual_speed = self.level_speed
        target_speed = actual_speed
        trapped_speed = False
        for item in self.filler_items_times:
            last = self.filler_items_times[item]
            duration = extra_items[item]["duration"]
            if duration != 0.5:
                act = last - df
            else:
                act = last - duration
            last *= 2
            act *= 2
            if act <= 0:
                act = -1
            if item == "Rush" or item == "Get a Break":
                trapped_speed = True
            if math.floor(last)!= math.floor(act):
                match item:
                    case "Happy Sun":
                        self.game_state_manager.add_to_score(10)
                    case "Extra Live":
                        self.game_state_manager.add_lives(1)
                    case "Combo Killer":
                        self.game_last_actual_combo = 0
                    case "Chain Breaker":
                        self.game_last_chains = 0
                    case "Half Score":
                        dif_score: int = (self.game_score - self.game_base_score) // 2
                        self.game_state_manager.add_to_score(-dif_score)
                        self.game_last_score -= dif_score
                    case "Extra Coin":
                        mult: int = self.game_state_manager.get_coin_value()
                        if mult < 200:
                            mult = 500
                        self.game_area_coins += 1
                        self.game_state_manager.add_to_score(mult)
                        self.game_last_score += mult

                    case "Color Shift":
                        maxcolor: int = 4
                        if self.game_state_current_game_mode == ZumaDeluxeMode.GAUNTLET:
                            maxcolor = min(self.game_state_current_level // 7 + 4, 6)
                        else:
                            if self.game_state_current_level < 15:
                                maxcolor = 4
                            elif self.game_state_current_level < 33:
                                maxcolor = 5
                            else:
                                maxcolor = 6

                        self.game_state_manager.change_random_color(maxcolor)
                    case "Rush":
                        double_speed = self.get_level_base_speed() * 2
                        if actual_speed != double_speed:
                            target_speed = double_speed
                    case "Get a Break":
                        break_speed = 0.0
                        if actual_speed != break_speed:
                            target_speed = break_speed
                        else:
                            if actual_speed == target_speed:
                                target_speed = self.get_level_base_speed()/2
            if act < 0:
                to_remove.append(item)
            self.filler_items_times[item]  = act / 2

        if not trapped_speed:
            self.game_state_manager.set_level_speed(self.get_level_base_speed()* self.speed_multiplier)
        else:
            if actual_speed != target_speed:
                self.game_state_manager.set_level_speed(target_speed+(self.speed_multiplier/2))
        for item in to_remove:
            self.filler_items_times.pop(item)

    ready_level = False
    def harder_goal(self):


        if self.game_state_current_game_state is not ZumaDeluxeGameState.PLAYING and self.game_state_current_game_state is not ZumaDeluxeGameState.DANGER:
            self.ready_level = False
            return

        if self.ready_level:
            return

        print("harder_level")
        self.ready_level = True

        if not SectionState.Unlocked in self.check_difficulty_state():
            return

        if not SectionState.GoalUnlocked in self.check_difficulty_state():
            return

        if  not isinstance(self.game_actual_section, ZumaDeluxeStages):
            return
        suns = self.sun_idols_helpers - self.check_sun_idols()
        total_extra_amount:int = suns * 2000
        extra_level_amounts: int = 0
        lev = self.game_state_current_level
        area_clear: bool
        if lev < 15:
            extra_level_amounts = total_extra_amount // 5
        elif lev < 33:
            extra_level_amounts = total_extra_amount // 6
        else:
            extra_level_amounts = total_extra_amount // 7
        self.game_state_manager.add_to_target_score(extra_level_amounts)

    goal_levels = 0

    def _check_for_victory(self):
        if self.check_sun_idols() < self.sun_idols_required:
            self.goal_levels = 0
            return
        if self.selected_goal_level_gauntlet is not None and self.gauntlet_selection is not None:
            if SectionState.GoalIncomplete in self.gauntlet_selection[self.selected_goal_level_gauntlet]:
                self.gauntlet_selection[self.selected_goal_level_gauntlet].remove(SectionState.GoalIncomplete)
                self.gauntlet_selection[self.selected_goal_level_gauntlet].append(SectionState.GoalUnlocked)
        if self.selected_goal_level_adventure is not None and self.adventure_selection is not None:
            if SectionState.GoalIncomplete in self.adventure_selection[self.selected_goal_level_adventure]:
                self.adventure_selection[self.selected_goal_level_adventure].remove(SectionState.GoalIncomplete)
                self.adventure_selection[self.selected_goal_level_adventure].append(SectionState.GoalUnlocked)

        if self.game_actual_section is None:
            self.goal_levels = 0
            return
        if self.check_goal_level_clear == -1:
            return
        #print("tried goal")
        if isinstance(self.game_actual_section, ZumaDeluxeBoards):
            #print("tried gauntlet")
            if self.game_actual_section != self.selected_goal_level_gauntlet:
                #print("not same")
                self.goal_levels = 0
                return

            level_target: int = 0
            dif_lev: int = self.selected_gauntlet_difficulty
            level_target = dif_lev * 7
            #print(f"target dificulty {level_target}")
            #print(f"level{self.check_goal_level_clear}")
            suns = self.sun_idols_helpers - self.check_sun_idols()
            if self.check_goal_level_clear >= level_target:
                if self.goal_levels >= suns:
                    self.goal_completed = True
                    #print("done")
                    return
                #print("not amount of levels")
                print(suns)
                self.goal_levels += 1
                print(self.goal_levels)

        if isinstance(self.game_actual_section, ZumaDeluxeStages):
            #print("tried adventure")
            if self.game_actual_section != self.selected_goal_level_adventure:
                #print("not same")
                self.goal_levels = 0
                return
            dif_lev: int = self.game_state_current_level
            #print(f"level {dif_lev}")
            if dif_lev < 15:
                total_lev = 5
            elif dif_lev < 33:
                total_lev = 6
            else:
                total_lev = 7
            #print(f"total levels{total_lev}")
            self.goal_levels += 1
            #print(self.goal_levels)
            if self.goal_levels >= total_lev:
                self.goal_completed = True
                #print("done")
                return
            #print("not amount of levels")
            #print(total_lev)

            print(self.goal_levels)







    def check_state(self) -> List[SectionState]:
        state:List[SectionState] = [SectionState.NoneSelected]
        if self.game_actual_section is not None:
            if isinstance(self.game_actual_section, ZumaDeluxeBoards):
                try:
                    return self.gauntlet_selection[self.game_actual_section]
                except Exception:
                    pass
            else:
                try:
                    return self.adventure_selection[self.game_actual_section]
                except Exception:
                    pass

        return state

    def check_difficulty_state(self)->List[SectionState]:
        state:List[SectionState] = self.check_state()
        if SectionState.Unlocked not in state:
            return state
        else:
            if not isinstance(self.game_actual_section, ZumaDeluxeBoards):
                return state
            act_dif: int = list(ZumaDeluxeGauntletDifficulties).index(self.game_difficulty)
            max_dif: int = self.selected_gauntlet_difficulty
            many_dif: int = self.check_item("Progressive Difficulty")

            if act_dif > max_dif:
                state = [SectionState.NoneSelected]
            if many_dif < act_dif <= max_dif:
                state_list = []
                for stat in state:
                    if stat == SectionState.Unlocked:
                        state_list.append(SectionState.Blocked)
                    else:
                        state_list.append(stat)
                state = state_list

            return state




    def check_item(self, name: str)->int:
        if name not in self.received_items:
            self.received_items[name] = 0
        return  self.received_items[name]
    def check_sun_idols(self)->int:
        return self.check_item("Sun Idol")

    def check_progressive_lives(self)->int:

        return self.check_item("Progressive Lives")+1

    def reset_level(self):
        self.game_last_balls = 0
        self.game_last_coins = 0
        self.game_last_actual_combo = 0
        self.game_last_total_combo = 0
        self.game_last_chains = 0
        self.game_missing_score = 0
        self.game_state_last_level = self.game_state_current_level
        self.game_last_score = self.game_score
        self.ready_level = False
        self.speed_multiplier = 1


    def reset_area(self):
        self.game_area_coins = 0
        self.game_area_total_combo = 0
        self.game_area_chains = 0
        self.game_area_gaps = 0
        self.game_last_section = self.game_actual_section
        self.game_last_difficulty = self.game_difficulty
        self.game_area_max_combo = 0
        self.game_state_manager.set_lives(self.check_progressive_lives())
        self.last_live = self.check_progressive_lives()
        self.lost_a_live = False
        self.speed_multiplier = 1

    def get_level_base_speed(self)-> float:
        base_speed: float = 0.5
        if isinstance(self.game_actual_section, ZumaDeluxeStages):
            base_speed = levels_base_speed_adventure[self.get_adventure_str()]
        elif isinstance(self.game_actual_section, ZumaDeluxeBoards):
            dif_base: int = list(ZumaDeluxeGauntletDifficulties).index(self.game_difficulty)
            level = self.game_state_current_level if self.game_state_current_level is not None else 0
            if level < dif_base*7:
                level = level % 7
            else:
                level = level - dif_base*7
            match(dif_base):
                case 0:
                    if level < 3:
                        base_speed = 0.5+level*0.1
                    else:
                        base_speed = 0.6 + level*0.05

                    if base_speed > 0.9:
                        base_speed = 0.9
                case 1:
                    base_speed = 0.7 + level * 0.05
                    if base_speed > 0.95:
                        base_speed = 0.95
                case 2:
                    if level < 3:
                        base_speed = 0.8+level*0.05
                    else:
                        base_speed = 0.85 + ((level+1)//2) * 0.05
                    if base_speed > 1.2:
                        base_speed = 1.2
                case 3:
                    base_speed = 0.95 + ((level + 1) // 2) * 0.05
                    if base_speed > 1.5:
                        base_speed = 1.5
        return base_speed

    def get_adventure_str(self)-> str:
        level = self.game_state_current_level if self.game_state_current_level is not None else 0
        temple: int = 1
        base_temple_level: int = 1
        sub_level = 1
        if level < 15:
            temple += level // 5
            sub_level += (level % 5)
        elif level < 33:
            temple  += ((level - 15) // 6) + 3
            sub_level += ((level - 15) % 6)
        else:
            temple += ((level - 33) // 7) + 6
            sub_level += ((level - 33) % 7)

        return f"{temple}-{sub_level}"




