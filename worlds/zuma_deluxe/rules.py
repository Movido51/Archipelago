from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import *

if TYPE_CHECKING:
    from .world import ZumaDeluxe



def set_completion_condition(world: ZumaDeluxe) -> None:
    world.set_completion_rule(Has("Victory"))

