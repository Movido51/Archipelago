

from .world import ZumaDeluxe as ZumaDeluxe
from worlds.LauncherComponents import Component, Type, components, launch, icon_paths

def launch_client_zd(*args:str) -> None:
    from .client.client import launch_zuma_deluxe_ap_client
    launch(launch_zuma_deluxe_ap_client, name = "ZumaDeluxeClient", args = args)

components.append(
    Component(
        "Zuma Deluxe Client",
        func = launch_client_zd,
        game_name="Zuma Deluxe",
        component_type=Type.CLIENT,
        supports_uri=True,
        icon="zuma_deluxe"
    )
)

icon_paths["zuma_deluxe"] = f"ap:{__name__}/client/assets/icon.png"


