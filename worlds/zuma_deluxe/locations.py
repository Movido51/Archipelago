from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import ZumaDeluxe

class ZumaDeluxeLocation(Location):
    game = "Zuma Deluxe"

def get_location_names_with_ids(world: ZumaDeluxe, location_names: list[str]) -> dict[str, int | None]:
    return {location_name: world.location_name_to_id[location_name] for location_name in location_names}


