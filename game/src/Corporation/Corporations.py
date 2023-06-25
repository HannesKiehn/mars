from __future__ import annotations
from typing import TYPE_CHECKING

from game.src.Tag import Tag

if TYPE_CHECKING:
    from game.src.Player import Player


# TODO Corp Effects
class Corporations:
    def __init__(self) -> None:
        pass

    IDS_BASEGAME = [
        "credicor",
        "ecoline",
        "helion",
        "miningGuild",
        "interplanetaryCinematics",
        "inventrix",
        "phobolog",
        "tharsisRepublic",
        "thorgate",
        "unitedNationsMarsInitiative",
    ]
    IDS_CORPORATE_ERA = ["teractor", "saturnSystems"]
    IDS = IDS_BASEGAME + IDS_CORPORATE_ERA

    @staticmethod
    def play(corporationId: str, player: Player):
        player.corporation = corporationId
        match corporationId:
            case "credicor":
                player.cash = 57
            case "ecoline":
                player.cash = 36
                player.plants = 3
                player.PlantsProd = 2
                player.playTag(Tag.PLANT)
            case "helion":
                player.cash = 42
                player.heatProd = 3
                player.playTag(Tag.SPACE)
            case "miningGuild":
                player.cash = 30
                player.steel = 5
                player.steelProd = 1
                player.playTags([Tag.BUILDING, Tag.BUILDING])
            case "interplanetaryCinematics":
                player.cash = 30
                player.steel = 20
                player.playTag(Tag.BUILDING)
            case "inventrix":
                player.cash = 45
                player.playTag(Tag.SCIENCE)
            case "phobolog":
                player.cash = 23
                player.titanium = 10
                player.playTag(Tag.SPACE)
            case "tharsisRepublic":
                player.cash = 40
                player.playTag(Tag.BUILDING)
            case "thorgate":
                player.cash = 48
                player.powerProd = 1
                player.playTag(Tag.POWER)
            case "unitedNationsMarsInitiative":
                player.cash = 40
                player.playTag(Tag.EARTH)
            case "teractor":
                player.cash = 60
                player.playTag(Tag.EARTH)
            case "saturnSystems":
                player.cash = 42
                player.titaniumProd = 1
                player.playTag(Tag.JOVIAN)
