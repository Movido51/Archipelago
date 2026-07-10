from typing import List, NamedTuple, Optional, Tuple
import random

from pymem import Pymem
from pymem.process import close_handle, list_processes
from pymem.ressources.structure import ProcessEntry32

from .enums import (
    ZumaDeluxeInLevel,
    ZumaDeluxeGameState,
    ZumaDeluxeMode,
    ZumaDeluxeStages,
    ZumaDeluxeBoards
)

class GameState(NamedTuple):
    playing: ZumaDeluxeInLevel = ZumaDeluxeInLevel.MENU
    game_state_in_game: ZumaDeluxeGameState = ZumaDeluxeGameState.OTHER
    current_level: Optional[int] = None
    gauntlet_level: Optional[int] = None
    gauntlet_board: Optional[int] = None
    destroyed_balls: int = 0
    combos_total: int = 0
    actual_score: int = 0
    base_score: int = 0
    max_combo: int = 0
    chains: int = 0
    gaps: int = 0
    coins: int = 0
    level_speed: float = 0
    actual_time: int = 0
    ace_time_bool: bool = False
    actual_live: int = -1






class GameStateManager:
    process_name: str = "popcapgame"


    signature_address : int = 0x64
    signature_string: str = "Zuma"
    base_address: int = 0x19F4A4


    process: Optional[Pymem]
    is_process_running: bool

    stage_manager_address: Optional[int]
    game_state_address: Optional[int]

    gauntlet_board_address: Optional[int]

    unique_score_address: Optional[int]
    difficulty_base_address: Optional[int]
    balls_address: Optional[int]



    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.stage_manager_address = None
        self.game_state_address = None

        self.gauntlet_board_address = None

        self.unique_score_address = None
        self.difficulty_base_address = None
        self.balls_address = None

    @property
    def stage_manager_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x19F4A4, (0x72C,0x00))
    @property
    def current_level_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None

        return self.stage_manager_struct_address + 0x29C

    @property
    def global_score_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0xE8

    @property
    def final_time_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1E0

    @property
    def destroyed_blocks_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1E4
    @property
    def grabbed_coins_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1E8

    @property
    def total_gaps_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1EC
    @property
    def total_combo_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1F0
    @property
    def max_combo_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1F4
    @property
    def actual_chain_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x18C
    @property
    def lives_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0xF0
    @property
    def actual_time_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x1F4

    @property
    def base_score_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x168
    @property
    def target_score_address(self) -> Optional[int]:
        if self.stage_manager_struct_address is None:
            return None
        return self.stage_manager_struct_address + 0x164



    @property
    def game_state_struct_address(self) -> Optional[int]:
        return self.process.read_uint(self.process.base_address + 0x19F4A4) + 0x794
        return self._resolve_address(0x19F4A4,(-0x1348))
        return 0x001AE3D0


    @property
    def difficulty_base_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x19F4A4, (0x72c,0x128,0x00))
    @property
    def gauntlet_indicator_address(self)->Optional[int]:
        if self.difficulty_base_struct_address is None:
            return None
        return self.difficulty_base_struct_address + 0x6C
    @property
    def ace_time_address(self) -> Optional[int]:
        if self.difficulty_base_struct_address is None:
            return None
        return self.difficulty_base_struct_address + 0x78
    @property
    def principal_speed_address(self) -> Optional[int]:
        if self.difficulty_base_struct_address is None:
                return None
        return self.difficulty_base_struct_address + 0xCC

    @property
    def secondary_speed_address(self) -> Optional[int]:
        if self.difficulty_base_struct_address is None:
            return None
        return self.difficulty_base_struct_address + 0x148


    @property
    def gauntlet_board_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x19F4A4, (0x734,0x120))


    @property
    def unique_score_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x19F4A4, (0x72C,0x10,0x94,0x160))


    @property
    def balls_struct_address(self)->Optional[int]:
        return self._resolve_address(0x19F4A4, (0x72C,0x298,0x00))
    @property
    def ready_ball_address(self)->Optional[int]:
        if self.balls_struct_address is None:
            return None
        return self.balls_address + 0x2C
    @property
    def ready_ball_color_address(self)->Optional[int]:
        if self.ready_ball_address is None:
            return None
        return self.process.read_uint(self.ready_ball_address) + 0x8
    @property
    def reserve_ball_address(self)->Optional[int]:
        if self.balls_struct_address is None:
            return None
        return self.balls_address + 0x30

    @property
    def reserve_ball_color_address(self) -> Optional[int]:
        if self.reserve_ball_address is None:
            return None
        return self.process.read_uint(self.reserve_ball_address) + 0x8

    def get_current_game_state(self)-> ZumaDeluxeGameState:
        if self.game_state_struct_address is None:
            return ZumaDeluxeGameState.OTHER
        try:

            game_state_value: int = self.process.read_int(self.game_state_struct_address)

            return ZumaDeluxeGameState(game_state_value)
        except Exception:
            print(f"error getting it in {hex(self.game_state_struct_address)}")
            return ZumaDeluxeGameState.OTHER

    def get_current_level(self) -> Optional[int]:
        if self.current_level_address is None:
            return None
        try:

            return self.process.read_int(self.current_level_address)
        except Exception:
            return None
    def get_current_gauntlet_level(self)->Optional[int]:
        if self.gauntlet_indicator_address is None:
            return None
        try:
            return self.process.read_int(self.gauntlet_indicator_address)
        except Exception:
            return None
    def get_current_level_time(self)->Optional[int]:
        if self.final_time_address is None:
            return None
        if self.actual_time_address is None:
            return self.process.read_int(self.final_time_address)
        try:
            final_time_value: int = self.process.read_int(self.final_time_address)
            level_time_value: int = self.process.read_int(self.actual_time_address)
            if(final_time_value != 0):
                return final_time_value
            return level_time_value
        except Exception:
            return None
    def get_current_board_menu(self)->Optional[int]:
        if self.gauntlet_board_struct_address is None:
            return None
        try:
            board_index: int = self.process.read_int(self.gauntlet_board_struct_address)
            return board_index
        except Exception:
            return None
    def get_destroyed_balls(self)->int:
        if self.destroyed_blocks_address is None:
            return 0
        try:
            balls_destroyed: int = self.process.read_int(self.destroyed_blocks_address)
            return balls_destroyed
        except Exception:
            return 0

    def get_grabbed_coins(self)->int:
        if self.grabbed_coins_address is None:
            return 0
        try:
            coins: int = self.process.read_int(self.grabbed_coins_address)
            return coins
        except Exception:
            return 0

    def get_made_chains(self)->int:
        if self.actual_chain_address is None:
            return 0
        try:
            chain_made: int = self.process.read_int(self.actual_chain_address)
            return chain_made
        except Exception:
            return 0
    def get_max_combo(self)->int:
        if self.max_combo_address is None:
            return 0
        try:
            combo: int = self.process.read_int(self.max_combo_address)
            return combo
        except Exception:
            return 0
    def get_total_combo(self)->int:
        if self.total_combo_address is None:
            return 0
        try:
            total_combo: int = self.process.read_int(self.total_combo_address)
            return total_combo
        except Exception:
            return 0
    def get_total_gaps(self)->int:
        if self.total_gaps_address is None:
            return 0
        try:
            total_gaps: int = self.process.read_int(self.total_gaps_address)
            return total_gaps
        except Exception:
            return 0

    def get_actual_score(self)->int:
        if self.global_score_address is None:
            return 0
        try:
            score: int = self.process.read_int(self.global_score_address)
            base_score: int = self.process.read_int(self.base_score_address)
            if base_score > score:
                self.set_score(base_score)
                return base_score
            return score
        except Exception:
            return 0
    def get_base_score(self)-> int:
        if self.base_score_address is None:
            return -1
        try:
            base_score: int = self.process.read_int(self.base_score_address)
            return base_score
        except Exception:
            return -1

    def get_target_score(self)->int:
        if self.base_score_address is None:
            return -1
        try:
            target_score: int = self.process.read_int(self.target_score_address)
            return target_score
        except Exception:
            return -1
    def get_coin_value(self)->int:
        if self.get_target_score() == -1:
            return -1
        if self.get_base_score() == -1:
            return -1
        coins_value: int = 100
        dif_score = self.get_target_score() - self.get_base_score()
        coins_value *= dif_score //600
        return coins_value


    #writing

    def set_score(self, new_score: int)->bool:
        if self.global_score_address is None:
            return False
        try:
            self.process.write_int(self.global_score_address, new_score)
            return True
        except Exception:
            print("Failed to set score")
            return False




    def add_to_score(self, add :int)->bool:
        if self.global_score_address is None:
            return False
        try:
            actual: int = self.process.read_int(self.global_score_address)

            return self.set_score(actual+add)

        except Exception:
            print("failed to get actual score")
            return False

    def get_lives(self)->int:
        if self.lives_address is None:
            return -1
        try:
            actual: int = self.process.read_int(self.lives_address)
            return actual
        except Exception:
            print("failed to get lives")
            return -1

    def set_lives(self,new_lives:int)->bool:
        if self.lives_address is None:
            return False
        try:
            self.process.write_int(self.lives_address, new_lives)
            return True
        except Exception:
            return False

    def add_lives(self,add:int)->bool:
        if self.lives_address is None:
            return False
        try:
            actual: int = self.process.read_int(self.lives_address)
            return self.set_lives(actual+add)
        except Exception:
            print("failed to add lives")
            return False
    def change_random_color(self)->bool:
        if self.ready_ball_color_address is None:
            return False
        if self.reserve_ball_color_address is None:
            return False
        try:
            ready_color: int = self.process.read_int(self.ready_ball_color_address)
            reserved_color: int = self.process.read_int(self.reserve_ball_color_address)
            change_ready: int = random.randint(0, 5)
            change_reserved: int = random.randint(0, 5)
            ready_color += change_ready
            reserved_color += change_reserved
            self.process.write_int(self.ready_ball_color_address, ready_color)
            self.process.write_int(self.reserve_ball_color_address, reserved_color)

        except Exception:
            print("failed to change random color")
            return False

    def get_level_speed(self)->float:
        if self.principal_speed_address is None:
            return 0.0
        try:
            return  self.process.read_float(self.principal_speed_address)
        except Exception:
            print("no speed found")
            return 0.0
    def set_level_speed(self,new_speed:float)->bool:
        if self.principal_speed_address is None:
            return False

        try:
            self.process.write_float(self.principal_speed_address, new_speed)
        except Exception:
            print("unable to set speed primary")
            return False
        if self.secondary_speed_address is None:
            return False
        try:
            self.process.write_float(self.secondary_speed_address, new_speed)
        except Exception:
            print("unable to set speed secondary")
            return False
        return True

    def got_ace_time(self)->bool:
        if self.ace_time_address is None:
            return False
        if self.final_time_address is None:
            return False
        try:
            ace_time: int = self.process.read_int(self.ace_time_address)
            final_time: int = self.process.read_int(self.final_time_address)
            if final_time == 0:
                return False
            final_time = final_time //100
            if ace_time > final_time:
                return True
        except Exception:
            return False
    def set_target_score(self, setter:int)->bool:
        if self.target_score_address is None:
            return False
        try:
            self.process.write_int(self.target_score_address, setter)
            return True
        except Exception:
            print("unable to set score")
            return False
    def add_to_target_score(self, add:int)->bool:
        if self.target_score_address is None:
            return False
        try:
            old_target: int = self.process.read_int(self.target_score_address)
            return self.set_target_score(old_target+add)
        except Exception:
            print("unable to set score")
            return False



    def get_game_state(self)->GameState:

        self.stage_manager_address = self.stage_manager_struct_address
        self.game_state_address = self.game_state_struct_address
        self.gauntlet_board_address = self.gauntlet_board_struct_address
        self.unique_score_address = self.unique_score_struct_address
        self.difficulty_base_address = self.difficulty_base_struct_address
        self.balls_address = self.balls_struct_address

        state: ZumaDeluxeGameState = self.get_current_game_state()
        playing: ZumaDeluxeInLevel

        try:
            if self.stage_manager_address is None or self.stage_manager_address == 0:

                playing = ZumaDeluxeInLevel.MENU
            else:
                playing = ZumaDeluxeInLevel.LEVEL
        except Exception:
            playing = ZumaDeluxeInLevel.MENU

        if playing == ZumaDeluxeInLevel.MENU:
            return GameState(
                playing=playing,
                game_state_in_game=state,
                gauntlet_board=self.get_current_board_menu(),
            )

        return  GameState(
            playing=playing,
            game_state_in_game=state,
            current_level = self.get_current_level(),
            gauntlet_level = self.get_current_gauntlet_level(),
            gauntlet_board=self.get_current_board_menu(),
            destroyed_balls=self.get_destroyed_balls(),
            coins = self.get_grabbed_coins(),
            gaps =  self.get_total_gaps(),
            combos_total=  self.get_total_combo(),
            chains= self.get_made_chains(),
            actual_score = self.get_actual_score(),
            base_score = self.get_base_score(),
            max_combo=self.get_max_combo(),
            level_speed=self.get_level_speed(),
            ace_time_bool=self.got_ace_time(),
            actual_live= self.get_lives()

        )


    def open_process_handle(self) -> bool:
        try:
            candidate_pids: List[int] = list()

            process: ProcessEntry32
            for process in list_processes():
                if self.process_name.lower() in process.szExeFile.decode("utf-8").lower():
                    candidate_pids.append(process.th32ProcessID)

            if not len(candidate_pids):
                return False

            pid: int
            for pid in candidate_pids:
                try:
                    process: Pymem = Pymem(pid)

                    address: int = process.read_uint(process.base_address + self.base_address)

                    name: str =process.read_string(address+self.signature_address, len(self.signature_string))
                    if name == self.signature_string:
                        self.process = process
                        self.is_process_running = True

                        break
                except Exception:
                    print(f"{pid} broke")
                    pass

            if not self.is_process_running:
                return False

            self.stage_manager_address = self.stage_manager_struct_address
            self.game_state_address = self.game_state_struct_address

            self.gauntlet_board_address = self.gauntlet_board_struct_address

            self.unique_score_address = self.unique_score_struct_address
            self.difficulty_base_address = self.difficulty_base_struct_address
            self.balls_address = self.balls_struct_address
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.stage_manager_address = None
            self.game_state_address = None

            self.gauntlet_board_address = None

            self.unique_score_address = None
            self.difficulty_base_address = None
            self.balls_address = None

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.stage_manager_address = None
            self.game_state_address = None

            self.gauntlet_board_address = None

            self.unique_score_address = None
            self.difficulty_base_address = None
            self.balls_address = None

            return False

        return True


    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_uint(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_uint(address + offset)
            except Exception:
                return None

        return address + offsets[-1]