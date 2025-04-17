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
    52,  # armor
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
    74,  # armor
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
    63,  # armor
    16.95,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 1},  # ammo
    180,  # base damage
    144,  # base penetration
]

list_urss = [T_50, T_34, KV_1, SU_85]  # list of urss units

Crusader_III = [
    "Crusader III",  # name
    "light",  # classe
    540,  # max health
    40,  # armor
    21.63,  # speed
    3,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    120,  # base damage
    86,  # base penetration
]

Cromwell_I = [
    "Cromwell I",  # name
    "medium",  # classe
    610,  # max health
    76,  # armor
    17.38,  # speed
    3,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    75,  # base damage
    110,  # base penetration
]

Churchill_III = [
    "Churchill III",  # name
    "heavy",  # classe
    920,  # max health
    177,  # armor
    8.75,  # speed
    3,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    135,  # base damage
    145,  # base penetration
]

Achilles = [
    "Achilles",  # name
    "destroyer",  # classe
    720,  # max health
    57,  # armor
    17.68,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    150,  # base damage
    143,  # base penetration
]

list_uk = [Crusader_III, Cromwell_I, Churchill_III, Achilles]

Chi_Nu = [
    "Chi-Nu",  # name
    "medium",  # classe
    630,  # max health
    50,  # armor
    15.74,  # speed
    3,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    125,  # base damage
    124,  # base penetration
]

Chi_To = [
    "Chi-To",  # name
    "medium",  # classe
    920,  # max health
    75,  # armor
    12.23,  # speed
    4,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    130,  # base damage
    155,  # base penetration
]

Chi_Ri = [
    "Chi-Ri",  # name
    "medium",  # classe
    1250,  # max health
    75,  # armor
    13.02,  # speed
    4,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    130,  # base damage
    155,  # base penetration
]

Na_To = [
    "Na-To",  # name
    "destroyer",  # classe
    420,  # max health
    25,  # armor
    16.05,  # speed
    5,  # range
    {"HE": 1, "HEAT": 1, "AP": 1, "APCR": 0},  # ammo
    150,  # base damage
    150,  # base penetration
]

list_japan = [Chi_Nu, Chi_To, Chi_Ri, Na_To]

AMX_ELC_BIS = [
    "AMX ELC BIS",  # name
    "light",  # classe
    490,  # max health
    25,  # armor
    26.63,  # speed
    4,  # range
    {"HE": 1, "HEAT": 1, "AP": 0, "APCR": 0},  # ammo
    240,  # base damage
    120,  # base penetration
]

AMX_13 = [
    "AMX 13",  # name
    "light",  # classe
    500,  # max health
    50,  # armor
    22.13,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    110,  # base damage
    108,  # base penetration
]

M4A1_FL10 = [
    "M4A1 FL10",  # name
    "medium",  # classe
    810,  # max health
    50,  # armor
    17.55,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    135,  # base damage
    148,  # base penetration
]

ARL_44 = [
    "ARL 44",  # name
    "heavy",  # classe
    950,  # max health
    120,  # armor
    16.14,  # speed
    4,  # range
    {"HE": 1, "HEAT": 0, "AP": 1, "APCR": 0},  # ammo
    240,  # base damage
    135,  # base penetration
]

list_france = [AMX_ELC_BIS, AMX_13, M4A1_FL10, ARL_44]
