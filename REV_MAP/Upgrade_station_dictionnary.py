#Ceci est le dictionnaire de la station d'amélioration,
from email.headerregistry import UniqueUnstructuredHeader

from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.trigger_lists import Attribute, ObjectAttribute, Operation
from AoE2ScenarioParser.datasets.units import UnitInfo


#from pandas.core.common import not_none

food = 0
wood = 1
gold = 3
stone = 2
special_case = 2
special_case_2 = 3
special_case_3 = 4
special_case_4 = 5
special_case_5 =6
special_case_6 = 7
special_case_7 = 8
quantity_number_0 = 0
quantity_number_1 = 1
quantity_number_2 = 2
quantity_number_3 = 3

quantity_number_5000 = 5000
technologie_page_desc_icon = { #Ce dictionnaire est pour les tech qui font office d'ouverture de page, première élément les icônes; deuxièmes les descriptions
    1:[53,"Open the infantry upgrades and allow you to upgrade infantry units"],
    2:[45,"Open the cavalry upgrades and allow you to upgrade cavalry units"],
    3:[54,"Open the archery upgrades and allow you to upgrade ranged units"],
    4:[197,"Open the siege upgrades and allow you to upgrade siege units"],
    5:[210,"Open the economy upgrades and allow you to upgrade villagers and trade"],
    6:[4,"Go back to the technology category"],
}

technology_cost_icon = {
    #ID:[type coûts, Nombre de fois pour être dev, non attribuer, quantiter coûts 2, type coûts 3, quantiter resource 3, ICON]
    #--------------------------- Tech infantry
    1: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_010, 1, 44],
    2: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_018, 1, 124],
    3: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_029, 1, 176],
    4: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_030, 1, 22],
    5: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_031, 1, 114],
    6: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_051, 1, 107],
    7: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_059, 1, 67],
    8: [stone, 100, 5, None, Attribute.UNUSED_RESOURCE_060, 1, 91],
    #-------------------------------------------------------------- Tech cavalry
    9:  [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_123, 1, 45],
    10: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_061, 1, 23],
    11: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_066, 1, 110],
    12: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_69, 1, 106],
    13: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_70, 1, 114],
    14: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_71, 1, 10],
    15: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_72, 1, 19],
    16: [stone, 150, 5, None, Attribute.UNUSED_RESOURCE_73, 1, 91],
    #--------------------------------------------------------------- Tech Archery and GUN
    17: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_74, 1, 35],
    18: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_75, 1, 112],
    19: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_76, 1, 124],
    20: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_102, 1, 37],
    21: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_103, 1, 8],
    22: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_104, 1, 52],
    23: [stone, 150, 5, None, Attribute.UNUSED_RESOURCE_105, 1, 91],
    #--------------------------------------------------------------- # Siege
    24: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_106, 1, 18],
    25: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_107, 1, 126],
    26: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_108, 1, 220],
    27: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_109, 1, 107],
    28: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_110, 1, 25],
    29: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_111, 1, 86],
    30: [stone, 300, 3, None, Attribute.UNUSED_RESOURCE_112, 1, 100],
    31: [stone, 200, 4, None, Attribute.UNUSED_RESOURCE_113, 1, 60],
    #-------------------------- Eco / villagers
    32: [stone, 200, 5, None, Attribute.UNUSED_RESOURCE_114, 1, 3], #GOLD PRODUCTION
    33: [stone, 200, 5, None, Attribute.UNUSED_RESOURCE_115, 1, 71], #WOOD PRODUCTION
    34: [stone, 200, 5, None, Attribute.UNUSED_RESOURCE_116, 1, 171], #FOOD PRODUCTION
    35: [stone, 400, 3, None, Attribute.UNUSED_RESOURCE_117, 1, 217], # RELIC cost
    36: [stone, 450, 4, None, Attribute.UNUSED_RESOURCE_118, 1, 11], # GARRISON CAPACITY
    37: [stone, 250, 5, None, Attribute.UNUSED_RESOURCE_119, 1, 212], # POP BONUS
}


Techno_xs = {
100: ("void Script_XS_{s}_{u}_{player}() {{" #TRUE OR FALSE CASE
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        #xsEffectAmount(cModResource, cAttributeStone, cSetAttribute, 50, -1);
    "}}"
        ),
101: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL_CASE
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
    "}}"
        ),
102: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 2
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
    "}}"
        ),
103: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 3
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
      
        "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute_2}, {valeur_XS_3}, {player});"
    "}}" ),

104: ("void Script_XS_{s}_{u}_{player}() {{" # Special CASE 4
        "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS}, {player});"
      
      "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS}, {player});"
    "}}"
        ),
105: ("void Script_XS_{s}_{u}_{player}() {{" # Special CASE 4
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur_2}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
    "}}"
        ),
106: ("void Script_XS_{s}_{u}_{player}() {{"
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
      "xsEffectAmount({operateur}, {unit_ID}, {attribute_3}, {valeur_XS}, {player});"
      
    "}}"
        ),
107: ("void Script_XS_{s}_{u}_{player}() {{"  # SPECIAL CASE 6
          "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS_2}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS_3}, {player});"
      
          "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute}, {valeur_XS_4}, {player});"
          "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute}, {valeur_XS_4}, {player});"

          "xsEffectAmount({operateur}, {unit_ID}, {attribute_2}, {valeur_XS}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_2}, {attribute_2}, {valeur_XS_2}, {player});"
          "xsEffectAmount({operateur}, {unit_ID_3}, {attribute_2}, {valeur_XS_3}, {player});"
      
          "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute_2}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute_2}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute_2}, {valeur_XS_4}, {player});"
      
         "xsEffectAmount({operateur}, {unit_ID_4}, {attribute_3}, {valeur_XS_5}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_5}, {attribute_3}, {valeur_XS_5}, {player});"
      "xsEffectAmount({operateur}, {unit_ID_6}, {attribute_3}, {valeur_XS_5}, {player});"
          "}}"),
108: ("void Script_XS_{s}_{u}_{player}() {{" #SPECIAL CASE 2
        "xsEffectAmount({operateur}, {unit_ID}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_2}, {attribute}, {valeur_XS}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_3}, {attribute}, {valeur_XS}, {player});"
      
        "xsEffectAmount({operateur_2}, {unit_ID_4}, {attribute}, {valeur_XS_4}, {player});"
        "xsEffectAmount({operateur_2}, {unit_ID_5}, {attribute}, {valeur_XS_4}, {player});"
       "xsEffectAmount({operateur_2}, {unit_ID_6}, {attribute}, {valeur_XS_4}, {player});"
      
      "xsEffectAmount({operateur}, {unit_ID_4}, {attribute_2}, {valeur_XS_5}, {player});"
        "xsEffectAmount({operateur}, {unit_ID_5}, {attribute_2}, {valeur_XS_5}, {player});"
       "xsEffectAmount({operateur}, {unit_ID_6}, {attribute_2}, {valeur_XS_5}, {player});"
    "}}"
        ),
#["cAddAttribute",904,,,],
    # Amélioration infantrie
    1: ["cAddAttribute", 906, 9, "256*4 + 4", False],  # Infantrie attaque upgrade
    2: ["cAddAttribute", 906, 0, 20, False],           # Amélioration HP
    3: ["cMulAttribute", 906, 10, 0.90, False],        # Vitesse d'attaque
    4: ["cAddAttribute", 906, 8, "256*4 + 2", True, 906, "256*3 + 2"],  # Armure
    5: ["cAddAttribute", 906, 109, 20, False],         # Régénération des PV
    6: ["cAddAttribute", 906, 22, 0.20, False],        # Radius
    7: ["cMulAttribute", 906, 5, 1.15, False],         # Vitesse de déplacement
    8: ["cMulAttribute", 906, 101, 0.85, False],       # Temps d'entrainement
    # Amélioration cavalerie
    9:  ["cAddAttribute", 912, 9, "256*4 + 2", False,],  # Attaque
    10: ["cAddAttribute", 912, 8, "256*4 + 3", True, 912, "256*3 + 3"],  # Armure (duplicata renommé)
    11: ["cMulAttribute", 912, 0, 1.20, False],        # Point de vie
    12: ["cAddAttribute", 912, 12, 0.50, False],       # Portée maximale
    13: ["cAddAttribute", 912, 109, 30, False],        # Régénération PV
    14: ["cMulAttribute", 912, 5, 1.10, False],        # Vitesse de déplacement
    15: ["cAddAttribute", 912, 22, 0.60, False],        # Radius
    16: ["cMulAttribute", 912, 101, 0.90, False],      # Temps d'entrainement

    # Archer tech
    17: ["cAddAttribute", 900, 9, "256 * 3 + 2", special_case, 936, "256 * 3 + 2", 944, "256 * 3 + 2"],
    18: ["cMulAttribute", 900, 10, 0.85, special_case, 936, 0.85, 944, 0.85],
    19: ["cAddAttribute", 900, 0, 10, special_case, 936, 10, 944, 10],
    20: ["cAddAttribute", 900, 12, 2, special_case_2, 936, 2, 944, 2, 1],
    21: ["cAddAttribute", 900, 22, 0.10, special_case, 936, 0.10, 944, 0.10],
    22: ["cAddAttribute", 900, 102, 2, special_case_2, 936, 2, 944, 2, 107],
    23: ["cMulAttribute", 900, 101, 0.90, special_case, 936, 0.90, 944, 0.90],
    # Siege upgrade
    24: ["cAddAttribute", 955, 9, "256 * 3 + 2", special_case, 913, "256 * 4 + 2", 954, "256 * 3 + 2"], #Damage siege
    25: ["cMulAttribute", 913, 10, 0.85, special_case, 954, 0.85, 955, 0.85], # Reload time
    26: ["cMulAttribute", 913, 5, 1.15, special_case, 42, 1.15, 955, 1.15], # Move speed
    27: ["cMulAttribute", 42, 13, 1.15, False], # Temps de déploiement trebs
    28: ["cAddAttribute", 913, 12, 1, special_case_7, 954, 1, 955, 1, 1258, 422, 548, "cSetAttribute", 0, 8, "256*4 + 1"], #Max range et armure pour bélier
    29: ["cMulAttribute", 913, 22, 1.10, special_case, 954, 1.10, 955, 1.10], # AOE
    30: ["cAddAttribute", 913, 102, 1, special_case_6, 954, 1, 955, 1, 107, 1258, 422, 548, 0, 0, 235, "cSetAttribute"], # Nombre de projectile + PV
    31: ["cMulAttribute", 913, 101, 0.90, special_case, 42, 0.10, 955, 0.90], # Temps de construction
    # Eco tech
    #xsEffectAmount(cModResource, cAttributeStone, cSetAttribute, 50, -1);
    32: ["cAddAttribute", 904, None, None, None],
    33: ["cAddAttribute", 904, None, None, None],
    34: ["cAddAttribute", 904, None, None, None],
    35: ["cAddAttribute", 904, None, None, None],
    36: ["cAddAttribute", 904, None, None, None],
    37: ["cAddAttribute", 904, None, None, None],
}

Techno_message = {
    #----------------- Tech infantry
    1: "Upgrade infantry damage <cost>.\n Give +4 damages to your infantries units.\nYou can make this upgrade 3 times.",
    2: "Upgrade infantry hitpoint <cost>.\n Give +20 hitpoints to your infantries units.\nYou can make this upgrade 3 times.",
    3: "Upgrade infantry attack speed <cost>\n Infantries attack 10% faster.\nYou can make this upgrade 3 times.",
    4: "Upgrade infantry armor <cost>\n Give +2 armor and piercing armor to your infantries units.\nYou can make this upgrade 3 times.",
    5: "Upgrade infantry health regeneration <cost>.\n Infantry heal +20 hp per minutes.\nYou can make this upgrade 3 times.",
    6: "Upgrade infantry radius attack <cost>.\n Infantry gain 0.20 radius attack.\nYou can make this upgrade 3 times.",
    7: "Upgrade infantry movement speed <cost>.\nInfantry move 15% faster\nYou can make this upgrade 3 times.",
    8: "Reduce the training time of infantry units <cost>.\n Infantry units (Unique units included) are produced 10% faster.\nYou can make this upgrade 3 times.",
    #-----------------------------------------------------------
    9:  "Upgrade cavalry attack <cost>.\n Give +2 attacks to your cavalry units (elephant included)\nYou can make this upgrade 3 times.",
    10: "Upgrade cavalry armor <cost>.\n Give +3 armors and piercing armor to cavalry units (elephant included)\nYou can make this upgrade 3 times.",
    11: "Upgrade cavalry hitpoints <cost>.\n Cavalry units gain 20% hitpoints (elephant included).\nYou can make this upgrade 3 times.",
    12: "Upgrade cavalry attack range <cost>.\n Give 0.50 range to cavalry attack (elephant included)\nYou can make this upgrade 3 times.",
    13: "Upgrade cavalry regeneration <cost>.\n Cavalry Heal 30 HP per minutes(elephant included).\nYou can make this upgrade 3 times.",
    14: "Upgrade cavalry movement speed <cost>.\n Cavalry move 10% faster(elephant included)\nYou can make this upgrade 3 times.",
    15: "Upgrade cavalry line of sight <cost>.\n Cavalry gain 0.60 attack radius (elephant included)\nYou can make this upgrade 3 times.",
    16: "Reduce the training time of cavalry units <cost>\nCavalry units are trained 10% faster (elephant and unique units included).\nYou can make this upgrade 3 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    17: "Upgrade ranged units damage <cost>.\nGive +2 attacks to every range units\nYou can make this upgrade 3 times.",
    18: "Upgrade ranged units attack speed <cost>.\nRanged units attack 15% faster.\nYou can make this upgrade 3 times.",
    19: "Upgrade ranged units hitpoints <cost>\nRanged units gain +10 HP.\nYou can make this upgrade 3 times.",
    20: "Upgrade ranged units range <cost>\nRanged units gain +2 range and line of sight\nYou can make this upgrade 3 times.",
    21: "Upgrade ranged units attack radius <cost>\nRanged units gain 0.10 radius attack.\nYou can make this upgrade 3 times.",
    22: "Give +2 projectile to ranged units <cost>.\nRanged units gain +2 projectile.\nYou can make this upgrade 3 times.",
    23: "Reduce ranged units training time <cost>\nRanged units (unique units included) are train 10% faster.\nYou can make this upgrade 3 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    24: "Upgrade siege attack <cost>\n Give +2 attacks to every siege units.\nYou can make this upgrade 3 times.",
    25: "Upgrade siege attack speed <cost>\n Siege weapon attack 15% faster.\nYou can make this upgrade 3 times.",
    26: "Upgrade siege movement speed <cost>\n Siege weapon move 15% faster.\nYou can make this upgrade 3 times.",
    27: "Upgrade trebuchet unpack speed <cost>\n Trebuchet unpack 15% faster.\nYou can make this upgrade 3 times.",
    28: "Upgrade siege ranged and ram HP <cost>\n Sieges weapons gain +1 range except rams who gain +1 melee armor instead .\nYou can make this upgrade 3 times.",
    29: "Upgrade siege blast <cost>\nSiege weapons gain +10% blastwidth.\nYou can make this upgrade 3 times.",
    30: "Give +1 projectile to siege weapons <cost>\nSiege weapons gain +1 projectile except rams who gain 235 HP instead.\nYou can make this upgrade 3 times.",
    31: "Reduce siege construction time <cost>\nSiege weapon are builded 10% faster(Unique units included).\nYou can make this upgrade 4 times.",
    #---------------------------------------------------------------------------------------------------------------------------------------------
    32: "Upgrade Gold production from relics <cost>.\nYour relic produce +40 gold per minute.\nYou can make this upgrade 5 times.",
    33: "Upgrade Wood production from relics <cost>\nYour relic produce +40 wood per minute.\nYou can make this upgrade 5 times.",
    34: "Upgrade Food production from relics <cost>\nYour relic produce +40 food per minute.\nYou can make this upgrade 5 times.",
    35: "Reduce the cost of relics <cost>.\nReduce the price of relics by 30%.\nYou can make this upgrade 3 times.",
    36: "Upgrade garrison capacity of monastery <cost>\n Monastery can hold +10 relics in garrison.\nYou can make this upgrade 4 times.",
    37: "Increase population population <cost>\nYou gain +50 population.\nYou can make this upgrade 3 times."
}

###########################################################################################################################################################################################################################################
#
#
#
#
#
#                                                                   Séparation, la suite c'est le TRADE WORKSHOP
#                                                                   Separation, next part is the TRADE WORKSHOP
#
#
#
#
#
###########################################################################################################################################################################################################################################
not_available_msg= "This spot has no mission, but it could be yours mission here\n Contact Maselia via steam or discord"
INT_DICT_DESC = {

}
for k in range(1, 10):
    INT_DICT_DESC[k] = [not_available_msg, quantity_number_5000]

ADV_DICT_DESC = {
    1: [
        "Advance evergreen exposition, Author: Maselia.\n This is the very first mission made for this map, mostly classic units but you will have to handle a few custom units and boss.\nStarting relics = 4, starting RES 800W, 800F, 800G, 1000S.",
        quantity_number_1
    ],

}

for k in range(2, 10):
    ADV_DICT_DESC[k] = [not_available_msg, quantity_number_5000]

EXP_DICT_DESC = {

}

for k in range(2, 10):
    EXP_DICT_DESC[k] = [not_available_msg, quantity_number_5000]



