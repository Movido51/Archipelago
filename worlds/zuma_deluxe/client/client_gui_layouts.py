from typing import List

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from ..gameControl.enums import ZumaDeluxeMode
from ..gameControl.game_controller import SectionState
from .client import ZumaDeluxeContext

class CheatLocation(BoxLayout):
    ctx: ZumaDeluxeContext
    layout_text: TextInput
    layout_button: Button
    def __init__(self, ctx: ZumaDeluxeContext):
        super().__init__(
            orientation = "horizontal",
            padding = "1dp",
            size_hint_y=None,
            height=40
        )
        self.ctx = ctx

        self.layout_text = TextInput(multiline=False)
        self.add_widget(self.layout_text)

        self.layout_button = Button(
            text="Send\nLocation",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_button)

        self.layout_button.bind(on_press=self.check_location)

    def check_location(self, _)-> None:
        location: str = self.layout_text.text
        print("sending location "+location)
        self.ctx.game_controller.completed_locations_queue.append(location)

class CheatItem(BoxLayout):
    ctx: ZumaDeluxeContext
    layout_text: TextInput
    layout_button: Button
    def __init__(self, ctx: ZumaDeluxeContext):
        super().__init__(
            orientation = "horizontal",
            padding = "1dp",
            size_hint_y=None,
            height=40
        )
        self.ctx = ctx

        self.layout_text = TextInput(multiline=False)
        self.add_widget(self.layout_text)

        self.layout_button = Button(
            text="Get\nItem",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_button)

        self.layout_button.bind(on_press=self.check_location)

    def check_location(self, _)-> None:
        location: str = self.layout_text.text
        print("sending location "+location)
        self.ctx.game_controller.received_items_queue.append(location)
class CheatLevelItems(BoxLayout):
    ctx: ZumaDeluxeContext
    layout_coin: Button
    layout_gap: Button
    layout_combo: Button
    layout_chain: Button
    #layout_coin: Button

    timer: Clock

    def __init__(self,ctx: ZumaDeluxeContext):
        super().__init__(
            orientation = "horizontal",
            padding = "1dp",
            size_hint_y=None,
            height=40
        )
        self.ctx = ctx

        self.layout_coin = Button(
            text="Toggle\nCoins",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_coin)

        self.layout_coin.bind(on_press=self.toggle_coins)

        self.layout_gap = Button(
            text="Toggle\nGaps",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_gap)

        self.layout_gap.bind(on_press=self.toggle_gaps)

        self.layout_combo = Button(
            text="Toggle\nCombos",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_combo)

        self.layout_combo.bind(on_press=self.toggle_combos)

        self.layout_chain = Button(
            text="Toggle\nChains",
            size_hint_x=0.1
        )
        self.add_widget(self.layout_chain)

        self.layout_chain.bind(on_press=self.toggle_chains)

        timer = Clock.schedule_interval(self.update, 1.0/10.0)

    def update(self, *_):
        if self.ctx.game_controller.game_actual_section is None:
            self.layout_coin.background_color = (0.1, 0.1, 0.1, 1.0)
            self.layout_gap.background_color = (0.1, 0.1, 0.1, 1.0)
            self.layout_combo.background_color = (0.1, 0.1, 0.1, 1.0)
            self.layout_chain.background_color = (0.1, 0.1, 0.1, 1.0)
        else:
            color = (0.0,0.0,0.5,1.0)
            if self.ctx.game_controller.have_coins():
                color = (0.0,0.5,0.0,1.0)
            else:
                color = (0.5, 0.0, 0.0, 1.0)
            self.layout_coin.background_color = color
            if self.ctx.game_controller.have_combos():
                color = (0.0,0.5,0.0,1.0)
            else:
                color = (0.5, 0.0, 0.0, 1.0)
            self.layout_combo.background_color = color
            if self.ctx.game_controller.have_gaps():
                color = (0.0,0.5,0.0,1.0)
            else:
                color = (0.5, 0.0, 0.0, 1.0)
            self.layout_gap.background_color = color
            if self.ctx.game_controller.have_chains():
                color = (0.0,0.5,0.0,1.0)
            else:
                color = (0.5, 0.0, 0.0, 1.0)
            self.layout_chain.background_color = color


    def toggle_coins(self,*_):
        self.ctx.game_controller.toggle_item_su_type("Coins")
    def toggle_gaps(self,*_):
        self.ctx.game_controller.toggle_item_su_type("Gaps")
    def toggle_combos(self,*_):
        self.ctx.game_controller.toggle_item_su_type("Combos")
    def toggle_chains(self,*_):
        self.ctx.game_controller.toggle_item_su_type("Chains")


class CheatsScroll(ScrollView):
    ctx: ZumaDeluxeContext

    layout: BoxLayout

    timer: Clock
    def __init__(self, ctx: ZumaDeluxeContext):
        super().__init__()
        self.ctx = ctx

        self.layout = BoxLayout(orientation = "vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))
        self.add_widget(self.layout)

        try:
            lister = [
                self.ctx.game_controller.game_state_in_level,
                self.ctx.game_controller.game_state_current_game_state,
                self.ctx.game_controller.game_state_current_level,
                self.ctx.game_controller.game_state_current_gauntlet_level,
                self.ctx.game_controller.game_state_gauntlet_board,

                self.ctx.game_controller.last_game_state_gauntlet_board,
                self.ctx.game_controller.game_difficulty,
                self.ctx.game_controller.game_state_current_game_mode,
                self.ctx.game_controller.game_actual_section,

                self.ctx.game_controller.game_actual_level
            ]
            for data in lister:
                self.layout.add_widget(
                    Label(
                        text="None" if data is None else str(data),
                        size_hint_y=None,
                        height=30
                    )
                )


        except Exception:
            import traceback
            traceback.print_exc()
            print("algo aslio mal")


        self.timer = Clock.schedule_interval(self.update,1.0/10.0)


    def update(self, *_):
        self.layout.clear_widgets()

        try:
            lister = [
                ["is in level",self.ctx.game_controller.game_state_in_level],
                ["state of game",self.ctx.game_controller.game_state_current_game_state],
                ["current level",self.ctx.game_controller.game_state_current_level],
                ["gauntlet help",self.ctx.game_controller.game_state_current_gauntlet_level],
                ["gauntlet board",self.ctx.game_controller.game_state_gauntlet_board],

                ["last gauntlet board",self.ctx.game_controller.last_game_state_gauntlet_board],
                ["difficulty",self.ctx.game_controller.game_difficulty],
                ["current mode",self.ctx.game_controller.game_state_current_game_mode],
                ["actual map",self.ctx.game_controller.game_actual_section],

                ["name of level",self.ctx.game_controller.game_actual_level]
            ]
            for data in lister:
                self.layout.add_widget(
                    Label(
                        text="None" if data is None else str(data),
                        size_hint_y=None,
                        height=30
                    )
                )


        except Exception:
            import traceback
            traceback.print_exc()
            print("algo aslio mal")


class ListOfPoints(ScrollView):
    ctx: ZumaDeluxeContext
    layout: BoxLayout
    button: Button

    timer:Clock

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__()
        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))
        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0/10.0)


    def update(self,*_):
        while self.ctx.game_controller.game_action_list:
            item = self.ctx.game_controller.game_action_list.popleft()
            self.add_message(item, 5)


    def add_message(self, text: str, time: int) -> None:
        label = Label(
            text=text,
            size_hint_y=None,
            height=30
        )

        self.layout.add_widget(label)

        Clock.schedule_once(
            lambda dt: self.layout.remove_widget(label),
            50.0
        )






class CheatsAndList(BoxLayout):
    ctx: ZumaDeluxeContext
    layout_content: BoxLayout
    layout_in_Loc_Send: CheatLocation
    layout_items_toggle: CheatLevelItems
    layout_in_List: CheatsScroll
    layout_points: ListOfPoints

    def __init__(self, ctx: ZumaDeluxeContext):
        super().__init__(orientation = "vertical", padding = "8dp")

        self.ctx = ctx
        self.layout_content = BoxLayout(orientation = "vertical", padding = "8dp")
        self.add_widget(self.layout_content)

        self.layout_in_Loc_Send = CheatLocation(ctx=ctx)
        self.layout_content.add_widget(self.layout_in_Loc_Send)
        self.layout_content.add_widget(CheatItem(ctx=ctx))

        self.layout_items_toggle = CheatLevelItems(ctx=ctx)
        self.layout_content.add_widget(self.layout_items_toggle)

        self.layout_in_List = CheatsScroll(ctx=ctx)
        self.layout_content.add_widget(self.layout_in_List)

        self.layout_points = ListOfPoints(ctx=ctx)
        self.layout_content.add_widget(self.layout_points)


class NotConnectedLayout(BoxLayout):
    ctx: ZumaDeluxeContext

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.12)

        self.ctx = ctx

        self.add_widget(
            Label(text="Please connect to an Archipelago server first to view this tab.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.12
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True

class ZumaDeluxeGoalLayout(BoxLayout):
    ctx: ZumaDeluxeContext

    layout_text: Label
    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation = "vertical",
            size_hint_y=0.1
        )
        self.ctx = ctx

        self.layout_text = Label(
            text="Waiting...",
            halign = "center"
        )
        self.add_widget(self.layout_text)

    def set_text(self, text: str):
        self.layout_text.text = text

    def update(self):
        goal_message: str =""

        required = self.ctx.game_controller.sun_idols_required
        total = self.ctx.game_controller.sun_idols_helpers
        gotten = self.ctx.game_controller.check_sun_idols()
        if gotten<required:
            goal_message += f"you got {gotten} out of {required} to goal "
        elif gotten<total:
            goal_message += f"you can goal with {gotten} you could collect {total-gotten} more to make it more easy"
        else:
            goal_message += "the son is at its closest"
        self.set_text(goal_message)

class LevelLocationsLayout(BoxLayout):
    ctx: ZumaDeluxeContext

    coins_location: Label
    combo_location: Label
    combo_max_location: Label
    gaps_location: Label
    chain_location: Label



    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation="horizontal",
            size_hint_x=0.5,
            size_hint_y=1
        )

        self.ctx = ctx

        self.coins_location = Label(
            text=f"Coins\n{self.ctx.game_controller.coins}   {self.ctx.game_controller.game_area_coins}",
            halign="center",
            size_hint_y=1
        )
        self.add_widget(self.coins_location)

        self.combo_location = Label(
            text=f"Total Combo\n{self.ctx.game_controller.combo}   {self.ctx.game_controller.game_area_total_combo}",
            halign="center",
            size_hint_y=1
        )
        self.add_widget(self.combo_location)

        self.combo_max_location = Label(
            text=f"Max Combo\n{self.ctx.game_controller.max_combo}   {self.ctx.game_controller.game_area_max_combo}",
            halign="center",
            size_hint_y=1
        )
        self.add_widget(self.combo_max_location)

        self.gaps_location = Label(
            text=f"Gaps\n{self.ctx.game_controller.gaps}   {self.ctx.game_controller.game_area_gaps}",
            halign="center",
            size_hint_y=1
        )
        self.add_widget(self.gaps_location)

        self.chain_location = Label(
            text=f"Chains\n{self.ctx.game_controller.chain}   {self.ctx.game_controller.game_area_chains}",
            halign="center",
            size_hint_y=1
        )
        self.add_widget(self.chain_location)

    def update(self):
        self.coins_location.text=f"Coins\n{self.ctx.game_controller.coins}   {self.ctx.game_controller.game_area_coins}"

        self.combo_location.text=f"Total Combo\n{self.ctx.game_controller.combo}   {self.ctx.game_controller.game_area_total_combo}"

        self.combo_max_location.text=f"Max Combo\n{self.ctx.game_controller.max_combo}   {self.ctx.game_controller.game_area_max_combo}"

        self.gaps_location.text=f"Gaps\n{self.ctx.game_controller.gaps}   {self.ctx.game_controller.game_area_gaps}"

        self.chain_location.text=f"Chains\n{self.ctx.game_controller.chain}   {self.ctx.game_controller.game_area_chains}"

    def show(self):
        self.opacity = 1.0
        self.size_hint_x = 1
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_x = None
        self.height = "0dp"
        self.disabled = True


class ZumaDeluxeLevelInfoLayout(BoxLayout):
    ctx: ZumaDeluxeContext

    layout_actual_map: Label
    layout_level_locations: BoxLayout

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation="horizontal",
            size_hint_y=0.2,

        )
        self.ctx =ctx
        text_map: str = "not playing"
        state = SectionState.NoneSelected
        if self.ctx.game_controller.game_actual_section is not None:
            text_map = "Is PLaying "+self.ctx.game_controller.game_actual_section.value+ "\n" +self.ctx.game_controller.game_actual_level
            state = self.ctx.game_controller.check_difficulty_state()


        self.layout_actual_map = Label(
            text=text_map,
            halign = "center",
            size_hint_x = 0.5,
            size_hint_y = 1
        )

        self.layout_level_locations = LevelLocationsLayout(ctx=ctx)
        self.layout_level_locations.hide()
        if state == SectionState.Unlocked:
            color = (0, 1, 0, 1)
            self.layout_level_locations.show()

        elif state == SectionState.Blocked:
            color = (1, 0, 0, 1)

        else:
            color = (0.1, 0.1, 0.1, 1)
        self.layout_actual_map.color = color
        self.add_widget(self.layout_actual_map)
        self.add_widget(self.layout_level_locations)

    def update(self,*_):
        text_map: str = "not playing"
        self.layout_level_locations.hide()
        state = [SectionState.NoneSelected]
        if self.ctx.game_controller.game_actual_section is not None:
            text_map = "Is PLaying "+self.ctx.game_controller.game_actual_section.value+ "\n" +self.ctx.game_controller.game_actual_level
            state = self.ctx.game_controller.check_difficulty_state()

        if SectionState.Unlocked in state:
            color = (0, 1, 0, 1)
            self.layout_level_locations.update()
            self.layout_level_locations.show()

        elif SectionState.Blocked in state:
            color = (1, 0, 0, 1)
        else:
            color = (0.1, 0.1, 0.1, 1)
        if SectionState.GoalUnlocked in state:
            color = lerp(color,(0.7, 0.7, 0.0, 1.0),0.5)
        elif SectionState.GoalLocked in state:
            color = lerp(color, (0.3, 0.3, 0.0, 1.0), 0.5)
        self.layout_actual_map.color = color
        self.layout_actual_map.text = text_map

class GauntletLayout(BoxLayout):
    ctx: ZumaDeluxeContext
    list_boards: List[Label]

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation = "vertical",
            padding = "10dp",
            size_hint_y=None
        )

        self.ctx = ctx
        self.bind(
            minimum_height=self.setter("height")
        )
        boards_state = self.ctx.game_controller.gauntlet_selection
        self.list_boards = []
        for board, state in boards_state.items():
            message = f" {board.value} is: {state}"
            label_board = Label(
                text=message,
                halign="center",
                size_hint_y=None,
                height=30

            )
            if SectionState.Unlocked in state:
                color = (0, 1, 0, 1)
            elif SectionState.Blocked in state:
                color = (1, 0, 0, 1)
            else:
                color = (0, 0, 0, 1)

            if SectionState.GoalLocked in state or SectionState.GoalIncomplete in state:
                color = lerp(color,(0.3, 0.3, 0, 1),0.5)
            elif SectionState.GoalUnlocked in state:
                color = lerp(color,(1.0, 1.0, 0, 1),0.5)


            label_board.color = color
            self.list_boards.append(label_board)
            self.add_widget(label_board)

    def update(self,*_):
        boards_state = self.ctx.game_controller.gauntlet_selection

        for i, (board, state) in enumerate(boards_state.items()):
            message = f"{board.value} is: {state}"
            self.list_boards[i].text = message

            if SectionState.Unlocked in state:
                color = (0, 1, 0, 1)
            elif SectionState.Blocked in state:
                color = (1, 0, 0, 1)
            else:
                color = (0, 0, 0, 1)

            if SectionState.GoalLocked in state or SectionState.GoalIncomplete in state:
                color = lerp(color, (0.3, 0.3, 0, 1), 0.5)
            elif SectionState.GoalUnlocked in state:
                color = lerp(color, (1.0, 1.0, 0, 1), 0.5)
            self.list_boards[i].color = color

class AdventureLayout(BoxLayout):
    ctx: ZumaDeluxeContext
    list_stages: List[Label]

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation = "vertical",
            padding = "10dp",
            size_hint_y=None
        )

        self.ctx = ctx
        self.bind(
            minimum_height=self.setter("height")
        )

        stages_state = self.ctx.game_controller.adventure_selection
        self.list_stages = []
        for stage, state in stages_state.items():
            message = f" {stage.value} is: {state}"
            label_stage = Label(
                text=message,
                halign = "center",
                size_hint_y=None,
                height=30

            )
            if SectionState.Unlocked in state:
                color = (0, 1, 0, 1)
            elif SectionState.Blocked in state:
                color = (1, 0, 0, 1)
            else:
                color = (0, 0, 0, 1)

            if SectionState.GoalLocked in state or SectionState.GoalIncomplete in state:
                color = lerp(color, (0.3, 0.3, 0, 1), 0.5)
            elif SectionState.GoalUnlocked in state:
                color = lerp(color, (1.0, 1.0, 0, 1), 0.5)
            label_stage.color = color
            self.list_stages.append(label_stage)
            self.add_widget(label_stage)

    def update(self,*_):
        stages_state = self.ctx.game_controller.adventure_selection

        for i, (stage, state) in enumerate(stages_state.items()):
            message = f"{stage.value} is: {state}"
            self.list_stages[i].text = message
            if SectionState.Unlocked in state:
                color = (0, 1, 0, 1)
            elif SectionState.Blocked in state:
                color = (1, 0, 0, 1)
            else:
                color = (0, 0, 0, 1)

            if SectionState.GoalLocked in state or SectionState.GoalIncomplete in state:
                color = lerp(color, (0.3, 0.3, 0, 1), 0.5)
            elif SectionState.GoalUnlocked in state:
                color = lerp(color, (1.0, 1.0, 0, 1), 0.5)
            self.list_stages[i].color = color



class ZumaDeluxeLevelsLayout(BoxLayout):
    ctx: ZumaDeluxeContext

    layout_header: BoxLayout
    layout_info: ScrollView
    button_adventure: Button
    button_gauntlet: Button
    layout_adventure: AdventureLayout
    layout_gauntlet: GauntletLayout
    actual_mode: ZumaDeluxeMode

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(
            orientation="vertical"
        )
        self.ctx = ctx
        mode: ZumaDeluxeMode = self.ctx.game_controller.mode
        if mode is None:
            mode = ZumaDeluxeMode.ADVENTURE
        if mode == ZumaDeluxeMode.BOTH:
            self.actual_mode = ZumaDeluxeMode.ADVENTURE
        else:
            self.actual_mode = mode

        #header
        self.layout_header = BoxLayout(
            orientation="horizontal",
            padding="10dp",
            size_hint_y=None,
            height=50
        )
        if mode == ZumaDeluxeMode.BOTH:
            self.button_adventure = Button(
                text = "Adventure",

            )

            self.button_adventure.bind(on_press=self.show_adventure)
            self.button_gauntlet = Button(
                text = "Gauntlet",
            )
            self.button_gauntlet.bind(on_press=self.show_gauntlet)
            self.button_adventure.background_color = (0.7, 0.7, 0.7, 1.0)
            self.button_gauntlet.background_color = (0.3, 0.3, 0.3, 1.0)
            self.layout_header.add_widget(self.button_adventure)
            self.layout_header.add_widget(self.button_gauntlet)
        else:
            label_mode = Label(
                text = self.actual_mode.value,
                halign="center"
            )
            self.layout_header.add_widget(label_mode)

        self.add_widget(self.layout_header)

        #content
        self.layout_info = ScrollView(

        )

        if mode != ZumaDeluxeMode.GAUNTLET:
            self.layout_adventure = AdventureLayout(ctx=ctx)

        if mode != ZumaDeluxeMode.ADVENTURE:
            self.layout_gauntlet = GauntletLayout(ctx=ctx)

        if self.actual_mode == ZumaDeluxeMode.ADVENTURE:
            self.layout_info.add_widget(self.layout_adventure)
        else:
            self.layout_info.add_widget(self.layout_gauntlet)

        self.add_widget(self.layout_info)


    def show_adventure(self,*_):
        if self.actual_mode == ZumaDeluxeMode.ADVENTURE:
            return
        self.actual_mode = ZumaDeluxeMode.ADVENTURE
        self.layout_info.clear_widgets()
        self.layout_info.add_widget(self.layout_adventure)
        self.layout_adventure.update()
        self.button_adventure.background_color = (0.7, 0.7, 0.7, 1.0)
        self.button_gauntlet.background_color = (0.3, 0.3, 0.3, 1.0)

    def show_gauntlet(self,*_):
        if self.actual_mode == ZumaDeluxeMode.GAUNTLET:
            return
        self.actual_mode = ZumaDeluxeMode.GAUNTLET
        self.layout_info.clear_widgets()
        self.layout_info.add_widget(self.layout_gauntlet)
        self.layout_gauntlet.update()
        self.button_gauntlet.background_color = (0.7, 0.7, 0.7, 1.0)
        self.button_adventure.background_color = (0.3, 0.3, 0.3, 1.0)

    def update(self):
        if self.actual_mode == ZumaDeluxeMode.ADVENTURE:
            self.layout_adventure.update()
        else:
            self.layout_gauntlet.update()


class ZumaDeluxeContent(BoxLayout):
    ctx: ZumaDeluxeContext

    layout_goal_progression: ZumaDeluxeGoalLayout
    layout_bag: Label
    layout_level_information: ZumaDeluxeLevelInfoLayout
    layout_world_levels: ZumaDeluxeLevelsLayout
    layout_messages: Label

    timer:Clock



    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(orientation="vertical", padding="5dp")
        self.ctx = ctx

        self.layout_goal_progression = ZumaDeluxeGoalLayout(ctx=ctx)
        self.add_widget(self.layout_goal_progression)

        self.layout_bag = Label(
            text = "Bag Not implemented",
            halign = "center",
            size_hint_y=None,
            height= Window.height * 0.05

        )
        self.add_widget(self.layout_bag)

        self.layout_level_information = ZumaDeluxeLevelInfoLayout(ctx=ctx)
        self.add_widget(self.layout_level_information)

        self.layout_world_levels = ZumaDeluxeLevelsLayout(ctx=ctx)
        self.add_widget(self.layout_world_levels)



        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)


    def update(self,*_)->None:
        try:
            self.layout_goal_progression.update()
            self.layout_level_information.update()
            self.layout_world_levels.update()
            #self.layout_messages.update()

        except Exception:
            import traceback

            with open("zuma_deluxe_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")



class ZumaDeluxeTabLayout(BoxLayout):
    ctx: ZumaDeluxeContext
    layout_content: BoxLayout

    layout_content: BoxLayout
    layout_content_zuma_deluxe: ZumaDeluxeContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ZumaDeluxeContext) -> None:
        super().__init__(orientation="vertical", padding="1dp")
        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)


        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.mode is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_zuma_deluxe"):
                self.layout_content_zuma_deluxe.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()


        if not len(self.layout_content.children):
            self.layout_content_zuma_deluxe = ZumaDeluxeContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_zuma_deluxe)

def lerp(v1, v2, t):
    return tuple(a * (1 - t) + b * t for a, b in zip(v1, v2))