"""objet unite"""

from random import randint

from plateau import Cellule
import config
import unitvar

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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"""<Unite {self.name}
        {self.health}/{self.max_health}
        {self.armor}
        {self.speed}
        {self.range}
        {self.ammo}
        {self.base_damage}/{self.base_penetration}>"""

    def shoot(self, target: Unite, ammo):
        if ammo == "HE":
            if target.armor >= self.base_penetration:
        
        elif ammo == "AP":
            
        elif ammo == "HEAT":
            
        elif ammo == "APCR":