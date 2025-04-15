"""objet unite"""

from random import randint

from plateau import Cellule
import config
import unitvar

dict_urss = [["BT-7M"], ["T-34"], ["KV-1"], ["SU-85"]]

dict_united_kingdom = [
    ["Crusader III"],
    ["Cromwell I"],
    ["Churchill III"],
    ["Achilles"],
]

dict_japan = [["Chi-Nu"], ["Chi-To"], ["Chi-Ri"], ["Na-To"]]

dict_italy = [["AB 43"], ["P40"], ["75/46 M43"], ["Breda 501"]]

dict_france = [
    ["AMX-13"],
    ["M4A4 SA50"],
    ["ARL 44"],
    ["Lorraine 155 Mle.50"],
]


dict_nation = {"USA": dict_usa, "Germany": dict_germany, "URSS": dict_urss}


class Unite:
    def __init__(self, infolist: list[str]):

        self.name = infolist[0]
        self.classe = infolist[1]

        self.max_health = int(infolist[2])
        self.health = self.max_health
        self.armor = int(infolist[3])

        self.speed = int(infolist[4])
        self.range = int(infolist[5])

        self.ammo = infolist[6]
        self.base_damage = int(infolist[7])
        self.base_penetration = int(infolist[8])
