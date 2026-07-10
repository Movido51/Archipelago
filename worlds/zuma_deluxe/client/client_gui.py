from __future__ import annotations

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget




from typing import TYPE_CHECKING, Any, List,Tuple



#if TYPE_CHECKING:
from .client import ZumaDeluxeContext
from .client_gui_layouts import ZumaDeluxeTabLayout, CheatsAndList


class ZumaDeluxeManager(GameManager):
    base_title = "Archipelago Zuma Deluxe Client"
    ctx: ZumaDeluxeContext
    logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]

    zuma_deluxe_tab_layout: ZumaDeluxeTabLayout
    zuma_deluxe_tab_cheat_layout: CheatsAndList

    zuma_deluxe_tab: Widget
    zuma_deluxe_tab_cheat: Widget

    def build(self)-> Layout:
        container: Layout = super().build()
        self.zuma_deluxe_tab_layout = ZumaDeluxeTabLayout(self.ctx)
        self.zuma_deluxe_tab = self.add_client_tab("Zuma Deluxe", self.zuma_deluxe_tab_layout)

        self.zuma_deluxe_tab_cheat_layout = CheatsAndList(self.ctx)
        self.zuma_deluxe_tab_cheat = self.add_client_tab("Manual Zuma Deluxe", self.zuma_deluxe_tab_cheat_layout)
        return container




    def update_tabs(self)-> None:
        self.zuma_deluxe_tab_layout.update()


