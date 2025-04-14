"""objet unite"""

import random

from plateau import Cellule
import config.py

dict_usa = {
    0 : ["M24"],
    1 : ["M4A2"],
    2 : ["T1E1"],
    3 : ["M10 GMC"],
}

dict_germany = {
    0 : ["Puma"],
    1 : ["Panther"],
    2 : ["Tiger"],
    3 : ["Maus"],
    4 : ["Leopard"],
    
    
}
    

dict_nation = {
    "USA": dict_usa,
    "Germany": 1,
    "URSS": 2
}

class Unite():
    def __init__(self, infolist: list[str]):
        
        self.name = infolist[0]
        self.classe = infolist[1]
        
        self.max_health = int(infolist[2])
        self.health = self.max_health
        self.armor = int(infolist[3])
        
        self.speed = int(infolist[4])
        self.range = int(infolist[5])
        
        