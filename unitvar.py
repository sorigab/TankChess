"""
liste des variables pour chaque unite
"""

M24 = [
    "M24",  # name
    "light",  # classe
    550,  # max health
    38,  # armor
    27.19,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 1},  # ammo
    110,  # base damage
    96,  # base penetration
]

M4A3 = [
    "M4A3",  # name
    "medium",  # classe
    900,  # max health
    63,  # armor
    17.21,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 1},  # ammo
    115,  # base damage
    143,  # base penetration
]

T1E1 = [
    "T1E1",  # name
    "heavy",  # classe
    910,  # max health
    177,  # armor
    16.38,  # speed
    3,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    115,  # base damage
    128,  # base penetration
]

M10_GMC = [
    "M10 GMC",  # name
    "destroyer",  # classe
    470,  # max health
    57,  # armor
    17.40,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    115,  # base damage
    128,  # base penetration
]

list_usa = [M24, M4A3, T1E1, M10_GMC]  # list of usa units

sdkfz_234_2 = [
    "sd.kfz 234/2",  # name
    "light",  # classe
    580,  # max health
    50,  # armor
    25,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 1},  # ammo
    70,  # base damage
    100,  # base penetration
]

Pz_IV_F2 = [
    "Pz.IV F2",  # name
    "medium",  # classe
    630,  # max health
    80,  # armor
    17.53,  # speed
    5,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 1},  # ammo
    110,  # base damage
    110,  # base penetration
]

Pz_V_H1 =[
    "Pz.V H1",  # name
    "heavy",  # classe
    1200,  # max health
    100,  # armor
    11.90,  # speed
    4,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 1},  # ammo
    220,  # base damage
    145,  # base penetration
]

StuG_III_G = [
    "StuG III G",  # name
    "destroyer",  # classe
    460,  # max health
    80,  # armor
    18.68,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 1},  # ammo
    135,  # base damage
    150,  # base penetration
]

list_ger = [sdkfz_234_2, Pz_IV_F2, Pz_V_H1, StuG_III_G]  # list of germany units


T_50 = [
    "T-50",  # name
    "light",  # classe
    550,  # max health
    37,  # armor
    28.45,  # speed
    3,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    70,  # base damage
    90,  # base penetration
]

T_34 = [
    "T-34",  # name
    "medium",  # classe
    590,  # max health
    52,  # armor
    17.01,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    115,  # base damage
    125,  # base penetration
]

KV_1 = [
    "KV-1",  # name
    "heavy",  # classe
    840,  # max health
    110,  # armor
    10.18,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    160,  # base damage
    120,  # base penetration
]

SU_85 = [
    "SU-85",  # name
    "destroyer",  # classe
    460,  # max health
    45,  # armor
    16.95,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 1},  # ammo
    180,  # base damage
    144,  # base penetration
]

list_urss = [T_50, T_34, KV_1, SU_85]  # list of urss units