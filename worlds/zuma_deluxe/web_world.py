from BaseClasses import Tutorial
from .options import option_groups
from worlds.AutoWorld import WebWorld


class ZumaDeluxeWebWorld(WebWorld):
    game = "Zuma Deluxe"

    theme = "stone"


    # setup guide

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Zuma Deluxe for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Movido51"],
    )

    # tutorials add

    tutorials = [setup_en]
    option_groups = option_groups
    #options_presets = options_presets



