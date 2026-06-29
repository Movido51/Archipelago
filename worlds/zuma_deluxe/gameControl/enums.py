import enum

class ZumaDeluxeInLevel(enum.Enum):
    MENU = 0
    LEVEL = 1

class ZumaDeluxeGameState(enum.Enum):
    OTHER = -1
    MENU = 1762492
    PREPARING = 0
    PLAYING = 1
    CHANGE = 1866994645
    CLEAR_ADVENTURE = 61
    GAME_OVER_GAUNTLET = -2883723
    GAME_OVER_ADVENTURE = -11600032
    CLEAR_GAUNTLET = 1764884

class ZumaDeluxeMode(enum.Enum):
    ADVENTURE = 0
    GAUNTLET = 1
    BOTH = 2

class ZumaDeluxeAPGoals(enum.Enum):
    SPACE = 0
    RANDOM = 1

class ZumaDeluxeBoards(enum.Enum):
    SoD_1 = "Board 1 - Spiral of Doom"
    OT_2 = "Board 2 - Osprey Talon"
    RM_3 = "Board 3 - Riverbed Mosaic"
    BoE_4 = "Board 4 - Breath of Ethecatl"
    DV_5 = "Board 5 - Dark Vortex"
    SB_6 = "Board 6 - SwitchBack"
    LR_7 = "Board 7 - Long Range"
    WSA_8 = "Board 8 - When Spirals Attack"
    MD_9 = "Board 9 - Mud Slide"
    R_10 = "Board 10 - Rorschach"
    MoC_11 = "Board 11 - Mouth of Centeotl"
    SP_12 = "Board 12 - Snake Pit"
    SG_13 = "Board 13 - Sand Garden"
    LoTMS_14 = "Board 14 - Lair of The Mud Snake"
    LDP_15 = "Board 15 - Lan Ding Pad"
    AoT_16 = "Board 16 - Altar of Tlaloc"
    CoM_17 = "Board 17 - Code of Mixtec"
    SoQ_18 = "Board 18 - Shrine of Quetzalcoatl"
    MSpt_19 = "Board 19 - Mirror Serpent"
    ST_20 = "Board 20 - Sun Stone"
    ZE_21 = "Board 21 - Zumaic Exodus"
    Spc_22 = "Board 22 - Space"
    Rdm_23 = "Board 23 - Random"

class ZumaDeluxeStages(enum.Enum):
    ToZ_1 = "Stage 1 - Temple of Zukulkan 1"
    ToZ_2 = "Stage 2 - Temple of Zukulkan 2"
    ToZ_3 = "Stage 3 - Temple of Zukulkan 3"
    QQ_4 = "Stage 4 - Quetzal Quatl 1"
    QQ_5 = "Stage 5 - Quetzal Quatl 2"
    QQ_6 = "Stage 6 - Quetzal Quatl 3"
    PP_7 = "Stage 7 - Popo Poyolli 1"
    PP_8 = "Stage 8 - Popo Poyolli 2"
    PP_9 = "Stage 9 - Popo Poyolli 3"
    SSoZ_10 = "Stage 10 - Secret Shrine Of Zuma 1"
    SSoZ_11 = "Stage 11 - Secret Shrine Of Zuma 2"
    SSoZ_12 = "Stage 12 - Secret Shrine Of Zuma 3"
    SSoZ_13 = "Stage 13 - Space"


class ZumaDeluxeGauntletDifficulties(enum.Enum):
    RABBIT = "Rabbit"
    EAGLE = "Eagle"
    JAGUAR = "Jaguar"
    SUN_GOD = "Sun God"
