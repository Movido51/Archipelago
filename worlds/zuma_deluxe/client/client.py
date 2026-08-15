import asyncio
import math
import sys
import time
import urllib.parse

import CommonClient
import NetUtils
import Utils

from typing import Set, Optional, Dict, Any, List

from ..gameControl.game_controller import GameController, SectionState

from ..items_data import items_names_to_ids,items_ids_to_names
from ..locations_data import locations_names_to_ids, locations_ids_to_names

from ..gameControl.enums import *



class ZumaDeluxeCommandProcessor(CommonClient.ClientCommandProcessor):
    ctx: "ZumaDeluxeContext"

    async def _cmd_deathlink(self):
        """If your Death Link setting is set to "Toggle", use this command to turn Death Link on and off."""
        if self.ctx.game_controller.deathlink_option is not None:
            if self.ctx.game_controller.deathlink_option  == 1:
                if self.ctx.game_controller.deathlink:
                    self.ctx.game_controller.deathlink = False
                    self.output(f"Death Link turned off")
                else:
                    self.ctx.game_controller.deathlink = True
                    self.output(f"Death Link turned on")


            else:
                self.output(f"'death_link' is not set to 'toggle' for this seed.")
                self.output(f"'death_link' = " + str(self.ctx.game_controller.deathlink_option))
        else:
            self.output(
                f"No 'death_link' in slot_data keys. You probably aren't connected or are playing an older seed.")

class ZumaDeluxeContext(CommonClient.CommonContext):
    #tags: Set[str] = {"AP"}
    game: str = "Zuma Deluxe"
    command_processor  = ZumaDeluxeCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True
    client_loop: Optional[asyncio.Task]

    game_controller: GameController

    items_ids_to_names = items_ids_to_names
    location_ids_to_names = locations_ids_to_names


    items_names_to_ids = items_names_to_ids
    locations_names_to_ids = locations_names_to_ids

    seen_item_indices : Set[int] = set()

    data_storage_key: Optional[str]

    can_display_process_found_message: bool
    can_display_process_not_found_message: bool


    def __init__(self, server_address: Optional[str], password: Optional[str]):
        super().__init__(server_address, password)

        self.game_controller = GameController(logger=CommonClient.logger)
        self.controller_task = None


        self.seen_item_indices = set()
        self.can_display_process_found_message = True
        self.can_display_process_not_found_message = True

    def make_gui(self):
        from .client_gui import ZumaDeluxeManager
        return ZumaDeluxeManager

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

            # generated

            self.game_controller.mode = ZumaDeluxeMode(_args["slot_data"]["game_mode"])
            self.game_controller.goal = ZumaDeluxeAPGoals(_args["slot_data"]["goal"])
            self.game_controller.goal_mode = ZumaDeluxeMode(_args["slot_data"]["goal_mode"])

            self.game_controller.sun_idols_required = _args["slot_data"]["sun_idols_required_amount"]
            self.game_controller.sun_idols_helpers= _args["slot_data"]["sun_idols_helpers_amount"]
            self.game_controller.sun_idols_total = _args["slot_data"]["sun_idol"]

            self.game_controller.include_ace_time = bool(_args["slot_data"]["ace_time"])
            self.game_controller.coins = _args["slot_data"]["coins"]
            self.game_controller.gaps = _args["slot_data"]["gaps"]
            self.game_controller.combo = _args["slot_data"]["combo"]
            self.game_controller.max_combo = _args["slot_data"]["max_combo"]
            self.game_controller.chain = _args["slot_data"]["chain"]

            amount_levels = 7
            self.game_controller.coins = math.ceil(amount_levels * self.game_controller.coins / 100.0)
            self.game_controller.gaps = math.ceil(amount_levels * self.game_controller.gaps / 100.0)
            self.game_controller.combo = math.ceil(amount_levels * self.game_controller.combo / 100.0)




            self.game_controller.target_ratios = _args["slot_data"]["clear_score_multiplier"]
            self.game_controller.maximum_lives = _args["slot_data"]["maximum_starting_lives"]

            self.game_controller.selected_gauntlet_difficulty = _args["slot_data"]["gauntlet_difficulty"]

            self.game_controller.deathlink_option = _args["slot_data"]["death_link"]
            self.game_controller.deathlink = self.game_controller.deathlink_option != 0



            # # Generation Data
            if self.game_controller.mode != ZumaDeluxeMode.ADVENTURE:
                self.game_controller.selected_gauntlet_levels = [
                    ZumaDeluxeBoards(board_name) for board_name in _args["slot_data"]["gauntlet_selected_levels"]
                ]
                # self.game_controller.selected_starter_gauntlet = _args["slot_data"].get("gauntlet_stater_level")
                try:
                    self.game_controller.selected_goal_level_gauntlet = ZumaDeluxeBoards(
                        _args["slot_data"]["gauntlet_goal"])
                except Exception:
                    pass
                # set de niveles Gauntlet

                gauntlet_dict: Dict[ZumaDeluxeBoards, List[SectionState]] = {}
                for board in ZumaDeluxeBoards:
                    state: SectionState
                    if board in self.game_controller.selected_gauntlet_levels:
                        state = SectionState.Blocked
                        gauntlet_dict[board] = [state]

                        if board == self.game_controller.selected_goal_level_gauntlet:
                            state = SectionState.GoalLocked
                            gauntlet_dict[board].append(state)

                if self.game_controller.selected_goal_level_gauntlet not in self.game_controller.selected_gauntlet_levels and self.game_controller.selected_goal_level_gauntlet is not None:
                    gauntlet_dict[self.game_controller.selected_goal_level_gauntlet] = [SectionState.GoalLocked]

                self.game_controller.gauntlet_selection = gauntlet_dict



            if self.game_controller.mode != ZumaDeluxeMode.GAUNTLET:
                self.game_controller.selected_adventure_levels = [
                    ZumaDeluxeStages(stage_name) for stage_name in _args["slot_data"]["adventure_selected_levels"]
                ]

                #self.game_controller.selected_starter_adventure = _args["slot_data"].get("adventure_stater_level")
                try:
                    self.game_controller.selected_goal_level_adventure = ZumaDeluxeStages(_args["slot_data"]["adventure_goal"])
                except Exception:
                    pass
                adventure_dict: Dict[ZumaDeluxeStages, List[SectionState]] = {}
                for stage in ZumaDeluxeStages:
                    state: SectionState
                    if stage in self.game_controller.selected_adventure_levels:
                        state = SectionState.Blocked
                    else:
                        state = SectionState.NoneSelected

                    adventure_dict[stage] = [state]
                    if stage == self.game_controller.selected_goal_level_adventure:
                        adventure_dict[stage] = [SectionState.GoalLocked, SectionState.Blocked]
                self.game_controller.adventure_selection= adventure_dict

            # Data Storage
            self.data_storage_key = f"zuma_deluxe_{self.team}_{self.slot}"

            # Playing Status
            Utils.async_start(
                self.send_msgs([
                    {
                        "cmd": "StatusUpdate",
                        "status": CommonClient.ClientStatus.CLIENT_PLAYING
                    }
                ])
            )

            # UI Tabs
            self.ui.update_tabs()
    def on_deathlink(self, data: Dict[str, Any]) -> None:
        super().on_deathlink(data)
        print("received deathlink")
        if self.game_controller.deathlink:
            print("absorbed deathlink deathlink")
            message = data["cause"]
            if message == "":
                message = f"Death came by {data["source"]}"
            self.game_controller.last_death_message = message
            self.game_controller.speed_multiplier += 1

    async def controller(self):

        last_time = time.perf_counter()

        while not self.exit_event.is_set():
            await asyncio.sleep(0.2)
            now = time.perf_counter()
            dt = now - last_time
            last_time = now

            if  self.game_controller.deathlink != ("DeathLink" in self.tags):
                await self.update_death_link(self.game_controller.deathlink)


            # Enqueue Received Item Delta
            i: int
            network_item: NetUtils.NetworkItem

            for i, network_item in enumerate(self.items_received):
                if i in self.seen_item_indices:
                    continue

                item: str = self.items_ids_to_names[network_item.item]

                self.game_controller.received_items_queue.append(item)
                self.seen_item_indices.add(i)

            # Network Operations
            if self.server and self.slot:

                # Game Controller Update
                if not self.game_controller.is_process_running():
                    if not self.game_controller.open_process_handle():
                        if self.can_display_process_not_found_message:
                            CommonClient.logger.info("Looking for Zuma Deluxe process...")

                            self.can_display_process_found_message = True
                            self.can_display_process_not_found_message = False

                if self.game_controller.is_process_running():
                    if self.can_display_process_found_message:
                        CommonClient.logger.info("Zuma Deluxe process found!")

                        self.can_display_process_found_message = False
                        self.can_display_process_not_found_message = True

                    self.game_controller.update(dt)

                # Send Checked Locations
                checked_location_ids: List[int] = list()

                while len(self.game_controller.completed_locations_queue) > 0:
                    location: str = self.game_controller.completed_locations_queue.popleft()
                    try:
                        location_id: int = self.locations_names_to_ids[location]
                        checked_location_ids.append(location_id)
                    except KeyError:
                        print(location+ " doesnt exist")
                await self.check_locations(checked_location_ids)
                #Check Deathlink
                if self.game_controller.send_death:
                    await self.send_death(f"{self.player_names[self.slot]} could not survive the zumaic insanity")
                    self.game_controller.send_death = False

                # Check for Goal Completion
                if self.game_controller.goal_completed:
                    await self.send_msgs([
                        {
                            "cmd": "StatusUpdate",
                            "status": CommonClient.ClientStatus.CLIENT_GOAL
                        }
                    ])


def launch_zuma_deluxe_ap_client(*args) -> None:
    Utils.init_logging("ZumaDeluxeClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="Zuma Deluxe Client")

    parser.add_argument("url", nargs="?", help="Archipelago Connection URL")
    parser.add_argument('--name', default=None, help="Archipelago Slot Name")

    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)


    async def _main(_args):
        if not Utils.gui_enabled:
            raise RuntimeError("APQuest cannot be played without gui.")
        ctx: ZumaDeluxeContext = ZumaDeluxeContext(_args.connect, _args.password)
        ctx.auth = _args.name

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="ZumaDeluxeController")

        ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.just_fix_windows_console()

    asyncio.run(_main(args))

    colorama.deinit()

if __name__ == "__main__":
    launch_zuma_deluxe_ap_client(*sys.argv[1:])
