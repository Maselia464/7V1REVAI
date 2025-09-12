# Le script pose les fonctions de base de la carte
#C'est à dire:
# - Les coordonées des drapeaux pour placer les tours
# - Les coordonnées des drapeaux M pour les pierres
# - Les statistiques de base des joueurs (Workrate, resource, diplomatie, vision)
# - Le menu pour choisir la carte.
#---------------------------------------------------------------------------------------------
from selectors import SelectorKey

quantity_number_0 = 0
quantity_number_3 = 3
quantity_number_4 = 4
quantity_number_8 = 8
quantity_number_9 = 9
quantity_number_10 = 10
quantity_number_32 = 32
quantity_number_35 = 32
quantity_number_40 = 40
quantity_number_60 = 60
quantity_number_200 = 200
quantity_number_400 = 400
quantity_number_500 = 500
quantity_number_50 = 50
quantity_number_2500 = 2500
quantity_number_7500 = 7500
quantity_number_20000 = 20000
ATTACK_PRIORITY = 128
Timer_20s= 20
u = 1
reset_list = []
FLAG_O_ID = 2011
FLAG_P_ID = 2012
FLAG_ATHENIAN_2 = 2257
FLAG_ATHENIAN_3 = 2258
SPARTAN_FLAG_2= 2260
Non_convertible_goat = 2381
FEUDAL_BARRACKS = 20
CASTLE_BARRACKS = 132
IMP_BARRACKS = 498
CASTLE_ARCHERY_CAMP = 14
IMP_ARCHERY_CAMP = 10
CASTLE_STABLE = 101
IMP_STABLE = 153
FEUDAL_MONASTERY = 30
CASTLE_MONASTERY = 31
IMP_MONASTERY = 32
from email.headerregistry import UniqueUnstructuredHeader
from gc import enable
from idlelib.rpc import objecttable
from pickle import FALSE
from uuid import UUID

from AoE2ScenarioParser.datasets.effects import attributes
from AoE2ScenarioParser.objects.support import area
from packaging.markers import Operator

from logging import disable
from AoE2ScenarioParser.datasets.trigger_lists import *
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# Information of unit/building/hero and tech IDs
from AoE2ScenarioParser.datasets.projectiles import ProjectileInfo
from AoE2ScenarioParser.datasets.object_support import Civilization, StartingAge
from AoE2ScenarioParser.datasets.object_support import *
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.techs import TechInfo
# Information about player IDs
from AoE2ScenarioParser.datasets.players import PlayerId, PlayerColorId, ColorId
from AoE2ScenarioParser import scenarios
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
# Information about terrain IDs
from AoE2ScenarioParser.datasets.terrains import TerrainId

from AoE2ScenarioParser.datasets.trigger_lists import \
    DiplomacyState, Operation, ButtonLocation, PanelLocation, \
    TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, \
    Comparison, ObjectAttribute, Attribute, UnitAIAction, \
    AttackStance, ObjectType, ObjectClass, DamageClass, \
    HeroStatusFlag, Hotkey, BlastLevel, TerrainRestrictions, \
    ColorMood, ObjectState, SecondaryGameMode, ChargeType, \
    ChargeEvent, CombatAbility, FogVisibility, GarrisonType, \
    OcclusionMode, ProjectileHitMode, ProjectileVanishMode, \
    UnitTrait, ProjectileSmartMode, Age, ActionType, VictoryTimerType

from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.support import area
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager

from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.scenarios.support.data_triggers import DataTriggers

from AoE2ScenarioParser.objects.managers.option_manager import OptionManager

from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from unicodedata import category
#Dictionnaire pour le script
from AoE2ScenarioParser.objects.support.area import Area
from Upgrade_station_dictionnary import technologie_page_desc_icon, technology_cost_icon, special_case_3, special_case_7
from Upgrade_station_dictionnary import Techno_message
from Upgrade_station_dictionnary import Techno_xs
from Upgrade_station_dictionnary import INT_DICT_DESC
from Upgrade_station_dictionnary import ADV_DICT_DESC
from Upgrade_station_dictionnary import EXP_DICT_DESC

from data_tools import get_unit_reference_id
from data_tools import create_display_text_trigger
from data_tools import create_spawn_trigger
from data_tools import create_complex_toggle_trigger
from data_tools import create_toggle_trigger_range
from data_tools import modify_attributes_trigger
from data_tools import get_blacksmith_zone
from data_tools import calculate_square_bounds
from special_tech import special_tech_civ
from Begining_animation import begining_animation
import os



os.environ['TCL_LIBRARY'] = r'C:\Users\redma\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\redma\AppData\Local\Programs\Python\Python313\tcl\tk8.6'
P1 = PlayerId.ONE
XS_general_ID = [900,936,944,906,912,947,955,913,923]
melee_general_ID = [906,912,947]
import tkinter as tk
from tkinter import filedialog, Variable
import subprocess  # Si tu veux lancer des scripts externes

Liste_joueur = {
    1: PlayerId.ONE,
    2: PlayerId.TWO,
    3: PlayerId.THREE,
    4: PlayerId.FOUR,
    5: PlayerId.FIVE,
    6: PlayerId.SIX,
    7:PlayerId.SEVEN,
    8:PlayerId.EIGHT
}
P8=PlayerId.EIGHT
timer_quantity_1 = 5
X_coord_close = {
    0: [77, 57],
    1: [76, 58],
    2: [74, 60],
    3: [73, 61],
    4: [72, 62],
    5: [71, 63],
    6: [75, 59],

}
Lister_couleur = {
    1: "BLUE",
    2: "RED",
    3: "GREEN",
    4: "YELLOW",
    5: "AQUA",
    6: "PURPLE",
    7: "GRAY",
    8: "ORANGE",
}
input_path = "C:\\Users\\redma\\Games\\Age of Empires 2 DE\\76561198382316787\\resources\\_common\\scenario\\REV 7 VS 1 AI MAP BUILD.aoe2scenario"
output_path = "C:\\Users\\redma\\Games\\Age of Empires 2 DE\\76561198382316787\\resources\\_common\\scenario\\REV 7 VS 1 AI MAP BETA.aoe2scenario"

# ----- Récupération des coordonées des drapeaux et stockage dans tableau
scenario = AoE2DEScenario.from_file(input_path)
scenario_uuid = scenario.uuid
area = Area.from_uuid(scenario_uuid)
trigger_manager = scenario.trigger_manager
results = {}
timer_quantity_1 = 5
Script_rule = "void rule_for_friendly_fire() {"
for p in range (1,8):
    player=Liste_joueur[p]
    Script_rule +=f"xsEffectAmount(cSetAttribute, 900, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 936, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 944, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 912, 44, 4, {player});"
    Script_rule += f"xsEffectAmount(cSetAttribute, 947, 44, 4, {player});"
Script_rule += f"xsEffectAmount(cSetAttribute, 190, 44, 4, 1);"
Script_rule += f"xsEffectAmount(cSetAttribute, 190, 44, 4, 2);"
Script_rule += "}"

Balancing = trigger_manager.add_trigger(
            name=f"Equilibrage général",
            enabled=True,
            looping=False,
)
Balancing.new_condition.timer(
    timer=timer_quantity_1,
)
Balancing.new_effect.script_call(
    message=Script_rule,
)
short_cut_rock_remove =trigger_manager.add_trigger(
    name="Rock short cut block Unlock",
    enabled=True,
    looping=False,
)
short_cut_rock_remove.new_condition.objects_in_area(
    source_player=P8,
    quantity=1,
    inverted=True,
    object_list=BuildingInfo.BLACKSMITH.ID,
    **area.select_entire_map().to_dict(),
)
short_cut_rock_remove.new_effect.remove_object(
    source_player=PlayerId.GAIA,
    object_list_unit_id=OtherInfo.SVAN_TOWER.ID,
    **area.select_entire_map().to_dict(),
)
for b in range (len(X_coord_close)):
    short_cut_rock_remove.new_effect.create_object(
        source_player=PlayerId.GAIA,
        object_list_unit_id=OtherInfo.SVAN_TOWER.ID,
        location_x=X_coord_close[b][0],
        location_y=X_coord_close[b][1],
    )
# 💡 Liste des types d’éléments à analyser (tu peux ajouter ce que tu veux ici)
unit_type_ids = [
    BuildingInfo.CITY_GATE_NORTH_TO_SOUTH.ID,
    BuildingInfo.CITY_GATE_NORTHWEST_TO_SOUTHEAST.ID,
    BuildingInfo.CITY_GATE_WEST_TO_EAST.ID,
    BuildingInfo.CITY_GATE_SOUTHWEST_TO_NORTHEAST.ID,
]

# 🔍 On récupère toutes les unités qui matchent l’un des types ci-dessus
units = scenario.unit_manager.get_all_units()
filtered_units = [u for u in units if u.unit_const in unit_type_ids]
list_ref = [u.reference_id for u in filtered_units]
close_gate = trigger_manager.add_trigger(
            name="Close P8 gate",
            enabled=True,
            looping=False,
)
close_gate.new_effect.lock_gate(
    selected_object_ids=list_ref,
)



LOS_torch =trigger_manager.add_trigger(
    name="Line_of_sight torch",
    enabled=True,
    looping=False,
)
LOS_torch.new_effect.modify_attribute(
    source_player=P1,
    quantity=10,
    object_attributes=ObjectAttribute.LINE_OF_SIGHT,
    object_list_unit_id=OtherInfo.TORCH_A.ID,
    operation=Operation.SET,
)
LOS_torch.new_effect.modify_attribute(
    source_player=P1,
    quantity=10,
    object_attributes=ObjectAttribute.LINE_OF_SIGHT,
    object_list_unit_id=OtherInfo.TORCH_B.ID,
    operation=Operation.SET,
)


Building_list = [IMP_MONASTERY,CASTLE_MONASTERY,FEUDAL_MONASTERY,IMP_STABLE,CASTLE_STABLE,IMP_ARCHERY_CAMP,CASTLE_ARCHERY_CAMP,BuildingInfo.BARRACKS.ID,FEUDAL_BARRACKS, CASTLE_BARRACKS,
                 IMP_BARRACKS,BuildingInfo.ARCHERY_RANGE.ID,BuildingInfo.STABLE.ID,BuildingInfo.SIEGE_WORKSHOP.ID,
                 BuildingInfo.MONASTERY.ID,BuildingInfo.CASTLE.ID,BuildingInfo.BLACKSMITH.ID,BuildingInfo.UNIVERSITY.ID,BuildingInfo.MONASTERY.ID,
                 BuildingInfo.MARKET.ID]
workrate_building = trigger_manager.add_trigger(
    name="workrate building",
    enabled=True,
    looping=False,
)
for work_building in range(len(Building_list)):
    edited_building = Building_list[work_building]
    for p in range(1,8):
        player = Liste_joueur[p]
        workrate_building.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=edited_building,
            object_attributes=ObjectAttribute.WORK_RATE,
            quantity=quantity_number_8,
            operation=Operation.MULTIPLY,
        )
        workrate_building.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=edited_building,
            object_attributes=ObjectAttribute.DEAD_UNIT_ID,
            quantity=edited_building,
            operation=Operation.SET,
        )
        workrate_building.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=edited_building,
            object_attributes=ObjectAttribute.TRAIN_TIME,
            quantity=quantity_number_0,
            operation=Operation.SET,
        )
################################################################################
#
#                       Fonction récupération des coordonnées de drapeau
#
################################################################################
# flag_utils.py
from AoE2ScenarioParser.datasets.other import OtherInfo
from uuid import UUID


def get_flag_positions(scenario):
    FLAG_O_ID = 2011
    FLAG_P_ID = 2012

    Flag_list = [
        ("FLAG_A", OtherInfo.FLAG_A.ID),
        ("FLAG_B", OtherInfo.FLAG_B.ID),
        ("FLAG_C", OtherInfo.FLAG_C.ID),
        ("FLAG_G", OtherInfo.FLAG_G.ID),
        ("FLAG_H", OtherInfo.FLAG_H.ID),
        ("FLAG_K", OtherInfo.FLAG_K.ID),
        ("FLAG_O", FLAG_O_ID),
        ("FLAG_P", FLAG_P_ID),
        ("DONJON", BuildingInfo.DONJON.ID),
    ]

    flag_positions = {
        f"coordinate_{name}": {} for name, _id in Flag_list
    }

    id_to_name = {flag_id: name for name, flag_id in Flag_list}

    for units in scenario.unit_manager.units:
        for u in units:
            if isinstance(u, UUID):
                continue
            if u.unit_const in id_to_name:
                flag_name = id_to_name[u.unit_const]
                key = f"coordinate_{flag_name}"
                p = u.player
                if p not in flag_positions[key]:
                    flag_positions[key][p] = []
                flag_positions[key][p].append((int(u.x), int(u.y)))

    return flag_positions

################################################################################
#
#                       Fonction de la Tente D pour raccourcie
#
################################################################################
army_tent_d_function = trigger_manager.add_trigger(
    name="Army tent D stats",
    enabled=True,
    looping=False,
)
replace_flag = trigger_manager.add_trigger(
    name="Military tent D replace flag",
    enabled=True,
    looping=False,
)
replace_flag.new_effect.replace_object(
        **area.select_entire_map().to_dict(),
        source_player=PlayerId.SEVEN,
        target_player=player,
        object_list_unit_id=FLAG_ATHENIAN_2,
        object_list_unit_id_2=BuildingInfo.ARMY_TENT_E.ID
)
for p in range(1,8):
    player = Liste_joueur[p]
    replace_flag.new_effect.replace_object(
        **area.select_entire_map().to_dict(),
        source_player=player,
        target_player=player,
        object_list_unit_id=FLAG_ATHENIAN_3,
        object_list_unit_id_2=BuildingInfo.ARMY_TENT_D.ID
    )
    Tent_list = [BuildingInfo.ARMY_TENT_D.ID,BuildingInfo.ARMY_TENT_E.ID]
    for list in range(len(Tent_list)):
        army_tent_d_function.new_effect.modify_attribute(
            source_player=player,
            object_attributes=ObjectAttribute.COMBAT_ABILITY,
            object_list_unit_id=Tent_list[list],
            quantity=quantity_number_32,
            operation=Operation.SET,
        )
        army_tent_d_function.new_effect.modify_attribute(
            source_player=player,
            object_attributes=ObjectAttribute.DEAD_UNIT_ID,
            object_list_unit_id=Tent_list[list],
            quantity=Tent_list[list],
            operation=Operation.SET,
        )
        army_tent_d_function.new_effect.modify_attribute(
            source_player=player,
            object_attributes=ObjectAttribute.TRAIN_TIME,
            object_list_unit_id=Tent_list[list],
            quantity=quantity_number_0,
            operation=Operation.SET,
        )
        army_tent_d_function.new_effect.modify_attribute(
            source_player=player,
            object_attributes=ObjectAttribute.LINE_OF_SIGHT,
            object_list_unit_id=Tent_list[list],
            quantity=quantity_number_40,
            operation=Operation.SET,
        )
army_tent_d_script = trigger_manager.add_trigger(
        name=f"script XS function",
        enabled=True,
        looping=False,
    )
army_tent_d_script.new_condition.timer(
    timer=quantity_number_10,
)
units = UnitInfo.unique_units(include_chronicles=True)

ID_LIST=[906,900,936,944,912,955,913,918]
p = 1
L = 0
for list in range (len(ID_LIST)):
    unit_id = ID_LIST[list]
    if p != PlayerId.EIGHT:
        building_shrine = BuildingInfo.ARMY_TENT_D.ID
        player = Liste_joueur[p]
    elif p == PlayerId.EIGHT and L != 1:
        print(f"Valeur de L {L}")
        building_shrine_List = [BuildingInfo.ARMY_TENT_E.ID]
        building_shrine = building_shrine_List[L]
        player = PlayerId.SEVEN
        L += 1
    p += 1
    script_argument = f"void setupSpeedAura{unit_id}{building_shrine}()"
    script_argument += """ {
        xsTaskAmount(0, 5);
        xsTaskAmount(1, 1);
        xsTaskAmount(2, 12);
        xsTaskAmount(3, 0);
        xsTaskAmount(4, 5);
        xsTaskAmount(5, 6);
        xsTaskAmount(6, 4);
    """
    script_argument += f"xsTask({building_shrine}, 155, {unit_id}, {player});"
    script_argument += "}"
    army_tent_d_script.new_effect.script_call(
        message=script_argument,
    )


################################################################################
#
#                       Désactivation des sélections objets du décord
#
################################################################################
disable_building_selection = trigger_manager.add_trigger(
    name="Disable building selection",
    enabled=True,
    looping=False,
)
for p in range (1,8):
    DISABLE_BUILDING_LIST =[BuildingInfo.DOCK.ID,BuildingInfo.HUT_A.ID,
                            BuildingInfo.HUT_B.ID,BuildingInfo.HUT_C.ID,BuildingInfo.HUT_D.ID,BuildingInfo.HUT_E.ID,
                            BuildingInfo.HUT_F.ID,BuildingInfo.HUT_G.ID,BuildingInfo.MINING_CAMP.ID,BuildingInfo.SEA_TOWER.ID,BuildingInfo.GUARD_TOWER.ID,
                            BuildingInfo.MILL.ID,BuildingInfo.PAVILION_C.ID,BuildingInfo.HOUSE.ID,UnitInfo.VILLAGER_MALE.ID,UnitInfo.VILLAGER_FEMALE.ID]
    player = Liste_joueur[p]
    for list in range (len(DISABLE_BUILDING_LIST)):
        building_to_handle=DISABLE_BUILDING_LIST[list]
        disable_building_selection.new_effect.disable_object_selection(
            source_player=player,
            **area.select_entire_map().to_dict(),
            object_list_unit_id=building_to_handle,
        )
        disable_building_selection.new_effect.disable_object_deletion(
            source_player=player,
            **area.select_entire_map().to_dict(),
            object_list_unit_id=building_to_handle,
        )
################################################################################
#
#                       Désactivation des objets à construire
#
################################################################################
timer_condition = quantity_number_9
for p in range (1,8):
    player = Liste_joueur[p]
    disable_building_build = trigger_manager.add_trigger(
        name=f"Disable building player {player}",
        enabled = True,
        looping= False,
    )
    disable_tech = trigger_manager.add_trigger(
        name=f"Disable building player {player}",
        enabled=True,
        looping=False,
    )
    timer_condition = timer_condition + 1
    disable_building_build.new_condition.timer(
        timer=timer_condition
    )
    disable_tech.new_condition.timer(
        timer=timer_condition
    )
    DISABLE_BUILDING_CONSTRUCTION = [BuildingInfo.HOUSE.ID,BuildingInfo.MILL.ID,BuildingInfo.LUMBER_CAMP.ID,BuildingInfo.MINING_CAMP.ID,BuildingInfo.DOCK.ID,
                                     BuildingInfo.FARM.ID, BuildingInfo.MARKET.ID,BuildingInfo.BLACKSMITH.ID,BuildingInfo.UNIVERSITY.ID,
                                     BuildingInfo.WONDER.ID,BuildingInfo.MONASTERY.ID,BuildingInfo.TOWN_CENTER.ID,BuildingInfo.BARRACKS.ID,
                                     BuildingInfo.ARCHERY_RANGE.ID,BuildingInfo.STABLE.ID,BuildingInfo.SIEGE_WORKSHOP.ID,BuildingInfo.PALISADE_WALL.ID,BuildingInfo.PALISADE_GATE,
                                     BuildingInfo.WATCH_TOWER.ID,BuildingInfo.GUARD_TOWER.ID,BuildingInfo.ID,BuildingInfo.KEEP.ID,BuildingInfo.CASTLE.ID,BuildingInfo.KREPOST.ID,
                                     BuildingInfo.DONJON.ID,BuildingInfo.STONE_WALL.ID,UnitInfo.TRADE_CART_FULL.ID,UnitInfo.TRADE_CART_EMPTY.ID]
    DISABLE_TECH_RESEARCH = [TechInfo.GUARD_TOWER.ID,TechInfo.HEATED_SHOT.ID,TechInfo.BOMBARD_TOWER.ID,TechInfo.MASONRY.ID,TechInfo.SVAN_TOWERS.ID,TechInfo.YASAMA.ID,
                             TechInfo.TREADMILL_CRANE.ID,TechInfo.FORTIFIED_WALL.ID,TechInfo.REDEMPTION.ID,TechInfo.EUPSEONG.ID,TechInfo.MURDER_HOLES.ID,TechInfo.ARROWSLITS.ID,TechInfo.WHEELBARROW.ID,TechInfo.HAND_CART.ID,
                             TechInfo.CRENELLATIONS.ID,TechInfo.HILL_FORTS.ID,TechInfo.FORTIFIED_BASTIONS.ID,TechInfo.SVAN_TOWERS.ID,TechInfo.TIGUI.ID,TechInfo.CARRACK.ID,TechInfo.THALASSOCRACY.ID,TechInfo.STRONGHOLD.ID,
                             TechInfo.GREAT_WALL.ID,TechInfo.SILK_ROAD.ID,TechInfo.ATHEISM.ID,TechInfo.YASAMA.ID,TechInfo.KAMANDARAN.ID,TechInfo.DETINETS.ID]
    for list in range(len(DISABLE_BUILDING_LIST)):
        disable_building_build.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=DISABLE_BUILDING_LIST[list],
            enabled=False,
        )
    for list in range(len(DISABLE_TECH_RESEARCH)):
        disable_tech.new_effect.enable_disable_technology(
            source_player=player,
            technology=DISABLE_TECH_RESEARCH[list],
            enabled=False,
        )
###################################################################################################################################################
#
#
#                                                           Respawn des objets de décoration sur la carte
#
#
###################################################################################################################################################
Props_respawn=[OtherInfo.TREE_PINE_FOREST.ID,OtherInfo.TREE_OAK_FOREST.ID,OtherInfo.ROCK_1.ID,OtherInfo.ROCK_2.ID,2009,2008,OtherInfo.TREE_DEAD.ID]
props_respawn_trigger = trigger_manager.add_trigger(
    name="Props respawn trigger",
    enabled=True,
    looping=False,
)
for list in range (len(Props_respawn)):
    object_change=Props_respawn[list]
    props_respawn_trigger.new_effect.modify_attribute(
        source_player=PlayerId.GAIA,
        object_attributes=ObjectAttribute.DEAD_UNIT_ID,
        object_list_unit_id=object_change,
        quantity=object_change,
    )
###################################################################################################################################################
#
#
#                                                           Station d'amélioration
#
#
###################################################################################################################################################
################################################# RELIC tech ##############################
for u in range (1,8):
        quantity_number_1 = 1
        quantity_number_2 = 2500
        quantity_number_3 = 26
        cost_1 = 3
        button_location_v = 10
        player = Liste_joueur[u]
        # Fonction changer le cheval en relique gaia
        relic_buy1= trigger_manager.add_trigger(
            name=f"Première activation {player}",
            enabled=True,
            looping=False,
        )
        relic_buy2 = trigger_manager.add_trigger(
            name=f"Cheval en relique gaia {player}",
            enabled=True,
            looping=True,
        )
        # Fonction enlever le trigger de changement cheval en gaia
        relic_buy3 = trigger_manager.add_trigger(
            name=f"Enlever le trigger de changement cheval en gaia {player}",
            enabled=False,
            looping=True,
        )
        # Variable utilisé par Fonction Relique
        trigger_remove_second = f"Cheval en relique gaia {player}"
        trigger_remove_third = f"Enlever le trigger de changement cheval en gaia {player}"
        trigger_id_second = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_second), None)
        trigger_id_third = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_remove_third), None)
        # Acheter RELIQUE
        # Conditon de Fonction de Création de Cheval pour Relique
        relic_buy1.new_condition.timer(
            timer = Timer_20s,
        )
        relic_buy1.new_effect.enable_disable_object(
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            enabled=True,
        )
        relic_buy1.new_effect.change_train_location(
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            object_list_unit_id_2=BuildingInfo.MONASTERY.ID,
            source_player=player,
            button_location=button_location_v,
        )
        relic_buy1.new_effect.modify_attribute(
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
            object_attributes=ObjectAttribute.ICON_ID,
            quantity=quantity_number_3,
            operation=Operation.SET,
        )
        relic_buy1.new_effect.change_object_cost(
            resource_1=cost_1,
            resource_1_quantity=quantity_number_500,
            source_player=player,
            object_list_unit_id=UnitInfo.HORSE_A.ID,
        )
        relic_buy1.new_effect.change_object_description(
            source_player=player,
            message="Buy a new relic <cost>\n You cab buy a new relic to gain more resource from your monastery\n you can reduce the price of relics or upgrade the production rate at your fortress in the economic section",
            object_list_unit_id=UnitInfo.HORSE_A.ID,
        )
        relic_buy2.new_condition.objects_in_area(
            object_list=UnitInfo.HORSE_A.ID,  # Cheval A
            source_player=player,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
            quantity=quantity_number_1,
        )
        relic_buy2.new_effect.change_ownership(
            object_list_unit_id=UnitInfo.HORSE_A.ID,  # cheval A
            source_player=player,
            target_player=PlayerId.GAIA,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
        )
        relic_buy2.new_effect.activate_trigger(
            trigger_id=trigger_id_third,
        )
        relic_buy3.new_condition.timer(
            timer=quantity_number_1,
        )
        relic_buy3.new_effect.replace_object(
            object_list_unit_id=UnitInfo.HORSE_A.ID,  # cheval A
            source_player=PlayerId.GAIA,
            **area.select_entire_map().to_dict(),
            # fonction pour sélectionner toute la carte, fonctionne avec tous les effets et condition qui ont besoin d'avoir une selection
             object_list_unit_id_2=OtherInfo.RELIC.ID,  # Relique Gaia
        )
        relic_buy3.new_effect.deactivate_trigger(
            trigger_id=trigger_id_third,
        )
###########################################################################################

Autorisation_tech = {}
bouton_techno = ["None",7,8,11,12,13,15]
for u in range (1,7):
    for p in range (1,8):
        quantity_number_1 = 0
        quantity_number_2= 1
        player = Liste_joueur[p]
        tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{u}")  # <-- OK ici
        tech_id = tech_obj.ID
        bouton_placement = bouton_techno[u]
        print(f"Tech ID {u} = {tech_id}")
######################################################################################################
#############################-Cette partie gère les tech qui font office de page######################
######################################################################################################
        Autorisation_tech[u] = trigger_manager.add_trigger(
            name=f"Activation des technologies pour changer de page {u}",
            enabled=True,
            looping=False,
        )
        if u != 6: #Ici on à besoin que la tech 6 qui fait office de retour arrière reste innactive
            Autorisation_tech[u].new_effect.enable_disable_technology(
                source_player=player,
                enabled=True,
                technology=tech_id,
            )
        else:
            Autorisation_tech[u].new_effect.enable_disable_technology(
                source_player=player,
                enabled=False,
                technology=tech_id,
            )
        Autorisation_tech[u].new_effect.change_technology_location(
            source_player=player,
            button_location=bouton_placement,
            object_list_unit_id_2=BuildingInfo.FORTRESS.ID,
            technology=tech_id,
        )
        Autorisation_tech[u].new_effect.change_technology_icon(
            source_player=player,
            technology=tech_id,
            quantity=technologie_page_desc_icon[u][quantity_number_1]
        )
        Autorisation_tech[u].new_effect.change_technology_description(
            source_player=player,
            technology=tech_id,
            message=technologie_page_desc_icon[u][quantity_number_2]
        )
#Il faut faire une vérification des techs qui ajoute 1 valeur variable pour déterminer les technologies
Recherche_check = {} #Check la tech qui est rechercher
for u in range (1,7):
    for p in range (1,8):
        player = Liste_joueur[p]
        if u != 6:
            quantity = u
            vrai_ou_faux = False #Tant qu'on arrive pas à la tech qui gère le changement de page, on désactive les autres tech au moment de la recherche.
            vrai_ou_faux_2 = True
        else:
            quantity = 0
            vrai_ou_faux = True #Quand on arrive à la tech qui fait le retour arrière alors on réactive les technologies de page.
            vrai_ou_faux_2 = False
        tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{u}")  # <-- OK ici
        tech_id = tech_obj.ID
        Recherche_check[u] = trigger_manager.add_trigger(
            name=f"Vérifie la techno {tech_id} pour {player}",
            enabled=True,
            looping=True,
        )
        Recherche_check[u].new_condition.research_technology(
            technology=tech_id,
            source_player=player,
        )
        Recherche_check[u].new_effect.modify_resource(
            quantity=quantity,
            operation=Operation.SET,
            source_player=player,
            tribute_list=Attribute.UNUSED_RESOURCE_008,
        )
        for d in range(1, 7):  # Désactivation des techno
            tech_obj_2 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{d}")  # <-- OK ici
            tech_id_2 = tech_obj_2.ID
            if d != 6:
                Recherche_check[u].new_effect.enable_disable_technology(
                    technology=tech_id_2,
                    enabled=vrai_ou_faux,
                    source_player=player,
                )
            else:
                Recherche_check[u].new_effect.enable_disable_technology(
                    technology=tech_id_2,
                    enabled=vrai_ou_faux_2,
                    source_player=player,
                )


#Ensuite il faut catégoriser les techs par valeur variable
Les_tech = {}
#print(f" PRE U: {u}")
for u in range (1,6):
    c = u + 1
#    print(f"U: {u}")
    quantity_number_25 = 0
    quantity_number_26 = 1
    if u == 1:
        min_boucle = 1
        maxi_boucle = 9
    elif u == 2:
        min_boucle = 9
        maxi_boucle = 17
    elif u == 3:
        min_boucle = 17
        maxi_boucle = 24
    elif u == 4:
        min_boucle = 24
        maxi_boucle = 32
    else:
        min_boucle = 32
        maxi_boucle = 38
    for p in range (1,8):
        player = Liste_joueur[p]
        Les_tech[u] = trigger_manager.add_trigger(  # End of the plugin
            name=f"Pour les technologies {u} joueur {player}",
            enabled=True,
            looping=True,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity= u,
            inverted=False,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_008,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=c,
            inverted=True,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_008,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=quantity_number_25,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_498,
            inverted=False,
        )
        Les_tech[u].new_condition.accumulate_attribute(
            quantity=quantity_number_26,
            source_player=player,
            attribute=Attribute.UNUSED_RESOURCE_498,
            inverted=True,
        )
        comptage = 0
#       print(f"Min Boucle: {min_boucle} MAX BOUCLE {maxi_boucle}")
        for s in range (min_boucle,maxi_boucle):
            comptage = comptage + 1
            y = comptage + 6
            l = s - 1
            tech_obj = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # <-- OK ici
            tech_id = tech_obj.ID
            quantity_number_1 = 0
            quantity_number_2 = 1
            quantity_number_3 = 2
            quantity_number_4 = 3
            quantity_number_5 = 4
            quantity_number_6 = 5
            quantity_number_7 = 6
            Les_tech[u].new_effect.enable_disable_technology(
                enabled=True,
                technology=tech_id,
                source_player=player,
            )
            Les_tech[u].new_effect.change_technology_location(
                source_player=player,
                button_location=comptage,
                object_list_unit_id_2=BuildingInfo.FORTRESS.ID,
                technology=tech_id,
            )
            Les_tech[u].new_effect.change_technology_description(
                source_player=player,
                technology=tech_id,
                message=Techno_message[s],
            )
            Les_tech[u].new_effect.change_technology_cost(
                technology=tech_id,
                source_player=player,
#---------------- Type de coûts
                resource_1=technology_cost_icon[s][quantity_number_1],
                resource_2=technology_cost_icon[s][quantity_number_5],
#----------------- Quantité des coûts
                resource_1_quantity=technology_cost_icon[s][quantity_number_2],
                resource_2_quantity=technology_cost_icon[s][quantity_number_6],
#----------------- Resource non utilisée pour limiter l'upgrade
            )
            Les_tech[u].new_effect.change_technology_icon(
                source_player=player,
                technology=tech_id,
                quantity=technology_cost_icon[s][quantity_number_7],
            )
            print(f"Valeur ICONE{technology_cost_icon[s][quantity_number_7]}")
        Les_tech[u].new_effect.modify_resource(
            tribute_list=Attribute.UNUSED_RESOURCE_498,
            quantity=quantity_number_26,
            source_player=player,
            operation=Operation.SET

        )
###############################################################################################################
#                                                                                                             #
#                                                                                                             #
#                                    Séparation pour la lecture                                               #
#                                    On passe aux conditions de chaque tech                                   #
#                                                                                                             #
#                                                                                                             #
###############################################################################################################
        comptage = 0
        check_tech = {}
        for s in range(min_boucle, maxi_boucle):
            comptage = comptage + 1
            y = comptage + 6
            quantity_number_7 = 0
            quantity_number_8 = 1
            quantity_number_9 = 2
            quantity_number_10 = 3
            quantity_number_11 = 4
            quantity_number_12 = 5
            quantity_number_13 = 6
            quantity_number_14 = 101
            quantity_number_15 = 100
            quantity_number_16 = 102
            quantity_number_17 = 7
            quantity_number_18 = 8
            quantity_number_19 = 9
            quantity_number_20 = 103
            quantity_number_21 = 104
            quantity_number_22= 105
            quantity_number_23 = 106
            quantity_number_24 = 50
            quantity_number_107 = 107
            quantity_number_30 = 10
            quantity_number_31 = 11
            quantity_number_32 = 12
            quantity_number_33 = 13
            quantity_number_34 = 14
            quantity_number_35 = 15
            quantity_number_36 = 16
            quantity_number_108 = 108
            quantity_number_true = Techno_xs[s][quantity_number_11]
            if_true = 1
            special_case= 2
            special_case_2= 3
            special_case_3 = 4
            special_case_4 =5
            special_case_5 =6
            special_case_6 = 7
            special_case_7 = 8
            tech_obj_2 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # <-- OK ici
            tech_id_2 = tech_obj_2.ID
            print(quantity_number_true)
            if quantity_number_true == if_true :
                Script_XS = Techno_xs[quantity_number_14].format(s=s, u=u, player=player,operateur=Techno_xs[s][quantity_number_7],unit_ID_2=Techno_xs[s][quantity_number_12],unit_ID=Techno_xs[s][quantity_number_8],attribute=Techno_xs[s][quantity_number_9],valeur_XS=Techno_xs[s][quantity_number_10],valeur_XS_2=Techno_xs[s][quantity_number_13])
            elif quantity_number_true == special_case:
                Script_XS = Techno_xs[quantity_number_16].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18])
            elif quantity_number_true == special_case_2:
                Script_XS = Techno_xs[quantity_number_20].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_19],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18])
# -----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_3:
                Script_XS = Techno_xs[quantity_number_21].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10])
# -----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_4:
                Script_XS = Techno_xs[quantity_number_22].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_13],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_17],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_18])
#-----------------------------------------------------------------------------------------------------------------
            elif quantity_number_true == special_case_5:
                Script_XS = Techno_xs[quantity_number_23].format(s=s, u=u, player=player,# ICI !!!!!!!!!!
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_12],
                                                                 attribute_3=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],)
            elif quantity_number_true == special_case_6:
                Script_XS = Techno_xs[quantity_number_107].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_36],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],
                                                                 unit_ID_4=Techno_xs[s][quantity_number_30],
                                                                 unit_ID_5=Techno_xs[s][quantity_number_31],
                                                                 unit_ID_6=Techno_xs[s][quantity_number_32],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_19],
                                                                 attribute_3=Techno_xs[s][quantity_number_34],
                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_2=Techno_xs[s][quantity_number_13],
                                                                 valeur_XS_3=Techno_xs[s][quantity_number_18],
                                                                 valeur_XS_4=Techno_xs[s][quantity_number_33],
                                                                 valeur_XS_5=Techno_xs[s][quantity_number_35],)
            elif quantity_number_true == special_case_7:
                Script_XS = Techno_xs[quantity_number_108].format(s=s, u=u, player=player,
                                                                 operateur=Techno_xs[s][quantity_number_7],
                                                                 operateur_2=Techno_xs[s][quantity_number_32],
                                                                 unit_ID=Techno_xs[s][quantity_number_8],
                                                                 unit_ID_2=Techno_xs[s][quantity_number_12],
                                                                 unit_ID_3=Techno_xs[s][quantity_number_17],

                                                                 unit_ID_4=Techno_xs[s][quantity_number_19],
                                                                 unit_ID_5=Techno_xs[s][quantity_number_30],
                                                                 unit_ID_6=Techno_xs[s][quantity_number_31],

                                                                 attribute=Techno_xs[s][quantity_number_9],
                                                                 attribute_2=Techno_xs[s][quantity_number_34],

                                                                 valeur_XS=Techno_xs[s][quantity_number_10],
                                                                 valeur_XS_4=Techno_xs[s][quantity_number_33],
                                                                 valeur_XS_5=Techno_xs[s][quantity_number_35],)
                print(Script_XS)


            else:
                Script_XS = Techno_xs[quantity_number_15].format(s=s,u=u,player=player,operateur=Techno_xs[s][quantity_number_7],unit_ID=Techno_xs[s][quantity_number_8],attribute=Techno_xs[s][quantity_number_9],valeur_XS=Techno_xs[s][quantity_number_10])
            check_tech[y] = trigger_manager.add_trigger(
                name=f"vérifie si la tech à été recherché {tech_id_2}",
                enabled=True,
                looping=True,
            )
            check_tech[y].new_condition.research_technology(
                technology=tech_id_2,
                source_player=player,
            )
            check_tech[y].new_condition.accumulate_attribute(
                quantity=u,
                inverted=False,
                source_player=player,
                attribute=Attribute.UNUSED_RESOURCE_008, #Ceci est la condition qui check les tech ne te fait pas avoir
            )
            check_tech[y].new_condition.accumulate_attribute(
                quantity=c,
                inverted=True,
                source_player=player,
                attribute=Attribute.UNUSED_RESOURCE_008,
            )
            if s not in [32,33,34,35,36,37]:
                check_tech[y].new_effect.script_call(
                    message=Script_XS,
                )
            elif s == 32:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.RELIC_GOLD_PRODUCTION_RATE,
                    source_player=player,
                    quantity=quantity_number_60,
                    operation=Operation.ADD,
                )
            elif s == 33:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.RELIC_WOOD_PRODUCTION_RATE,
                    source_player=player,
                    quantity=quantity_number_40,
                    operation=Operation.ADD,
                )
            elif s == 34:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.RELIC_FOOD_PRODUCTION_RATE,
                    source_player=player,
                    quantity=quantity_number_40,
                    operation=Operation.ADD,
                )
            elif s == 35:
                quantity_number_10_BIS = 10
                quantity_number_13_BIS = 13
                check_tech[y].new_effect.modify_attribute(
                    object_list_unit_id=UnitInfo.HORSE_A.ID,
                    quantity=quantity_number_10_BIS,
                    object_attributes=ObjectAttribute.GOLD_COSTS,
                    operation=Operation.MULTIPLY,
                    source_player=player,
                )
                check_tech[y].new_effect.modify_attribute(
                    object_list_unit_id=UnitInfo.HORSE_A.ID,
                    quantity=quantity_number_13_BIS,
                    object_attributes=ObjectAttribute.GOLD_COSTS,
                    operation=Operation.DIVIDE,
                    source_player=player,
                )
            elif s == 36:
                quantity_number_10_BIS = 10
                check_tech[y].new_effect.modify_attribute(
                    object_list_unit_id=BuildingInfo.MONASTERY.ID,
                    quantity=quantity_number_10_BIS,
                    object_attributes=ObjectAttribute.GARRISON_CAPACITY,
                    operation=Operation.ADD,
                    source_player=player,
                )
            else:
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.POPULATION_HEADROOM,
                    source_player=player,
                    quantity=quantity_number_50,
                    operation=Operation.ADD,
                )
                check_tech[y].new_effect.modify_resource(
                    tribute_list=Attribute.BONUS_POPULATION_CAP,
                    source_player=player,
                    quantity=quantity_number_50,
                    operation=Operation.ADD,
                )
            check_tech[y].new_effect.enable_disable_technology(
                technology=tech_id_2,
                source_player=player,
                enabled=True,
            )

Retour_0 = {}
for p in range (1,8):
    player = Liste_joueur[p]
    quantity_number_1 = 1
    quantity_number_2 = 0
    Retour_0[p] = trigger_manager.add_trigger(
        name="Désactivation des triggers",
        enabled=True,
        looping=True,
    )
    Retour_0[p].new_condition.accumulate_attribute(
        quantity=quantity_number_2,
        source_player=player,
        attribute=Attribute.UNUSED_RESOURCE_008,
        inverted=False,
    )
    Retour_0[p].new_condition.accumulate_attribute(
        quantity=quantity_number_1,
        source_player=player,
        attribute=Attribute.UNUSED_RESOURCE_008,
        inverted=True,
    )
    Retour_0[p].new_effect.modify_resource(
        tribute_list=Attribute.UNUSED_RESOURCE_498,
        quantity=quantity_number_2,
        source_player=player,
        operation=Operation.SET
    )
    for y in range (7,15):
        tech_obj_3 = getattr(TechInfo, f"BLANK_TECHNOLOGY_{y}")  # Faire une double conditio, check 1 en inver et 0,et désact les tech de 7 à 16
        tech_id_3 = tech_obj_3.ID
        vrai_ou_faux_2 = False
        Retour_0[p].new_effect.enable_disable_technology(
            technology=tech_id_3,
            enabled=False,
            source_player=player,
        )
###########################################################################################################################################################################################################################################
#
#
#
#
#
#                                                                   Séparation, la suite c'est le Attribution ressource
#
#
#
#
#
###########################################################################################################################################################################################################################################
#---------------------------- ATTRIBUTION DES RESSOURCES POUR LES TECHNOLOGIES



for p in range (1,8):
    quantity_number_2_real = 2
    
    player=Liste_joueur[p]
    quantity_number_1_real = 1
    color=Lister_couleur[p]
    quantity_number_1 = 4
    quantity_number_2 = 2
    timer30s = 30
    timer35s = 35
    attribution_resource_pour_tech = trigger_manager.add_trigger(
        name=f"Attribution des resources pour tech {player}",
        enabled=True,
        looping=False,
    )
    attribution_resource_pour_tech.new_condition.timer(
        timer=timer30s,
    )
    for y in range (1,38):
        Amount = technology_cost_icon[y][quantity_number_2_real]
        attribution_resource_pour_tech.new_effect.modify_resource(
            tribute_list=technology_cost_icon[y][quantity_number_1],
            source_player=player,
            quantity=Amount,
            operation=Operation.SET,
        )
    Age_List=[TechInfo.FEUDAL_AGE.ID,TechInfo.CASTLE_AGE.ID,TechInfo.IMPERIAL_AGE.ID]
    for list in range(len(Age_List)):
        chinese_disable_bonus = trigger_manager.add_trigger(
            name=f"Ban modification du coûts des tech chinois{player}",
            enabled=True,
            looping=False,
        )
        chinese_disable_bonus.new_condition.research_technology(
            source_player=player,
            technology=TechInfo.CHINESE.ID,
            inverted=False,
        )
        chinese_disable_bonus.new_condition.research_technology(
            source_player=player,
            technology=Age_List[list],
            inverted=False,
        )
        chinese_disable_bonus.new_effect.modify_resource(
            source_player=player,
            tribute_list=Attribute.RESEARCH_COST_MODIFIER,
            quantity=quantity_number_1_real,
            operation=Operation.SET
        )
    #---------------------------- ATTRIBUTION DES RESSOURCES POUR LES TECHNOLOGIES
for p in range (1,8):
    player =Liste_joueur[p]
    quantity_number_1 = 1
    check_wonder = trigger_manager.add_trigger(
        name=f"Vérification merveille",
        enabled = True,
        looping=False,
    )
    check_wonder.new_condition.objects_in_area(
        source_player=player,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
        object_list=BuildingInfo.FORTRESS.ID,
        object_state=ObjectState.ALIVE,
        inverted=False,
    )
    check_wonder.new_effect.modify_resource(
        source_player=player,
        tribute_list=Attribute.UNUSED_RESOURCE_122,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
#########################################################################
#
#
#                        Prochaine section, buff orange
#
#
#########################################################################
timer30s= 30
gate_xs_script="""void gate_hp(){
xsEffectAmount(cSetAttribute, 939, 0, 20000, 1);
xsEffectAmount(cSetAttribute, 939, 0, 20000, 2);
xsEffectAmount(cSetAttribute, 939, 109, 1500, 1);
xsEffectAmount(cSetAttribute, 939, 109, 1500, 2);
xsEffectAmount(cSetAttribute, 939, 129, 1000, 1);
xsEffectAmount(cSetAttribute, 939, 129, 1000, 2);
}
"""
Fire_tower_stat_base = trigger_manager.add_trigger(
            name=f"Fire tower stats",
            enabled=True,
            looping=False,
        )
Fire_tower_stat_base.new_condition.timer(
    timer=timer30s,
)

for p in range (1,3):
    quantity_number_0 = 0
    quantity_number_1 = 1
    quantity_number_50 = 50
    quantity_number_4= 4
    Fire_tower_replace_tower = trigger_manager.add_trigger(
        name=f"Fire tower replace",
        enabled=True,
        looping=True,
    )
    player = Liste_joueur[p]
    Fire_tower_stat_base.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=BuildingInfo.FIRE_TOWER.ID,
        object_attributes=ObjectAttribute.DEAD_UNIT_ID,
        quantity=BuildingInfo.PALISADE_WALL.ID,
        operation=Operation.SET,
    )
    Fire_tower_stat_base.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=BuildingInfo.FIRE_TOWER.ID,
        object_attributes=ObjectAttribute.HIT_POINTS,
        quantity=quantity_number_500,
        operation=Operation.SET,
    )
    Fire_tower_stat_base.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=BuildingInfo.PALISADE_WALL.ID,
        object_attributes=ObjectAttribute.HIT_POINTS,
        quantity=quantity_number_7500,
        operation=Operation.SET,
    )
    Fire_tower_stat_base.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=BuildingInfo.PALISADE_WALL.ID,
        object_attributes=ObjectAttribute.TRAIN_TIME,
        quantity=quantity_number_0,
        operation=Operation.SET,
    )
    Fire_tower_stat_base.new_effect.modify_attribute(
        source_player=player,
        object_list_unit_id=BuildingInfo.FIRE_TOWER.ID,
        object_attributes=ObjectAttribute.ATTACK,
        armour_attack_class=quantity_number_4,
        armour_attack_quantity=quantity_number_35,
        operation=Operation.SET,
    )
    Fire_tower_stat_base.new_effect.change_variable(
        variable=quantity_number_50,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
    Fire_tower_replace_tower.new_condition.objects_in_area(
        source_player=player,
        object_state=ObjectState.ALIVE,
        object_list=BuildingInfo.PALISADE_WALL.ID,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
    )
    Fire_tower_replace_tower.new_effect.replace_object(
        source_player=player,
        target_player=player,
        object_list_unit_id=BuildingInfo.PALISADE_WALL.ID,
        object_list_unit_id_2=BuildingInfo.FIRE_TOWER.ID,
        **area.select_entire_map().to_dict(),
    )
    Fire_tower_replace_tower.new_effect.display_instructions(
        source_player=player,
        object_list_unit_id=UnitInfo.KING.ID,
        message="<ORANGE> Thank for the free buff, we will use it wisely to kick your asses !"
    )
    Fire_tower_replace_tower.new_effect.change_variable(
        variable=10,
        message="Fire tower effect",
        operation=Operation.SET,
        quantity=1,
    )
Fire_tower_stat_base.new_effect.script_call(
        message=gate_xs_script,
    )
city_gate_stat = trigger_manager.add_trigger(
    name="City Gate stat for P8",
    enabled=True,
    looping=False,
)
P8 = PlayerId.EIGHT
Gate_list = [BuildingInfo.CITY_GATE_WEST_TO_EAST.ID,
             BuildingInfo.CITY_GATE_NORTH_TO_SOUTH.ID,
             BuildingInfo.CITY_GATE_NORTHWEST_TO_SOUTHEAST.ID,
             BuildingInfo.CITY_GATE_SOUTHWEST_TO_NORTHEAST.ID,
             BuildingInfo.CITY_WALL.ID]
timer20s = 20
city_gate_stat.new_condition.timer(
    timer=timer20s,
)
for gate in range (len(Gate_list)):
    quantity_number_20000 = 20000
    city_gate_stat.new_effect.modify_attribute(
            source_player=P8,
            object_list_unit_id=Gate_list[gate],
            object_attributes=ObjectAttribute.DEAD_UNIT_ID,
            quantity=Gate_list[gate],
            operation=Operation.SET,
        )
    city_gate_stat.new_effect.modify_attribute(
        source_player=P8,
        object_list_unit_id=Gate_list[gate],
        object_attributes=ObjectAttribute.HIT_POINTS,
        quantity=quantity_number_20000,
        operation=Operation.SET,
    )
    city_gate_stat.new_effect.modify_attribute(
        source_player=P8,
        object_list_unit_id=Gate_list[gate],
        object_attributes=ObjectAttribute.REGENERATION_RATE,
        quantity=quantity_number_500,
        operation=Operation.SET,
    )
city_gate_stat.new_effect.modify_attribute(
        source_player=P8,
        object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
        object_attributes=ObjectAttribute.TERRAIN_RESTRICTION_ID,
        quantity=1,
        operation=Operation.SET,
)
################################################################################################################
#                                                                                                              #
#                                                                                                              #
#                                           Selection de la mission                                            #
#                                                                                                              #
#                                                                                                              #
#                                                                                                              #
################################################################################################################
display_table = trigger_manager.add_trigger(
        name=f"display table text",
        enabled = True,
        looping=False,
    )
display_table_2 = trigger_manager.add_trigger(
        name=f"Please wait",
        enabled = True,
        looping=False,
    )
display_table.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=1000,
        inverted=False,
    )
display_table_2.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=1000,
        inverted=False,
    )
display_table.short_description = str(f"7vs1 Sister Land Pine")
display_table_2.short_description = str(f"+ Please wait for host to select a mission at the wonder")
display_table.display_on_screen = True
display_table.description_order = 200

display_table_2.display_on_screen = True
display_table_2.description_order = 199
################################################################################################################
#                                                                                                              #
#                                                                                                              #
#                                           Selection de la mission                                            #
#                                                                                                              #
#                                                                                                              #
#                                                                                                              #
################################################################################################################
#------------- Variable
#--- Game element
PJ = PlayerId.ONE
#--- quantity
quantity_number_0 = 0
quantity_number_1 = 1
quantity_number_2 = 2
quantity_number_3 = 3
quantity_number_4 = 4
quantity_number_5 = 5
quantity_number_6 = 6
quantity_number_7 = 7
quantity_number_8 = 8
quantity_number_9 = 9
quantity_number_10 = 10
quantity_number_11 = 11
quantity_number_12 = 12
quantity_number_13 = 13
quantity_number_14 = 14
quantity_number_15 = 15
#--- Timers
timer_5s = 5
#--- Liste
Hero_list=[HeroInfo.AETHELFRITH.ID,HeroInfo.ADMIRAL_YI_SUN_SHIN.ID,HeroInfo.ABRAHA_ELEPHANT.ID]
Select_Hero_list = [HeroInfo.ALARIC_THE_GOTH.ID,HeroInfo.ALEXANDER_NEVSKI.ID,HeroInfo.ALGIRDAS.ID,HeroInfo.AMOGHAVARSHA.ID,
                    HeroInfo.ARCHBISHOP.ID,HeroInfo.ARCHER_OF_THE_EYES.ID,HeroInfo.ARISTAGORAS.ID,HeroInfo.ARISTIDES.ID,HeroInfo.ARTAPHERNES.ID,
                    HeroInfo.ATAULF.ID,HeroInfo.ATTILA_THE_HUN.ID,HeroInfo.BABUR.ID] # liste des héros qui font office de bouton de selection

button_list_mission = [quantity_number_1,quantity_number_2,quantity_number_3,quantity_number_4,
                       quantity_number_6,quantity_number_7,quantity_number_8,quantity_number_9,quantity_number_10,
                       quantity_number_11,quantity_number_13,quantity_number_15] #Emplacement sur la merveille

button_list =[quantity_number_7,quantity_number_8,quantity_number_12] # Emplacement sur la merveille pour les niveaux de difficulté

desc = ["Open intermidiate mission menu selection", "Open advance mission menu selection","Open expert mission menu selection"]
difficulty_choice = ["Intermidiate", "Advance", "Expert"]

trigger_ids = []

#---------------------------- Cette partie active le premier menu de selection à la merveille
name_choice_enable = "Menu selection enable unit"
difficulty_choice_enable = trigger_manager.add_trigger(
    name=name_choice_enable,
    enabled=True,
    looping=False,
)
difficulty_choice_enable.new_condition.timer(
    timer=timer_5s,
)

difficulty_choice_enable.new_condition.variable_value(
    variable=quantity_number_0,
    comparison=Comparison.EQUAL,
    quantity=quantity_number_0,
)
imp_set_res = trigger_manager.add_trigger(
    name="Set cost of mission selection",
    enabled=True,
    looping=False,
)
for select_mission_imp in range (len(Select_Hero_list)):
    imp_set_res.new_effect.change_train_location(
        source_player=PJ,
        object_list_unit_id=Select_Hero_list[select_mission_imp],
        object_list_unit_id_2=BuildingInfo.WONDER.ID,
        button_location=button_list_mission[select_mission_imp],
    )
    imp_set_res.new_effect.modify_attribute(
        source_player=PJ,
        object_attributes=ObjectAttribute.TRAIN_TIME,
        object_list_unit_id=Select_Hero_list[select_mission_imp],
        quantity=1,
        operation=Operation.SET,
    )
for h in range (len(Hero_list)):
    v = h+1
    difficulty_choice_enable.new_effect.enable_disable_object(
        source_player=PJ,
        object_list_unit_id=Hero_list[h],
        enabled=True,
    )
    difficulty_choice_enable.new_effect.change_train_location(
        object_list_unit_id=Hero_list[h],
        object_list_unit_id_2=BuildingInfo.WONDER.ID,
        source_player=PJ,
        button_location=button_list[h],
    )
    difficulty_choice_enable.new_effect.change_object_description(
        source_player=PJ,
        object_list_unit_id=Hero_list[h],
        message=desc[h],

    )
    difficulty_choice_enable.new_effect.change_object_cost(
        source_player=PJ,
        object_list_unit_id=Hero_list[h],
        resource_1=Attribute.UNUSED_RESOURCE_200,
        resource_1_quantity=quantity_number_1,
    )
    difficulty_choice_enable.new_effect.modify_attribute(
        source_player=PJ,
        object_list_unit_id=Hero_list[h],
        object_attributes=ObjectAttribute.TRAIN_TIME,
        quantity=quantity_number_0,
    )
#---------------------------- Cette partie déploie les missions
    trigger_name_difficulty_choice = f"Choosen difficulty is{difficulty_choice[h]}"
    trigger_ids.append(trigger_name_difficulty_choice)
    choosen_difficulty = trigger_manager.add_trigger(
        name=trigger_name_difficulty_choice,
        enabled=True,
        looping=True,
    )
    choosen_difficulty.new_condition.objects_in_area(
        source_player=PJ,
        object_list=Hero_list[h],
        object_state=ObjectState.ALIVE,
        quantity=quantity_number_1,
        **area.select_entire_map().to_dict(),
    )
    for select_mission in range (len(Select_Hero_list)):
        choosen_difficulty.new_effect.enable_disable_object(
            object_list_unit_id=Select_Hero_list[select_mission],
            source_player=PJ,
            enabled=True,
        )
    for select_mission in range (len(Hero_list)):
        choosen_difficulty.new_effect.enable_disable_object(
            object_list_unit_id=Hero_list[select_mission],
            source_player=PJ,
            enabled=False,
        )
    choosen_difficulty.new_effect.change_variable( #La variable 0 va gérer la difficulter sélectionner
        variable=quantity_number_0,
        quantity=v,
        operation=Operation.SET,
        message="difficulty  choice do not touch"
    )
    choosen_difficulty.new_effect.change_variable( #La variable 1 va gérer les pages de missions de la difficulté sélectionner
        variable=quantity_number_1,
        quantity=quantity_number_1,
        operation=Operation.SET,
        message="Mission choice do not touch"
    )
    choosen_difficulty.new_effect.modify_resource(
        source_player=PJ,
        tribute_list=Attribute.UNUSED_RESOURCE_201,
        quantity=quantity_number_1,
        operation=Operation.SET,
    )
    choosen_difficulty.new_effect.remove_object(
        source_player=PJ,
        object_list_unit_id=Hero_list[h],
        **area.select_entire_map().to_dict(),
        object_state=ObjectState.ALIVE,
    )
difficulty_choice_enable.new_effect.modify_resource(
    source_player=PJ,
    tribute_list=Attribute.UNUSED_RESOURCE_200,
    quantity=quantity_number_1,
    operation=Operation.SET,
)
mission_select_hero_list = [
     HeroInfo.ALARIC_THE_GOTH.ID, HeroInfo.ALEXANDER_NEVSKI.ID, HeroInfo.ALGIRDAS.ID, HeroInfo.AMOGHAVARSHA.ID,
     HeroInfo.ARCHBISHOP.ID, HeroInfo.ARCHER_OF_THE_EYES.ID, HeroInfo.ARISTAGORAS.ID, HeroInfo.ARISTIDES.ID,
     HeroInfo.ARTAPHERNES.ID,
]
for difficulty_making in range(1, 4):
    quantity_number_0 = 0
    quantity_number_1 = 1
    quantity_number_2 = 2
    quantity_number_3 = 3
    quantity_number_5000 = 5000

    if difficulty_making == 1:
        current_dict = INT_DICT_DESC
    elif difficulty_making == 2:
        current_dict = ADV_DICT_DESC
    else:
        current_dict = EXP_DICT_DESC

    total_missions = len(current_dict)
    page = 0

    for idx, key in enumerate(current_dict.keys()):
        if idx % 9 == 0:
            hero_index = 0
            page += 1
            # Nouveau trigger à chaque début de page
            trigger_name_choice_selection = f"Choosen difficulty is{difficulty_choice[h]}"
            trigger_ids.append(trigger_name_choice_selection)
            mission_choice_selection = trigger_manager.add_trigger(
                name=trigger_name_choice_selection,
                enabled=True,
                looping=True,
            )
            mission_choice_selection.new_condition.variable_value(
                variable=quantity_number_0,
                quantity=difficulty_making,
                comparison=Comparison.EQUAL,
            )
            mission_choice_selection.new_condition.variable_value(
                variable=quantity_number_1,
                quantity=page,
                comparison=Comparison.EQUAL,
            )
            print(f"--- Trigger ---")
            print(f"Condition: variable_0 = {difficulty_making}, variable_1 = {page}")

        mission_data = current_dict[key]
        hero = mission_select_hero_list[hero_index % len(mission_select_hero_list)]
        hero_index += 1
        res_quantity = current_dict[key][quantity_number_1]
        mission_description =  current_dict[key][quantity_number_0]
        # À toi de gérer ce que tu veux faire avec mission_data ici
        print(f"Mission clé {key}: {mission_data}")
        mission_choice_selection.new_effect.change_object_description(
            source_player=PlayerId.ONE,
            object_list_unit_id=hero,
            message=mission_description,
        )
        mission_choice_selection.new_effect.change_object_cost(
            source_player=PlayerId.ONE,
            object_list_unit_id=hero,
            resource_1=Attribute.UNUSED_RESOURCE_201,
            resource_1_quantity=res_quantity,
        )
#---------------- Cet section gère babur qui fait office de tourne page
    trigger_name_turn_page_1 = f"Mission turn page {difficulty_making},page {page}"
    trigger_name_turn_page_2 = f"Mission end page turn {difficulty_making},page {page}"
    trigger_ids.append(trigger_name_turn_page_1)
    trigger_ids.append(trigger_name_turn_page_2)
    mission_turn_page_plus = trigger_manager.add_trigger(
        name=trigger_name_turn_page_1,
        enabled=True,
        looping=True,
    )
    mission_turn_page_END = trigger_manager.add_trigger(
        name=trigger_name_turn_page_2,
        enabled=True,
        looping=True,
    )
    mission_turn_page_plus.new_condition.variable_value(
        variable=quantity_number_0,
        quantity=difficulty_making,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_plus.new_condition.variable_value(
        variable=quantity_number_1,
        quantity=page,
        comparison=Comparison.LESS,
    )
    mission_turn_page_END.new_condition.variable_value(
        variable=quantity_number_0,
        quantity=difficulty_making,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_END.new_condition.variable_value(
        variable=quantity_number_1,
        quantity=page,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_plus.new_effect.change_object_description(
        object_list_unit_id=HeroInfo.BABUR.ID,
        message="See next page"
    )
    mission_turn_page_plus.new_effect.change_object_cost(
        source_player=PlayerId.ONE,
        object_list_unit_id=HeroInfo.BABUR.ID,
        resource_1=Attribute.UNUSED_RESOURCE_201,
        resource_1_quantity=quantity_number_1,
    )
    mission_turn_page_END.new_effect.change_object_description(
        object_list_unit_id=HeroInfo.BABUR.ID,
        message="This is the last page, you have to go back"
    )
    mission_turn_page_END.new_effect.change_object_cost(
        source_player=PlayerId.ONE,
        object_list_unit_id=HeroInfo.BABUR.ID,
        resource_1=Attribute.UNUSED_RESOURCE_201,
        resource_1_quantity=quantity_number_5000,
    )
    trigger_name_turn_page_minus_1 = f"Mission turn page {difficulty_making},page {page}"
    trigger_name_turn_page_minus_2 = f"Mission end page turn {difficulty_making},page {page}"
    trigger_ids.append(trigger_name_turn_page_minus_1)
    trigger_ids.append(trigger_name_turn_page_minus_2)
    mission_turn_page_minus = trigger_manager.add_trigger(
        name=trigger_name_turn_page_minus_1,
        enabled=True,
        looping=True,
    )
    mission_turn_page_END_2 = trigger_manager.add_trigger(
        name=trigger_name_turn_page_minus_2,
        enabled=True,
        looping=True,
    )
    mission_turn_page_minus.new_condition.variable_value(
        variable=quantity_number_0,
        quantity=difficulty_making,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_minus.new_condition.variable_value(
        variable=quantity_number_1,
        quantity=quantity_number_1,
        comparison=Comparison.LARGER,
    )
    mission_turn_page_minus.new_effect.change_object_description(
        object_list_unit_id=HeroInfo.ATAULF.ID,
        message="See last page"
    )
    mission_turn_page_minus.new_effect.change_object_cost(
        source_player=PlayerId.ONE,
        object_list_unit_id=HeroInfo.ATAULF.ID,
        resource_1=Attribute.UNUSED_RESOURCE_201,
        resource_1_quantity=quantity_number_1,
    )
    mission_turn_page_END_2.new_condition.variable_value(
        variable=quantity_number_0,
        quantity=difficulty_making,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_END_2.new_condition.variable_value(
        variable=quantity_number_1,
        quantity=quantity_number_1,
        comparison=Comparison.EQUAL,
    )
    mission_turn_page_END_2.new_effect.change_object_description(
        object_list_unit_id=HeroInfo.ATAULF.ID,
        message="This is the first page, pick a mission or move a page futher"
    )
    mission_turn_page_END_2.new_effect.change_object_cost(
        source_player=PlayerId.ONE,
        object_list_unit_id=HeroInfo.ATAULF.ID,
        resource_1=Attribute.UNUSED_RESOURCE_201,
        resource_1_quantity=quantity_number_5000,
    )
trigger_name_previous_menu= "Previous menu"
trigger_ids.append(trigger_name_previous_menu)
mission_previous_menu = trigger_manager.add_trigger(
        name=trigger_name_previous_menu,
        enabled=True,
        looping=True,
)

mission_previous_menu.new_effect.change_object_cost(
    source_player=PlayerId.ONE,
    resource_1=Attribute.UNUSED_RESOURCE_201,
    resource_1_quantity=quantity_number_1,
    object_list_unit_id=HeroInfo.ATTILA_THE_HUN.ID,
)
mission_previous_menu.new_effect.change_object_description(
    source_player=PlayerId.ONE,
    message="Go back to the difficulty selection",
    object_list_unit_id=HeroInfo.ATTILA_THE_HUN.ID,
)
page_turn_hero = [HeroInfo.ATAULF.ID,HeroInfo.BABUR.ID,HeroInfo.ATTILA_THE_HUN.ID]
Select_Hero_list = [HeroInfo.ALARIC_THE_GOTH.ID,HeroInfo.ALEXANDER_NEVSKI.ID,HeroInfo.ALGIRDAS.ID,HeroInfo.AMOGHAVARSHA.ID,
                    HeroInfo.ARCHBISHOP.ID,HeroInfo.ARCHER_OF_THE_EYES.ID,HeroInfo.ARISTAGORAS.ID,HeroInfo.ARISTIDES.ID,HeroInfo.ARTAPHERNES.ID,
                    HeroInfo.ATAULF.ID,HeroInfo.ATTILA_THE_HUN.ID,HeroInfo.BABUR.ID]
Hero_list=[HeroInfo.AETHELFRITH.ID,HeroInfo.ADMIRAL_YI_SUN_SHIN.ID,HeroInfo.ABRAHA_ELEPHANT.ID]
for h in range (len(page_turn_hero)):
    current_hero = page_turn_hero[h]
    trigger_name_page_turn = f"Page turn hero {current_hero}"
    trigger_ids.append(trigger_name_page_turn)
    change_page_detection = trigger_manager.add_trigger(
        name=trigger_name_page_turn,
        enabled = True,
        looping= True,
    )
    change_page_detection.new_condition.objects_in_area(
        source_player=PlayerId.ONE,
        object_list=current_hero,
        **area.select_entire_map().to_dict(),
        object_state=ObjectState.ALIVE,
        quantity=quantity_number_1,
    )
    if current_hero == HeroInfo.ATAULF.ID:
        the_operation = Operation.SUBTRACT
        the_number = 1
    elif current_hero == HeroInfo.BABUR.ID:
        the_operation = Operation.ADD
        the_number = 1
    else:
        the_operation = Operation.SET
        the_number = 0
        change_page_detection.new_effect.change_variable(
            variable=quantity_number_0,
            quantity=the_number,
            operation=the_operation,
        )
        change_page_detection.new_effect.modify_resource(
            source_player=PlayerId.ONE,
            tribute_list=Attribute.UNUSED_RESOURCE_200,
            quantity=quantity_number_1,
        )
        for y in range (len(Select_Hero_list)):
            change_page_detection.new_effect.enable_disable_object(
                source_player=PlayerId.ONE,
                object_list_unit_id=Select_Hero_list[y],
                enabled=False,
            )
        for x in range (len(Hero_list)):
            change_page_detection.new_effect.enable_disable_object(
                source_player=PlayerId.ONE,
                object_list_unit_id=Hero_list[x],
                enabled=True,
            )

    change_page_detection.new_effect.change_variable(
        variable=quantity_number_1,
        quantity=the_number,
        operation=the_operation,
    )
    change_page_detection.new_effect.remove_object(
        source_player=PlayerId.ONE,
        **area.select_entire_map().to_dict(),
        object_list_unit_id=current_hero,
        object_state=ObjectState.ALIVE,
    )

################################################################################################################
#                                                                                                              #
#                                                                                                              #
#                                          Ici on récupère tous les trigger du menu                            #
#                                          et on les stock dans un gros trigger a activer pour start la mission#
#                                                                                                              #
#                                                                                                              #
################################################################################################################
stop_menu_name = "Stop menu trigger"
mission_start_stop_menu = trigger_manager.add_trigger(
    name=stop_menu_name,
    enabled = False,
    looping=False,
)
for name in range (len(trigger_ids)):
    name_trigger = trigger_ids[name]
    trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_trigger), None)
    mission_start_stop_menu.new_effect.deactivate_trigger(
        trigger_id=trigger_id_1,
    )
activate_stop_menu = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == stop_menu_name), None)
mission_start_stop_menu.new_effect.disable_object_selection(
    source_player=PlayerId.ONE,
    **area.select_entire_map().to_dict(),
    object_list_unit_id=BuildingInfo.WONDER.ID,
)
special_tech_civ(scenario)
begining_animation(scenario)
################################################################################################################
#                                                                                                              #
#                                                                                                              #
#                                           ADV-evergreen exposition                                           #
#                                           La prochaine partie est pour ADV-Green                             #
#                                                                                                              #
#                                                                                                              #
################################################################################################################

Limitation_evergreen_expo = trigger_manager.add_trigger( #Ce trigger démarre la mission evergreen exposion
    name="----B ADV MISSION EVERGREEN EXPOSITION-----",
    enabled=False,
    looping=False,
)
mission_timer= 6000
timer_name_cond = "Timer before failure"
timer_name_display ="Display timer failure"
fire_tower_destruction ="Fire tower enemy buff"
timer_text= "<RED>Finish the mission before the end of the timer : %d"
buff_text_fire_tower = "Enemy gain : +2 armors and piercings, +25 HP, melee units gain +2 attacks"
quantity_number_0 = 0
quantity_number_1 = 1
quantity_number_2 = 2
timer90s = 90
timer8s = 8
quantity_number_3 = 3
quantity_number_8 = 8
quantity_number_20 = 20
quantity_number_30 = 30
quantity_number_100 = 100
TRIGGER_NAME_INDEX = 8

name_activate = "Activate the trigger"
script_summon_hut = """void enemy_inside_huts_evergreen_A() {
xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, 30);
xsEffectAmount(cSpawnUnit, 1123, 70, 3, 8);
}"""
unlock_c_area_reward= 1200
lines = ["void fire_tower_destruction() {"]
for unit_id in XS_general_ID:
    lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, 8, 256*3 + 2, 8);")
    lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, 8, 256*4 + 2, 8);")
    lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, 0, 25, 8);")
    if unit_id in melee_general_ID:
        lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, 9, 256*4 + 2, 8);")
# Ajouts fixes pour l’unité 785
lines.append("}")
script_buff_fire_tomer_evergreen = "\n".join(lines)

P8 = PlayerId.EIGHT
Name_for_base_activation = ["adv_evergreen_multi_archer_wave_MID","adv_evergreen_house_wave_MID","Tent_summon_evergreen_A","Buff multiple ranged units",timer_name_cond,
                            timer_name_display,fire_tower_destruction]
timer_to_move= [timer_name_cond, timer_name_display,fire_tower_destruction]
relic_list_production = [Attribute.RELIC_FOOD_PRODUCTION_RATE,Attribute.RELIC_WOOD_PRODUCTION_RATE]
Trigger_name_list = ["ADV_GREEN_Start_RES_Monk","Test_Trigger"]
fire_tower_evergreen_buff = trigger_manager.add_trigger(
    name=fire_tower_destruction,
    enabled=False,
    looping=True,
)
fire_tower_evergreen_buff.new_condition.variable_value(
    variable=quantity_number_10,
    quantity=1,
)
fire_tower_evergreen_buff.new_effect.script_call(
    message=script_buff_fire_tomer_evergreen,
)
fire_tower_evergreen_buff.new_effect.display_instructions(
    message=buff_text_fire_tower,
    display_time=20,
    instruction_panel_position=1,
    object_list_unit_id=UnitInfo.MONK.ID,
)
fire_tower_evergreen_buff.new_effect.change_variable(
    variable=quantity_number_10,
    quantity=0,
    operation=Operation.SET,
)
Timer_cond_evergreen_expo = trigger_manager.add_trigger(
    name=timer_name_cond,
    enabled=False,
    looping=False,
)
Timer_cond_evergreen_expo.new_condition.timer(
    timer=mission_timer
)
Timer_cond_evergreen_expo.new_effect.declare_victory(
    source_player=P8,
)
Timer_display_evergreen_expo = trigger_manager.add_trigger(
    name=timer_name_display,
    enabled=False,
    looping=False,
)

Timer_display_evergreen_expo.new_effect.display_timer(
    message=timer_text,
    display_time=mission_timer,
    time_unit=TimeUnit.MINUTES_AND_SECONDS,
)

for move in range (len(timer_to_move)):
    trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == timer_to_move[move]), None)
    trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "----B ADV MISSION EVERGREEN EXPOSITION-----"), None)
    trigger_manager.move_triggers([trigger_id_1], trigger_id_2)

adv_ever_green_trigger = trigger_manager.add_trigger( #Ce trigger démarre la mission evergreen exposion
    name="ADV evergreen exposition start engine",
    enabled=True,
    looping=False,
)
adv_ever_green_trigger.new_condition.variable_value( #Cette condition check si c'est du niveau avancée
    quantity=quantity_number_0,
    comparison=Comparison.EQUAL,
    variable=quantity_number_2,
)

adv_ever_green_trigger.new_condition.variable_value( #Cette condition check si c'est evergreen qui à été sélectionnée
    quantity=quantity_number_1,
    comparison=Comparison.EQUAL,
    variable=quantity_number_1,
)
adv_ever_green_trigger.new_condition.objects_in_area(
    source_player=PlayerId.ONE,
    object_list=HeroInfo.ALARIC_THE_GOTH.ID,
    **area.select_entire_map().to_dict(),
    quantity=quantity_number_1,
)
for p in range (1,8):

    player= Liste_joueur[p]
    Starting_res = [Attribute.FOOD_STORAGE,Attribute.WOOD_STORAGE,Attribute.GOLD_STORAGE,Attribute.STONE_STORAGE]
    RES = [800, 800, 800, 1000]
    for h in range (len(Starting_res)):
        adv_ever_green_trigger.new_effect.modify_resource(
            source_player=player,
            tribute_list=Starting_res[h],
            quantity=RES[h],
        )
        adv_ever_green_trigger.new_effect.modify_resource(
            source_player=player,
            tribute_list=Attribute.RELIC_GOLD_PRODUCTION_RATE,
            quantity=quantity_number_30,
        )
        adv_ever_green_trigger.new_effect.research_technology(
            source_player=player,
            technology=TechInfo.FEUDAL_AGE.ID,
            force_research_technology=True,
        )
        for j in range (len(relic_list_production)):
            adv_ever_green_trigger.new_effect.modify_resource(
                source_player=player,
                tribute_list=relic_list_production[j],
                quantity=quantity_number_20,
            )
    for g in range (1,5):
        adv_ever_green_trigger.new_effect.create_garrisoned_object(
            source_player=player,
            object_list_unit_id=BuildingInfo.CASTLE.ID,
            object_list_unit_id_2=UnitInfo.MONK_WITH_RELIC.ID,
            **area.select_entire_map().to_dict(),
        )
adv_ever_green_trigger.new_effect.modify_resource(
            source_player=P8,
            tribute_list=Attribute.UNUSED_RESOURCE_030,
            quantity=quantity_number_0,
            operation=Operation.SET,
        )
adv_ever_green_trigger.new_effect.display_instructions(
    source_player=PlayerId.EIGHT,
    message="<AQUA>###### MISSIONS SELECTED EVERGREEN EXPOSITION Mission creator: Maselia \nDifficuly : Advance, Starting relics: 4, Sarting credits: 1000\nStarting age: Feudal",
    display_time=timer90s,
)
adv_ever_green_trigger.new_effect.display_instructions(
    source_player=PlayerId.EIGHT,
    message="<AQUA>Relics generation rate per minutes:\n Wood: 20, Food: 20, Gold: 30",
    display_time=timer90s,
    instruction_panel_position=quantity_number_1,
)
adv_ever_green_trigger.new_effect.display_instructions(
    source_player=PlayerId.EIGHT,
    message="<AQUA><----\n<---- check message for the defence composition\n<----",
    display_time=timer90s,
    instruction_panel_position=quantity_number_2,
)
adv_ever_green_trigger.new_effect.activate_trigger(
    trigger_id=activate_stop_menu, #Active le trigger qui désactive le menu
)
adv_ever_green_trigger.new_effect.modify_attribute(
    source_player=PlayerId.EIGHT,
    quantity=quantity_number_100,
    object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
)
adv_ever_green_trigger.new_effect.modify_attribute(
    source_player=PlayerId.EIGHT,
    quantity=quantity_number_100,
    object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    object_list_unit_id=BuildingInfo.ARMY_TENT_E.ID,
)
quantity_number_5000=5000
adv_ever_green_trigger.new_effect.modify_attribute(
    source_player=PlayerId.EIGHT,
    quantity=quantity_number_5000,
    object_attributes=ObjectAttribute.HIT_POINTS,
    object_list_unit_id=BuildingInfo.ARMY_TENT_E.ID,
)
adv_ever_green_trigger.new_effect.modify_attribute(
    source_player=PlayerId.EIGHT,
    quantity=BuildingInfo.ARMY_TENT_D.ID,
    object_attributes=ObjectAttribute.DEAD_UNIT_ID,
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
)
adv_ever_green_trigger.new_effect.script_call(
    message="void armor_out_tower() { xsEffectAmount(cSetAttribute, 190, 8, 256*3 + 0, 1);xsEffectAmount(cSetAttribute, 190, 8, 256*4 + 0, 1);xsEffectAmount(cSetAttribute, 190, 8, 256*3 + 0, 2);xsEffectAmount(cSetAttribute, 190, 8, 256*4 + 0, 2);}"
)

main_x = 98
main_y = 68
adv_ever_green_trigger.new_effect.create_object(
        source_player=PlayerId.EIGHT,
        object_list_unit_id=BuildingInfo.ARMY_TENT_E.ID,
        location_x=main_x ,
        location_y=main_y,
)
X_coordinate=[110,127]
y_coordinate=[38,51]
trigger_name_ever =  "First area tower evergreen A"
adv_evergreen_tower_A_placement= trigger_manager.add_trigger( #Ce trigger démarre la mission evergreen exposion
    name=trigger_name_ever,
    enabled=False,
    looping=False,
)
for coordinate in range (len(X_coordinate)):
    adv_evergreen_tower_A_placement.new_effect.create_object(
        source_player=PlayerId.EIGHT,
        object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
        location_x=X_coordinate[coordinate],
        location_y=y_coordinate[coordinate],
    )

adv_evergreen_tower_A_placement.new_effect.replace_object(
    source_player=PlayerId.EIGHT,
    target_player=PlayerId.EIGHT,
    object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
    object_list_unit_id_2=BuildingInfo.SEA_TOWER.ID,
    **area.select_entire_map().to_dict(),
)
wave_compo_name_list = []
Evergreen_composition_A = ["<ORANGE>DEFENCE COMPOSITION","<ORANGE>20 Multi shoot archer","<ORANGE>30 walking houses","<ORANGE> 8 Knights","<ORANGE> 2 Scorpions", "<ORANGE> 30 Skirmishers","<ORANGE> Support : Militia, Spearmen, Step Lancer, Karambit warrior(house)"]
for o in range (len(Evergreen_composition_A)):
    timer = 5 + o
    wave_compo_name = f"Wave composition {o}"
    evergreen_wave_compo_A = trigger_manager.add_trigger(
        name=wave_compo_name,
        enabled=False,
        looping=False,
    )
    evergreen_wave_compo_A.new_condition.timer(
        timer=timer,
    )
    wave_compo_name_list.append(wave_compo_name)
    for p in range (1,8):
        player = Liste_joueur[p]
        evergreen_wave_compo_A.new_effect.send_chat(
            source_player=player,
            message=Evergreen_composition_A[o],
        )

#Objective tabs

obj_tab_list=["+ Destroy the military tent to progress", "- Kill the Multi Archer (20 stone reward each)", "- Destroy the sea tower summoning the enemy units (200 stones reward each)"]
for g in range (len(obj_tab_list)):
    Tab_position = 199 - g
    trigger_name = f"Main objective A evergreen exposition : {g}"
    text_trigger_id = create_display_text_trigger(
        scenario,
        name=trigger_name,
        description_order=Tab_position,
        text=obj_tab_list[g]
    )
    wave_compo_name_list.append(trigger_name)
tid = create_toggle_trigger_range(
    scenario,
    name="Enable_wave_composition",
    start_trigger_name=wave_compo_name_list[0],
    end_trigger_name=wave_compo_name_list[-1],
    enable=True
)
adv_ever_green_trigger.new_effect.activate_trigger(
    trigger_id=tid,
)
adv_ever_green_trigger.new_effect.remove_object(
    source_player=PlayerId.ONE,
    object_list_unit_id=HeroInfo.ALARIC_THE_GOTH.ID,
    **area.select_entire_map().to_dict(),
)
X_A_coord = 110
Y_A_coord = 38
X_B_coord = 127
Y_B_coord = 51
timer7s = 7
timer24s= 24
timer12s =12
timer120s= 120
summon_tent_timer = 35

# Modification des statisques des archers pour leur donner des missiles en plus
trigger = modify_attributes_trigger(
    scenario,
    name="Buff multiple ranged units",
    player=PlayerId.EIGHT,
    units=[
        {
            "unit": UnitInfo.ARCHER.ID,
            "modifications": [
                [ObjectAttribute.MAX_TOTAL_MISSILES, 5, Operation.SET],
                [ObjectAttribute.TOTAL_MISSILES, 5, Operation.SET],
                [ObjectAttribute.DEAD_UNIT_ID, 2381, Operation.SET],
                [ObjectAttribute.HIT_POINTS, 100, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0 ,Operation.SET,"Multi shot archer"]
            ],
        },
        {
            "unit": BuildingInfo.BLACKSMITH.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 20000, Operation.SET],
                [ObjectAttribute.GARRISON_CAPACITY, 20, Operation.SET],
            ],
        },
        {
            "unit": HeroInfo.GAJAH_MADA.ID,
            "modifications": [
                [ObjectAttribute.DEAD_UNIT_ID, 70, Operation.SET],
                [ObjectAttribute.HIT_POINTS, 5, Operation.SET],
                [ObjectAttribute.STANDING_GRAPHIC, 2223, Operation.SET],
                [ObjectAttribute.WALKING_GRAPHIC, 2223, Operation.SET],
                [ObjectAttribute.RUNNING_GRAPHIC, 2223, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Walking house"]
            ],
        },
        {
            "unit": BuildingInfo.HOUSE.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 200, Operation.SET],
                [ObjectAttribute.GARRISON_CAPACITY, 10, Operation.SET],
                [ObjectAttribute.TRAIN_TIME, 0, Operation.SET],
                [ObjectAttribute.UNIT_SIZE_X, 1, Operation.SET],
                [ObjectAttribute.UNIT_SIZE_Z, 1, Operation.SET],
            ],
        },
    ]
)

first_section_main_evergreen = trigger_manager.add_trigger(
    name=name_activate,
    enabled=False,
    looping=False,
)
first_section_main_evergreen.new_condition.timer(
    timer=timer120s,
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_ever), None)
first_section_main_evergreen.new_effect.activate_trigger(
    trigger_id=trigger_id_1,
)
################################################### Data du spawn en appellant la fonction qui créer les triggers à partir des informations #####################################
spawn_data = [
    [BuildingInfo.ARMY_TENT_E.ID, UnitInfo.ARCHER.ID,   98, 68, 12, 20, Attribute.UNUSED_RESOURCE_030, 5, "adv_evergreen_multi_archer_wave_MID"],
    [BuildingInfo.ARMY_TENT_E.ID, HeroInfo.GAJAH_MADA.ID,   98, 68, 25, 30, Attribute.UNUSED_RESOURCE_72, 5, "adv_evergreen_house_wave_MID"],
##### ----------------------- support
]
used_resource_ids = [wave[6].value for wave in spawn_data if wave[6] is not None]
reset_list = used_resource_ids.copy()

for data in spawn_data:
    create_spawn_trigger(scenario, data)
spawn_data = [
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.KNIGHT.ID,     X_A_coord, Y_A_coord, timer24s,  quantity_number_8, Attribute.UNUSED_RESOURCE_008, 2, "adv_evergreen_knight_wave_A"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.SKIRMISHER.ID, X_B_coord, Y_B_coord, 15,  quantity_number_30, Attribute.UNUSED_RESOURCE_010, 4, "adv_evergreen_skimisher_wave_B"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.SCORPION.ID,   X_B_coord, Y_B_coord, 18, quantity_number_2, Attribute.UNUSED_RESOURCE_018, 1, "adv_evergreen_scorpion_wave_B"],
##### ----------------------- support
]
used_resource_ids = [wave[6].value for wave in spawn_data if wave[6] is not None]
reset_list += used_resource_ids.copy()

evergreen_summon_tent = trigger_manager.add_trigger(
    name="Tent_summon_evergreen_A",
    enabled=False,
    looping=True,
)
evergreen_summon_tent.new_condition.timer(
    timer=summon_tent_timer,
)
evergreen_summon_tent.new_condition.objects_in_area(
    source_player=P8,
    quantity=100,
    inverted=True,
    object_list=UnitInfo.KARAMBIT_WARRIOR.ID,
    **area.select_entire_map().to_dict(),
)
evergreen_summon_tent.new_effect.script_call(
    message=script_summon_hut,
)
##################### Création de la liste pour récupérer les IDS
trigger_ids_evergreen_A = []
##################### Récupère l'ID du trigger qui place les tours

for h in range (len(Name_for_base_activation)):
    trigger_name_ever=Name_for_base_activation[h]
    trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_ever), None)
    adv_ever_green_trigger.new_effect.activate_trigger(
        trigger_id=trigger_id_1,
    )
stop_wait = "Please wait"
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == stop_wait), None)
adv_ever_green_trigger.new_effect.deactivate_trigger(
    trigger_id=trigger_id_1,
)
#########################################################################

############### Création des triggers avec le spawn DATA
for data in spawn_data:
    create_spawn_trigger(scenario, data)
############### Récupération des noms des triggers pour les balancer dans le trigger qui va les activer
for name in range (len(spawn_data)):
    trigger_ids_evergreen_A.append(spawn_data[name][8])
    name_trigger = trigger_ids_evergreen_A[name]
    trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_trigger), None)
    first_section_main_evergreen.new_effect.activate_trigger(
        trigger_id=trigger_id_1,
    )

############### enfin on envoi notre activation dans le trigger qui active la mission
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_activate), None)
adv_ever_green_trigger.new_effect.activate_trigger(
    trigger_id=trigger_id_1,
)



spawn_data = [
    #Building                   #Unit                #Cooridnate of the tower   #Timer #Amount          #The res that will count or None for support # Name of the trigger
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.SPEARMAN.ID,X_A_coord, Y_A_coord,      24,  quantity_number_8, None,       8, "adv_evergreen_spearmen_suppwave_A"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.MILITIA.ID, X_B_coord, Y_B_coord,      18,  quantity_number_30, None,6, "adv_evergreen_SUPP_MILITIA_A_suppwave_B"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.MILITIA.ID, X_B_coord, Y_B_coord,     18,   quantity_number_2, None,  6, "adv_evergreen_SUPP_MILITIA_B_suppwave_B"],
    [BuildingInfo.ARMY_TENT_E.ID, UnitInfo.STEPPE_LANCER.ID,   98, 68, 12, 20, None, 5, "adv_evergreen_SUPP_STEP_LANCER_suppwave_M"],
]
for data in spawn_data:
    create_spawn_trigger(scenario, data)
trigger_ids_evergreen_A = []
trigger_id_2 = []
trigger_name_for_start = []
name_A = "Activate support A area 1 evergreen"
name_B = "Activate support M area 1 evergreen"
trigger_name_for_start.append(name_A)
trigger_name_for_start.append(name_B)
for supp_list in range (len(spawn_data)):
    trigger_name_list = spawn_data[supp_list][8]
    print(f"Le nom du trigger est {trigger_name_list}")
    IDS = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_list), None)
    trigger_id_2.append(IDS)
summon_support_EVERGREEN_A_AREA_A = trigger_manager.add_trigger(
    name=name_A,
    enabled= False,
    looping=False,
)
summon_support_EVERGREEN_A_AREA_A.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_008,
    quantity=quantity_number_8,
    inverted=False,
)
summon_support_EVERGREEN_A_AREA_A.new_effect.activate_trigger(
    trigger_id=trigger_id_2[quantity_number_0],
)
summon_support_EVERGREEN_M_AREA_A = trigger_manager.add_trigger(
    name=name_B,
    enabled= False,
    looping=False,
)
summon_support_EVERGREEN_M_AREA_A.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_030,
    quantity=20,
    inverted=False,
)
summon_support_EVERGREEN_M_AREA_A.new_effect.activate_trigger(
    trigger_id=trigger_id_2[quantity_number_3],
)
unit_list=[UnitInfo.SCORPION.ID,UnitInfo.SKIRMISHER.ID]
attribute_check = [Attribute.UNUSED_RESOURCE_018,Attribute.UNUSED_RESOURCE_010]
spawn_number = [2,30]
trigger_get_id = [1,2]
for area_A_supp_B in range (0,2):
    value = trigger_get_id[area_A_supp_B]
    unit_check = unit_list[area_A_supp_B]
    name_b = f"Activate support B area 1 evergreen {unit_check}"
    trigger_name_for_start.append(name_b)
    summon_support_EVERGREEN_B_AREA_A = trigger_manager.add_trigger(
        name=name_b,
        enabled= False,
        looping=False,
    )
    summon_support_EVERGREEN_B_AREA_A.new_condition.own_fewer_objects(
        source_player=P8,
        quantity=quantity_number_1,
        object_list=unit_list[area_A_supp_B],
        **area.select_entire_map().to_dict(),
    )
    summon_support_EVERGREEN_B_AREA_A.new_condition.accumulate_attribute(
        source_player=P8,
        attribute=attribute_check[area_A_supp_B],
        quantity=spawn_number[area_A_supp_B],
        inverted=False,
    )
    summon_support_EVERGREEN_B_AREA_A.new_effect.activate_trigger(
        trigger_id=trigger_id_2[value],
    )

Evergreen_B_area_unlock = trigger_manager.add_trigger(
        name="Area_B_unlocked",
        enabled= False,
        looping=False,
)
for f in range (len(trigger_name_for_start)):
    trigger_name_list = trigger_name_for_start[f]
    IDS = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_list), None)
    first_section_main_evergreen.new_effect.activate_trigger(
        trigger_id=IDS,
    )
debug = trigger_name_for_start
B_unlock_ID = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "Area_B_unlocked"), None)
toggle_id = combo_id = create_complex_toggle_trigger(
    scenario,
    name="Combo_Toggle_ABCD",
    toggle_logic=[
        [True, "Area_B_unlocked"],
        [False, "adv_evergreen_spearmen_suppwave_A", "adv_evergreen_SUPP_MILITIA_A_suppwave_B", "adv_evergreen_SUPP_MILITIA_B_suppwave_B", "adv_evergreen_SUPP_STEP_LANCER_suppwave_M"]
    ]
)


trigger = trigger_manager.get_trigger(toggle_id)
P8 = PlayerId.EIGHT
print(f"Value in player 8 is {P8}")
trigger.new_condition.objects_in_area(
    **area.select_entire_map().to_dict(),
    source_player=P8,
    quantity=quantity_number_1,
    object_list=BuildingInfo.ARMY_TENT_E.ID,
    inverted=True,
)
trigger.new_condition.timer(
    timer=quantity_number_5,
)
adv_evergreen_tower_A_placement.new_effect.activate_trigger(
        trigger_id=toggle_id,
)

Evergreen_A_check_goat = trigger_manager.add_trigger(
        name="Goat check zone A evergreen",
        enabled= False,
        looping=True,
)
Evergreen_A_check_goat.new_condition.objects_in_area(
    source_player=P8,
    object_list=Non_convertible_goat,
    **area.select_entire_map().to_dict(),
    quantity=quantity_number_1,
)
for p in range (1,8):
    player = Liste_joueur[p]
    Evergreen_A_check_goat.new_effect.modify_resource(
        source_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=quantity_number_20,
        operation=Operation.ADD,
    )
Evergreen_A_check_goat.new_effect.remove_object(
    source_player=P8,
    object_list_unit_id=Non_convertible_goat,
    **area.select_entire_map().to_dict(),
)

Evergreen_A_check_goat = trigger_manager.add_trigger(
        name="Tower destruction check evergreen",
        enabled= False,
        looping=True,
)
Evergreen_A_check_goat.new_condition.objects_in_area(
    source_player=P8,
    object_list=BuildingInfo.ARMY_TENT_D.ID,
    **area.select_entire_map().to_dict(),
    quantity=quantity_number_1,
    object_state=ObjectState.FOUNDATION,
)
for p in range (1,8):
    player = Liste_joueur[p]
    Evergreen_A_check_goat.new_effect.modify_resource(
        source_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=quantity_number_400,
        operation=Operation.ADD,
    )
Evergreen_A_check_goat.new_effect.remove_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
    **area.select_entire_map().to_dict(),
    object_state=ObjectState.FOUNDATION,
)
name_list = ["Goat check zone A evergreen","Tower destruction check evergreen"]
trigger_id_list = []
for tlist in range (len(name_list)):
    trigger_id_list.append (next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_list[tlist]), None))
for tlist in range (len(trigger_id_list)):
    adv_ever_green_trigger.new_effect.activate_trigger(
        trigger_id=trigger_id_list[tlist],
    )
##########################################################################################
#
#           On passe à la ZONE B de evergreen, la A est terminée
#
##########################################################################################
# On ajoute 3 d'attaque à toutes les unités et 1 d'armure de percing
lines = ["void Buff_A(){"]

for unit_id in XS_general_ID:
    lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, cArmor, 3*256 + 1, 8);")

    if unit_id == 913:
        lines += [
            f"xsEffectAmount(cAddAttribute, {unit_id}, 9, 3*256 + 3, 8);",
            f"xsEffectAmount(cAddAttribute, {unit_id}, 9, 4*256 + 3, 8);",
        ]
    elif unit_id in melee_general_ID:
        lines.append(f"xsEffectAmount(cAddAttribute, {unit_id}, 9, 4*256 + 3, 8);")
    else:
        lines += [
            f"xsEffectAmount(cAddAttribute, {unit_id}, 9, 3*256 + 3, 8);",
        ]

# Ajouts fixes pour l’unité 785
lines += [
    "xsEffectAmount(cAddAttribute, 785, 0, 1500, 8);",
    "xsEffectAmount(cAddAttribute, 785, 102, 4, 8);",
    "xsEffectAmount(cAddAttribute, 785, 9, 4, 8);",
    "}"
]

evergreen_buff_A = "\n".join(lines)
# Le script est ajouter au trigger qui débloque la zone
Evergreen_B_area_unlock.new_effect.script_call(
    message=evergreen_buff_A
)

for list_gate in range (len(Gate_list)):
    Evergreen_B_area_unlock.new_effect.remove_object(
        source_player=P8,
        object_list_unit_id=Gate_list[list_gate],
        area_x1=129,
        area_y1=73,
        area_x2=104,
        area_y2=87,
    )

adv_ever_green_trigger = trigger_manager.add_trigger( #Ce trigger démarre la mission evergreen exposion
    name="----E ADV MISSION EVERGREEN EXPOSITION A-----",
    enabled=False,
    looping=False,
)
evergreen_end_b_area = trigger_manager.add_trigger(
    name="----B ADV MISSION EVERGREEN EXPOSITION B-----",
    enabled=False,
    looping=False,
)
################## Movement du trigger qui active la seconde zone pour éviter de le désactiver
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "Area_B_unlocked"), None)
trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "----B ADV MISSION EVERGREEN EXPOSITION B-----"), None)
trigger_manager.move_triggers([trigger_id_1], trigger_id_2 + 1)
#########################################################################################################################################################


################################### On désactive tout les triggers de la zone A
disable_A_Area = create_toggle_trigger_range(
    scenario,
    name="Disable Area A Evergreen",
    start_trigger_name="----B ADV MISSION EVERGREEN EXPOSITION-----",
    end_trigger_name="----E ADV MISSION EVERGREEN EXPOSITION A-----",
    enable=False
)

Evergreen_B_area_unlock.new_effect.activate_trigger(
    trigger_id=disable_A_Area,
)



##################################################################################
#Nouvelle zone de la mission Evergreen A
#Variable pour cette zone ici
wave_compo_name_list = []
debut_list = 0
fin_liste = -1
name_t_c_area = "EVERGREEN C AREA, UNLOCK"
start_zone_c = "----B ADV MISSION EVERGREEN EXPOSITION C-----"
end_zone_c = "----E ADV MISSION EVERGREEN EXPOSITION C-----"
coord_spawn_loc_b = {
             #X   #Y
    "FLAG A":[125,114], #FLAG A
    "FLAG B":[134,124], #FLAG B
    "FLAG G":[147,84]  #FLAG G
}
Spawn_id_activation = []
X_A, Y_A = coord_spawn_loc_b["FLAG A"]
X_B, Y_B = coord_spawn_loc_b["FLAG B"]
X_G, Y_G = coord_spawn_loc_b["FLAG G"]
reward_tower_b_area = 550
area_credit_unlock = 800
tower_check= "Tower destruction check evergreen B area"
################## Tarkans
tarkans_spawn_time = 12
Amount_tarkans =  40
spawn_rate_tarkans = 3
################## BOSS
boss_spawn_time = 1
Amount_boss = 1
spawn_rate_boss = 1
################# crossbow F A
crossbowman_spawn_time = 12
Amount_crossbowmans = 35
spawn_rate_crossbowmans = 5
crossbowman_start_time = 20
################# crossbow F A
pikeman_spawn_time = 12
amount_pikeman = 42
spawn_rate_pikeman = 6
################# SUPPORT
spawn_rate_light_cav =  20
light_cav_spawn_time = 12

spawn_rate_axe_thrownman = 12
axe_thrownman_spawn_time = 8
#############################
HArcher_attack = "3*256 + 150"
HArcher_blast_width = 5
HArcher_hp = 1500
STEELK_attack = "3*256 + 45"
STEELK_Armor = "4+256 + 0"
STEELK_PARMOR = "3*256 + 250"
STEELK_hp = 1200
boss_stat_EV_B ="void boss_stat() {"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 2308, 9, {HArcher_attack} , 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 2308, 22, {HArcher_blast_width}, 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 2308, 0, {HArcher_hp}, 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 636, 9, {STEELK_attack} , 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 636, 8, {STEELK_PARMOR}, 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 636, 8, {STEELK_Armor}, 8);"
boss_stat_EV_B += f"xsEffectAmount(cSetAttribute, 636, 0, {STEELK_hp}, 8);"
boss_stat_EV_B += "}"
##################################################################################
obj_tab_list=["+ Kill The high damage cavalry archer", "+ Kill The steel plate knight", "- Destroy the sea tower summoning the enemy units (550 stones reward each)"]
for g in range (len(obj_tab_list)):
    Tab_position = 199 - g
    trigger_name = f"Main objective B evergreen exposition : {g}"
    text_trigger_id = create_display_text_trigger(
        scenario,
        name=trigger_name,
        description_order=Tab_position,
        text=obj_tab_list[g]
    )
    wave_compo_name_list.append(trigger_name)
disable_A_Area = create_toggle_trigger_range(
    scenario,
    name="Enable text B Evergreen",
    start_trigger_name=wave_compo_name_list[debut_list],
    end_trigger_name=wave_compo_name_list[fin_liste],
    enable=True
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.
                    name == "Enable text B Evergreen"), None)

Evergreen_B_area_unlock.new_effect.activate_trigger(
    trigger_id=trigger_id_1,
)
Evergreen_B_area_unlock.new_effect.script_call(
    message=boss_stat_EV_B,
)
for o in range (0,2):
    trigger_2 = next((trigger for trigger in trigger_manager.triggers if trigger.name == wave_compo_name_list[o]), None)
    if trigger_2 is not None:
        trigger_2.remove_condition(condition_index=0)
    if o == 0:
        trigger_2.new_condition.objects_in_area(
            source_player=P8,
            object_list=HeroInfo.ARTAPHERNES.ID,
            **area.select_entire_map().to_dict(),
            quantity=1,
            inverted=True,
        )
    else:
        trigger_2.new_condition.objects_in_area(
            source_player=P8,
            object_list=HeroInfo.SIEUR_BERTRAND.ID,
            **area.select_entire_map().to_dict(),
            quantity=1,
            inverted=True,
        )
    trigger_2.new_condition.timer(
        timer=10,
    )
    trigger_2.new_effect.modify_resource(
        source_player=P8,
        quantity=1,
        tribute_list=Attribute.UNUSED_RESOURCE_75,
        operation=Operation.ADD,
    )

Evergreen_B_area_unlock.new_effect.display_instructions(
    source_player=PlayerId.ONE,
    message="<AQUA>Amazing work the first area is cleared! Don't just stand there go attack the second one!",
    instruction_panel_position=0,
    object_list_unit_id=UnitInfo.ARCHER.ID,
    display_time=120,
)
Evergreen_B_area_unlock.new_effect.display_instructions(
    source_player=PlayerId.ONE,
    message="<AQUA>Reward: Castle age researched, 800 stones.",
    instruction_panel_position=1,
    display_time=120,
)
Evergreen_B_area_unlock.new_effect.display_instructions(
    source_player=PlayerId.ONE,
    message="<ORANGE>Enemy buff: +3 attacks, +1 percing armor",
    instruction_panel_position=2,
    display_time=120,
)
Evergreen_B_area_unlock.new_effect.remove_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
    **area.select_entire_map().to_dict(),
    object_state=ObjectState.ALIVE,
)
Evergreen_B_area_unlock.new_effect.modify_attribute(
    source_player=P8,
    object_list_unit_id=HeroInfo.ARTAPHERNES.ID,
    message="High damage cavalry archer",
    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
    quantity=0,
)
Evergreen_B_area_unlock.new_effect.modify_attribute(
    source_player=P8,
    object_list_unit_id=HeroInfo.SIEUR_BERTRAND.ID,
    message="Steel knight",
    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
    quantity=0,
)
for p in range (1,8):
    player = Liste_joueur[p]
    Evergreen_B_area_unlock.new_effect.research_technology(
        source_player=player,
        technology=TechInfo.CASTLE_AGE.ID,
        force_research_technology=True,
    )
    Evergreen_B_area_unlock.new_effect.tribute(
        source_player=PlayerId.GAIA,
        target_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=reward_tower_b_area,
    )
Evergreen_composition_B = ["<ORANGE>DEFENCE COMPOSITION ZONE B","<ORANGE> [BOSS] High damage cav archer","<ORANGE> [BOSS] Steel armor Knights","<ORANGE> 40 Tarkans", "<ORANGE> 35 Crossbowmans ","<ORANGE> 42 Pikemans","<ORANGE>Support: Light Cavalry, Axe Thrownman"]
for o in range (len(Evergreen_composition_B)):
    timer = 5 + o
    wave_compo_name = f"Zone b compo {o}"
    evergreen_wave_compo_B = trigger_manager.add_trigger(
        name=wave_compo_name,
        enabled=False,
        looping=False,
    )
    evergreen_wave_compo_B.new_condition.timer(
        timer=timer,
    )
    wave_compo_name_list.append(wave_compo_name)
    for p in range (1,8):
        player = Liste_joueur[p]
        evergreen_wave_compo_B.new_effect.send_chat(
            source_player=player,
            message=Evergreen_composition_B[o],
        )
tid = create_toggle_trigger_range(
    scenario,
        name="Enable_wave_composition_area_B",
        start_trigger_name=wave_compo_name_list[0],
        end_trigger_name=wave_compo_name_list[-1],
        enable=True
)
Evergreen_B_area_unlock.new_effect.activate_trigger(
    trigger_id=tid,
)

#Creation des tours
#################################################################################
for flag_name, (x, y) in coord_spawn_loc_b.items():
    print(f"Création de {flag_name} à X:{x}, Y:{y}")
    Evergreen_B_area_unlock.new_effect.create_object(
        source_player=P8,
        object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
        location_x=x,
        location_y=y,
    )
Evergreen_B_area_unlock.new_effect.replace_object(
    source_player=P8,
    target_player=P8,
    object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
    object_list_unit_id_2=BuildingInfo.SEA_TOWER.ID,
    **area.select_entire_map().to_dict(),
)
Evergreen_B_check_tower = trigger_manager.add_trigger(
        name=tower_check,
        enabled= False,
        looping=True,
)
Evergreen_B_check_tower.new_condition.objects_in_area(
    source_player=P8,
    object_list=BuildingInfo.ARMY_TENT_D.ID,
    **area.select_entire_map().to_dict(),
    quantity=quantity_number_1,
    object_state=ObjectState.FOUNDATION,
)
for p in range (1,8):
    player = Liste_joueur[p]
    Evergreen_B_check_tower.new_effect.modify_resource(
        source_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=reward_tower_b_area,
        operation=Operation.ADD,
    )
Evergreen_B_check_tower.new_effect.remove_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.ARMY_TENT_D.ID,
    **area.select_entire_map().to_dict(),
    object_state=ObjectState.FOUNDATION,
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == tower_check), None)
Spawn_id_activation.append(trigger_id_1)
spawn_data = [
    #Building                   #Unit                #Cooridnate of the tower   #Timer  #Amount   #The res that will count or None for support # Name of the trigger
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.CROSSBOWMAN.ID,X_A ,Y_A,crossbowman_spawn_time,Amount_crossbowmans,Attribute.UNUSED_RESOURCE_71,spawn_rate_crossbowmans, "adv_evergreen_crossbowman_z_b"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.PIKEMAN.ID, X_B, Y_B,pikeman_spawn_time, amount_pikeman,Attribute.UNUSED_RESOURCE_72,spawn_rate_pikeman, "adv_evergreen_pikeman_z_b"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.TARKAN.ID,X_G, Y_G,tarkans_spawn_time,  Amount_tarkans, Attribute.UNUSED_RESOURCE_70,spawn_rate_tarkans, "adv_evergreen_tarkans_m_z_b"],
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       BOSS SECTION
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    [BuildingInfo.SEA_TOWER.ID, HeroInfo.ARTAPHERNES.ID,X_G ,Y_G,boss_spawn_time,Amount_boss,Attribute.UNUSED_RESOURCE_73,spawn_rate_boss, "adv_evergreen_BOSS_HCAV_ARCHER_z_b"],
    [BuildingInfo.SEA_TOWER.ID, HeroInfo.SIEUR_BERTRAND.ID,X_G ,Y_G,boss_spawn_time,Amount_boss,Attribute.UNUSED_RESOURCE_74,spawn_rate_boss, "adv_evergreen_BOSS_STEEL_KNIGHT_z_b"],
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                       SUPP SECTION
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.LIGHT_CAVALRY.ID,X_A ,Y_A,crossbowman_spawn_time,quantity_number_1,None,spawn_rate_crossbowmans, "adv_evergreen_LIGHT_CAVALRY_z_b_supp"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.THROWING_AXEMAN.ID, X_B, Y_B,pikeman_spawn_time, quantity_number_1,None,spawn_rate_pikeman, "adv_evergreen_THROWING_AXEMAN_z_b_supp"],
]
used_resource_ids = [wave[6].value for wave in spawn_data if wave[6] is not None]
reset_list += used_resource_ids.copy()

for data in spawn_data:
    create_spawn_trigger(scenario, data)
# Activation des spawn
AB_ID = create_toggle_trigger_range(
        scenario,
        name="EG_SIDE_ZONE_B_SPAWN",
        start_trigger_name="adv_evergreen_crossbowman_z_b",
        end_trigger_name="adv_evergreen_pikeman_z_b",
        enable=True
)

trigger_B1 = trigger_manager.get_trigger(AB_ID)
trigger_B1.new_condition.timer(
    timer=crossbowman_start_time
)
Spawn_id_activation.append(AB_ID)
G_ID = create_toggle_trigger_range(
        scenario,
        name="EG_MID_ZONE_B_SPAWN",
        start_trigger_name="adv_evergreen_tarkans_m_z_b",
        end_trigger_name="adv_evergreen_BOSS_STEEL_KNIGHT_z_b",
        enable=True
)
Spawn_id_activation.append(G_ID)

toggle_id = axe_thrownman = create_complex_toggle_trigger(
    scenario,
    name="ADV_EVERGREEN_B_AT_SUPP",
    toggle_logic=[
        [True, "adv_evergreen_THROWING_AXEMAN_z_b_supp"],
        [True, "adv_evergreen_LIGHT_CAVALRY_z_b_supp"],
    ]
)

trigger = trigger_manager.get_trigger(toggle_id)
trigger.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_71,
    quantity=Amount_crossbowmans,
)
Spawn_id_activation.append(toggle_id)

evergreen_unlock_c_area = trigger_manager.add_trigger(
    name=name_t_c_area,
    enabled=False,
    looping=False,
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_t_c_area), None)
Spawn_id_activation.append(trigger_id_1)
#--------- Trigger crée on redistribue dans le trigger d'activation avec la liste
for h in range (len(Spawn_id_activation)):
    Evergreen_B_area_unlock.new_effect.activate_trigger(
        trigger_id=Spawn_id_activation[h]
    )

evergreen_end_b_area = trigger_manager.add_trigger(
    name="----E ADV MISSION EVERGREEN EXPOSITION B-----",
    enabled=False,
    looping=False,
)
evergreen_start_c_area = trigger_manager.add_trigger(
    name=start_zone_c,
    enabled=False,
    looping=False,
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_t_c_area), None)
trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == start_zone_c), None)
trigger_manager.move_triggers([trigger_id_1], trigger_id_2 + 1)
##################################################################################
#
#
#                          C area is next
#
#
##################################################################################
Unlock_txt_1 = "<AQUA>The bosses are dead, the gate for the next area are open, It will take some time to reach the next area, destroy the blackmist to unlock the shortcut allowing"
Unlock_txt_2= "<AQUA>Reward: 1200 Stones"
Unlock_txt_3= "<ORANGE>ENEMY buff: +20% HP, +10% attacks speeds"
lines = ["void Buff_C_evergreen(){"]
unlock_c_area_reward= 1200
for unit_id in XS_general_ID:
    lines.append(f"xsEffectAmount(cMulAttribute, {unit_id}, 10, 0.90, 8);")
    lines.append(f"xsEffectAmount(cMulAttribute, {unit_id}, 0, 1.20, 8);")
# Ajouts fixes pour l’unité 785
lines += [
    "xsEffectAmount(cAddAttribute, 785, 0, 1000, 8);",
    "xsEffectAmount(cAddAttribute, 785, 102, 7, 8);",
    "xsEffectAmount(cAddAttribute, 785, 107, 7, 8);",
    "xsEffectAmount(cAddAttribute, 24, 65, -1, 8);",
    "}"
]
script_buff_C = "\n".join(lines)
portrait = UnitInfo.ARCHER.ID,
spawn_timer= 120
spawn_timer_C= 180
cycle_timer = 30
display_time = 120
time_cart_bomb = 300
remove_x_1 = 153
remove_x_2 = 184
remove_y_1 = 99
remove_y_2 = 76
coordinate_c_area = \
            [113,161, #FLAG A
              110,186, # FLAG B
              150,119, # FLAG C
              152,159] # FLAG M
ambush_coord_b_area =[127, 51,
                      153,54]
carts_speed_reduce = 2
hp_cart = 5000
name_cart = "Anti bombard tower device"
display_ambush = 120
T_name_cart = ["Cart detection area","Spawn the cart at blacksmith","Cart remove selection","Cart moving to tower"]
text_ambush = "<GREEN> It's an AMBUSH ! enemy spawn in the previous area, destroy the tower to stop the ambush !"
bomb_objective_name="Evergreen cart bomb display"
bomb_description_order=194
bomb_description_text="- Escort the cart to the bomb tower"
timer_ambush = 300
timer_cart= 260
tower_list = [BuildingInfo.GUARD_TOWER.ID,BuildingInfo.GUARD_TOWER.ID,BuildingInfo.SEA_TOWER.ID,BuildingInfo.BOMBARD_TOWER.ID]
Battalion_teuton = f"void battalion_teuton_evergreen()"
Battalion_teuton += """ {
    xsTaskAmount(0, 10);
    xsTaskAmount(1, 1);
    xsTaskAmount(2, 5);
    xsTaskAmount(3, 0);
    xsTaskAmount(4, 117);
    xsTaskAmount(5, 4);
    xsTaskAmount(6, 4);
    xsTask(25, 155, 906, 8);
}
"""
name_attribute_c = "Zone c attribute"
ambush_janisary_name_a ="combo janisary gun form"

script_ambush_janisary_projectile_a = "void combo_gun() {"
script_ambush_janisary_projectile_a += f"""
xsEffectAmount(cSetAttribute, {UnitInfo.HAND_CANNONEER.ID}, {ObjectAttribute.PROJECTILE_UNIT}, 380, 8);
"""
script_ambush_janisary_projectile_a += "\n}"
ambush_janisary_name_b ="combo janisary sword form"
script_ambush_janisary_projectile_b = "void sword_form() {"
script_ambush_janisary_projectile_b += f"""
xsEffectAmount(cSetAttribute, {UnitInfo.HAND_CANNONEER.ID}, {ObjectAttribute.PROJECTILE_UNIT}, -1, 8);
"""
script_ambush_janisary_projectile_b += "\n}"
############## for support
list_attribute= [Attribute.UNUSED_RESOURCE_018,Attribute.UNUSED_RESOURCE_70,Attribute.UNUSED_RESOURCE_103,Attribute.UNUSED_RESOURCE_72,Attribute.UNUSED_RESOURCE_73,Attribute.UNUSED_RESOURCE_74]
list_unit= [UnitInfo.MANGONEL.ID,UnitInfo.KNIGHT.ID,UnitInfo.TEUTONIC_KNIGHT.ID,UnitInfo.LONG_SWORDSMAN.ID,None,None]
check_unit = []
check_attribute = []
wave_compo_name_list = []
######################################################################
# ----------------- MID TOWER
spawn_rate_elephant = 3
amount_ele = 9
spawn_time_ele = 12

spawn_rate_kipchack = 15
amount_kipchack = 15
# ----------------- A TOWER
spawn_rate_knight = 12
amount_knight = 50
spawn_time_knight = 10

spawn_rate_mangonel = 1
amount_mangonel = 8
spawn_time_mangonel = 18
# ---------- SUPP TOWER A
spawn_rate_skimisher = 12
infinite = 1 #Necesaire pour l'identation
spawn_time_skimisher = 12

# ---------------- B tower
spawn_rate_battalion_teuton_knights = 2
amount_battalion_teuton_knights = 12
spawn_time_battalion_teutons = 12

spawn_rate_longswordman = 10
amount_longswordman = 80
spawn_time_longswordman = 12
# ----------- SUPP Tower B
spawn_rate_surprise_camel_archer = 4
spawn_time_surprise_camel_archer = 25

spawn_rate_FAP = 8
spawn_time_FAP = 14


# ---------------- C tower
spawn_rate_bf_crossbow = 20
amount_bf_crossbow =  8
spawn_time_bf_crossbow = 2
#sew = Super eagle warrior
spawn_rate_sew = 5
amount_sew = 20
spawn_time_sew = 15
#-----------------------
spawn_rate_slinger = 20
spawn_timer_slinger = 35
#--------------- Ambush B tower
spawn_rate_mangudai = 10
amount_mangudai =  100
spawn_time_mangudai = 25
#--------------- Ambush C tower
spawn_rate_combo_hand_canon = 15
amount_bf_combo_hand_canon =  90
spawn_time_combo_hand_canon = 18
list_blacksmith_function_name = []
blacksmith_defence = "Blacksmith defence evergreen c"
blacksmith_timer_spawn = 50
amount_paladin = 14
BL_D_TIME = 30
BL_WARNING = "<ORANGE> HEY ! THAT OUR VACATION HOME ! GET OFF OUR PROPERTY NOW !"
BL_destroy = "<AQUA> The blacksmith is down, now the shortcut is open and the old path is closed great job"
BL_death_time_text= 120
Blacksmith_dead= "Blacksmith death"
activate_blacksmith = []
#####################################################################
for i in range (len(tower_list)):
    x = coordinate_c_area[2 * i]
    y = coordinate_c_area[2 * i + 1]
    evergreen_unlock_c_area.new_effect.create_object(
        source_player=P8,
        object_list_unit_id=tower_list[i],
        location_x=x,
        location_y=y,
    )
Evergreen_composition_c = [
    "<ORANGE> " + line for line in [
        "DEFENCE COMPOSITION ZONE C",
        f"{amount_ele} elephant archer tent shooter",
        f"{amount_kipchack} Kipchak",
        f"{amount_knight} knight",
        f"{amount_mangonel} mangonel",
        f"{amount_battalion_teuton_knights} Battalian teuton",
        f"{amount_longswordman} longswordsman",
        f"{amount_bf_crossbow} Burst fire crossbow",
        f"{amount_sew} Super eagle warrior",
        "Support: Elite skirmisher, Fast attack pikeman, Surprise camel archer",
        "Tent support : Ghulam, Chakram Thrower",
        "Blacksmith protector: Paladin"
    ]
]
tent_summon = 45
script_summon_hut_evergreen_c = """void enemy_inside_huts_evergreen_c() {
int randomValue_A = xsGetRandomNumberLH(3, 6);
int randomValue_B = xsGetRandomNumberLH(2, 4);
xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, 30);
xsEffectAmount(cSpawnUnit, 1741, 1098, randomValue_B, 8);
xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, 30);
xsEffectAmount(cSpawnUnit, 1747, 1098, randomValue_A, 8);
}"""
script_summon_bomb_cart = """void summon_bomb_evergreen_c() {
xsEffectAmount(cModResource, cAttributeSpawnCap, cAttributeSet, 1);
xsEffectAmount(cSpawnUnit, 18, 733, 1, 1);
}"""
for o in range (len(Evergreen_composition_c)):
    timer = 5 + o
    wave_compo_name = f"Zone c compo {o}"
    evergreen_wave_compo_c = trigger_manager.add_trigger(
        name=wave_compo_name,
        enabled=False,
        looping=False,
    )
    evergreen_wave_compo_c.new_condition.timer(
        timer=timer,
    )
    wave_compo_name_list.append(wave_compo_name)
    for p in range (1,8):
        player = Liste_joueur[p]
        evergreen_wave_compo_c.new_effect.send_chat(
            source_player=player,
            message=Evergreen_composition_c[o],
        )
tid = create_toggle_trigger_range(
    scenario,
        name="Enable_wave_composition_area_C",
        start_trigger_name=wave_compo_name_list[0],
        end_trigger_name=wave_compo_name_list[-1],
        enable=True
)
evergreen_unlock_c_area.new_effect.activate_trigger(
    trigger_id=tid,
)
obj_tab_list=["+ Destroy the bombard tower","+ Kill all Elephant archer tent shooter", "- Destroy the sea tower summoning the enemy units (400 stones reward)"]
wave_compo_name_list = []
for g in range (len(obj_tab_list)):
    Tab_position = 199 - g
    trigger_name = f"Main objective C evergreen exposition : {g}"
    text_trigger_id = create_display_text_trigger(
        scenario,
        name=trigger_name,
        description_order=Tab_position,
        text=obj_tab_list[g]
    )
    evergreen_unlock_c_area.new_effect.activate_trigger(
        trigger_id=text_trigger_id,
    )

trigger_2 = next((trigger for trigger in trigger_manager.triggers if trigger.name == "Main objective C evergreen exposition : 1"), None)
if trigger_2 is not None:
    trigger_2.remove_condition(condition_index=0)
trigger_2.new_condition.objects_in_area(
    source_player=P8,
    object_list=UnitInfo.ELEPHANT_ARCHER.ID,
    **area.select_entire_map().to_dict(),
    quantity=1,
    inverted=True,
)
trigger_2.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_008,
    quantity=amount_ele,
)
trigger_2.new_effect.modify_resource(
    source_player=P8,
    tribute_list=Attribute.UNUSED_RESOURCE_105,
    quantity=1,
    operation=Operation.ADD,
)
trigger_2 = next((trigger for trigger in trigger_manager.triggers if trigger.name == "Main objective C evergreen exposition : 0"), None)
if trigger_2 is not None:
    trigger_2.remove_condition(condition_index=0)
trigger_2.new_condition.objects_in_area(
    source_player=P8,
    object_list=BuildingInfo.BOMBARD_TOWER.ID,
    **area.select_entire_map().to_dict(),
    quantity=1,
    inverted=True,
)
trigger_2.new_effect.modify_resource(
    source_player=P8,
    tribute_list=Attribute.UNUSED_RESOURCE_105,
    quantity=1,
    operation=Operation.ADD,
)
evergreen_unlock_c_area.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_75,
    quantity=2,
    inverted=False,
)

evergreen_unlock_c_area.new_effect.display_instructions(
    source_player = P1,
    instruction_panel_position=0,
    display_time=display_time,
    message=Unlock_txt_1,
)
evergreen_unlock_c_area.new_effect.script_call(
    message=script_buff_C,
)
evergreen_unlock_c_area.new_effect.display_instructions(
    source_player = P1,
    instruction_panel_position=1,
    display_time=display_time,
    message=Unlock_txt_2,
)
evergreen_unlock_c_area.new_effect.display_instructions(
    source_player = P8,
    instruction_panel_position=2,
    display_time=display_time,
    message=Unlock_txt_3,
)
for p in range (1,8):
    player = Liste_joueur[p]
    evergreen_unlock_c_area.new_effect.tribute(
        source_player=PlayerId.GAIA,
        target_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=unlock_c_area_reward,
    )
evergreen_unlock_c_area.new_effect.remove_object(
    source_player=P8,
    object_type=ObjectType.BUILDING,
    area_x1=remove_x_1,
    area_x2=remove_x_2,
    area_y1=remove_y_1,
    area_y2=remove_y_2,
)
evergreen_unlock_c_area.new_effect.remove_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
    **area.select_entire_map().to_dict(),
)
evergreen_unlock_c_area.new_effect.script_call(
    message=Battalion_teuton,
)
evergreen_turn_off_B = create_toggle_trigger_range(
        scenario,
        name="B_AREA_OFF",
        start_trigger_name="----B ADV MISSION EVERGREEN EXPOSITION B-----",
        end_trigger_name="----E ADV MISSION EVERGREEN EXPOSITION B-----",
        enable=False,
)
evergreen_unlock_c_area.new_effect.activate_trigger(
    trigger_id=evergreen_turn_off_B,
)
for h in range (len(reset_list)):
    evergreen_unlock_c_area.new_effect.modify_resource(
        source_player=P8,
        tribute_list=reset_list[h],
        quantity=0,
        operation=Operation.SET,
    )
for t in range (len(tower_list)):
    x = coordinate_c_area[2 * t]
    y = coordinate_c_area[2 * t + 1]
    evergreen_unlock_c_area.new_effect.create_object(
        source_player=P8,
        object_list_unit_id=tower_list[t],
        location_x=x, 
        location_y=y,
    )
trigger = modify_attributes_trigger(
    scenario,
    name=name_attribute_c,
    player=PlayerId.EIGHT,
    units=[
        {
            "unit": UnitInfo.CROSSBOWMAN.ID,
            "modifications": [
                [ObjectAttribute.MAX_TOTAL_MISSILES, 14, Operation.SET],
                [ObjectAttribute.TOTAL_MISSILES, 14, Operation.SET],
                [ObjectAttribute.HIT_POINTS, 350, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Burst fire crossbow"]
            ],
        },
    {
            "unit": BuildingInfo.TENT_B.ID,
            "modifications": [
                [ObjectAttribute.WALKING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.STANDING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.RUNNING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Summon tent"],
                [ObjectAttribute.HIT_POINTS,300,Operation.SET],
                [ObjectAttribute.GARRISON_CAPACITY, 5, Operation.SET],
                [ObjectAttribute.TRAIN_TIME, 0, Operation.SET],
                [ObjectAttribute.UNIT_SIZE_X, 1 , Operation.SET],
                [ObjectAttribute.UNIT_SIZE_Y, 1 , Operation.SET],

            ],
        },
        {
            "unit": UnitInfo.ELEPHANT_ARCHER.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 960, Operation.SET],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 10, Operation.SET],
                [ObjectAttribute.MAX_RANGE, 5, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0 , Operation.SET,"Elephant archer tent shooter"],
                [ObjectAttribute.PROJECTILE_UNIT, 372, Operation.SET]
            ],
        },
{
            "unit": 372,
            "modifications": [
                [ObjectAttribute.WALKING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.STANDING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.RUNNING_GRAPHIC, 3360, Operation.SET],
                [ObjectAttribute.DEAD_UNIT_ID, 1098, Operation.SET],
            ],
        },
        {
            "unit": UnitInfo.TEUTONIC_KNIGHT.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 180, Operation.SET],
                [ObjectAttribute.COMBAT_ABILITY, 32, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET, "Battalion teutonic knight"],
            ],
        },
        {
            "unit": UnitInfo.EAGLE_WARRIOR.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 200, Operation.SET],
                [ObjectAttribute.MOVEMENT_SPEED, 2, Operation.MULTIPLY],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 2, Operation.DIVIDE],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET, "Super eagle warrior"],
                [ATTACK_PRIORITY, 3, Operation.SET]
            ],
        },
{
            "unit": UnitInfo.PIKEMAN.ID,
            "modifications": [
                [ObjectAttribute.ATTACK_RELOAD_TIME, 2, Operation.DIVIDE],
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Fast Attack Pikeman"]
            ],
        },
{
            "unit": UnitInfo.CAMEL_ARCHER.ID,
            "modifications": [
                [ObjectAttribute.DEAD_UNIT_ID,1263, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Surprise Camel Archer"]
            ],
        },
{
            "unit": UnitInfo.HAND_CANNONEER.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Combo hand canon"]
            ],

        },
        {
            "unit": BuildingInfo.GUARD_TOWER.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 27000, Operation.SET],
                [ObjectAttribute.DEAD_UNIT_ID, 234, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"You cannot destroy guard tower"],
                [ObjectAttribute.GARRISON_CAPACITY, 30, Operation.SET],
                [ObjectAttribute.TRAIN_TIME, 0, Operation.SET],
                [ObjectAttribute.REGENERATION_RATE, 5000, Operation.SET],
                [ObjectAttribute.INVULNERABILITY_LEVEL, 5000, Operation.SET]
            ],

        },
{
            "unit": BuildingInfo.BOMBARD_TOWER.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 20000, Operation.SET],
                [ObjectAttribute.BLAST_WIDTH, 5, Operation.SET],
                [ObjectAttribute.GARRISON_CAPACITY, 30, Operation.SET],
            ],

        },
{
            "unit": BuildingInfo.WATCH_TOWER.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 5000, Operation.SET],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 14, Operation.DIVIDE],
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Sentry watch tower"],
                [ObjectAttribute.GARRISON_CAPACITY, 30, Operation.SET],
            ],

        },
    ]
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_attribute_c), None)
evergreen_unlock_c_area.new_effect.activate_trigger(
    trigger_id=trigger_id_1,
)
spawn_data = [
    #Building                   #Unit                #Cooridnate of the tower   #Timer  #Amount   #The res that will count or None for support # Name of the trigger
    [BuildingInfo.BOMBARD_TOWER.ID, UnitInfo.ELEPHANT_ARCHER.ID,coordinate_c_area[6] ,coordinate_c_area[7] ,spawn_time_ele,amount_ele,Attribute.UNUSED_RESOURCE_008,spawn_rate_elephant, "adv_evergreen_tent_summon_ele_z_c"],
    [BuildingInfo.BOMBARD_TOWER.ID, UnitInfo.KIPCHAK.ID, coordinate_c_area[6] , coordinate_c_area[7] , 0, amount_kipchack,Attribute.UNUSED_RESOURCE_010,amount_kipchack, "adv_evergreen_kipchak_z_c"],
# A tower
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.MANGONEL.ID,coordinate_c_area[0],coordinate_c_area[1],spawn_time_mangonel,  amount_mangonel, Attribute.UNUSED_RESOURCE_018,spawn_rate_mangonel, "adv_evergreen_mangonel_a_z_c"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.KNIGHT.ID,coordinate_c_area[0], coordinate_c_area[1],spawn_time_knight,  amount_knight, Attribute.UNUSED_RESOURCE_70,spawn_rate_knight, "adv_evergreen_knight_a_z_c"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.TEUTONIC_KNIGHT.ID,coordinate_c_area[2],coordinate_c_area[3],spawn_time_battalion_teutons,  amount_battalion_teuton_knights, Attribute.UNUSED_RESOURCE_103,spawn_rate_battalion_teuton_knights, "adv_evergreen_batta_teuton_b_z_c"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.LONG_SWORDSMAN.ID,coordinate_c_area[2],coordinate_c_area[3],spawn_time_longswordman,  amount_longswordman, Attribute.UNUSED_RESOURCE_72,spawn_rate_longswordman, "adv_evergreen_longsworman_b_z_c"],

    [BuildingInfo.SEA_TOWER.ID, UnitInfo.CROSSBOWMAN.ID,coordinate_c_area[4],coordinate_c_area[5],spawn_time_bf_crossbow,  amount_bf_crossbow, Attribute.UNUSED_RESOURCE_73,spawn_rate_crossbowmans, "adv_evergreen_crossbow_c_z_c"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.EAGLE_WARRIOR.ID,coordinate_c_area[4],coordinate_c_area[5],spawn_time_sew,  amount_sew, Attribute.UNUSED_RESOURCE_74,spawn_rate_sew, "adv_evergreen_sew_c_z_c"],
#####################################################################################################################################################################################################################################################################
#                           SUPP WAVE EN DESSOUS
###########################################################################################################################################################################################################
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.ELITE_SKIRMISHER.ID, coordinate_c_area[0], coordinate_c_area[1], spawn_time_skimisher,
     infinite, None, spawn_rate_skimisher, "adv_evergreen_skirmisher_a_z_c_s"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.CAMEL_ARCHER.ID, coordinate_c_area[2], coordinate_c_area[3],
     spawn_time_surprise_camel_archer, infinite, None,
     spawn_rate_battalion_teuton_knights, "adv_evergreen_surprise_camel_Archer_b_z_c_s"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.PIKEMAN.ID, coordinate_c_area[2], coordinate_c_area[3],
     spawn_time_FAP, infinite, None, spawn_rate_FAP,
     "adv_evergreen_Fast_Attack_Pikeman_b_z_c_s"],

    [BuildingInfo.SEA_TOWER.ID, UnitInfo.SLINGER.ID, coordinate_c_area[4], coordinate_c_area[5],
     spawn_timer_slinger, infinite, None, spawn_rate_slinger,
     "adv_evergreen_slinger_c_z_c_s"],

]

# Trouver l’index de départ
start_index = next(
    (i for i, row in enumerate(spawn_data) if row[1] == UnitInfo.ELITE_SKIRMISHER.ID),
    None
)

if start_index is None:
    raise ValueError("⚠️ Aucun ELITE_SKIRMISHER.ID trouvé dans spawn_data")

# Extraire tous les noms de trigger à partir de là
supp_trigger_names = [row[-1] for row in spawn_data[start_index:]]


for data in spawn_data:
    create_spawn_trigger(scenario, data)
tent_support_evergreen_c_area = trigger_manager.add_trigger(
    name="Tent support summon",
    enabled=False,
    looping=True,
)
tent_support_evergreen_c_area.new_condition.timer(
    timer=tent_summon,
)
tent_support_evergreen_c_area.new_effect.script_call(
    message=script_summon_hut_evergreen_c,
)
trigger_id_tent = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "Tent support summon"), None)
ambush_janisary_A = modify_attributes_trigger( #Gun form
        scenario,
        name="combo janisary gun form",
        player=PlayerId.EIGHT,
        units=[
            {
                "unit": UnitInfo.HAND_CANNONEER.ID,
                "modifications": [
                    [ObjectAttribute.STANDING_GRAPHIC, 855, Operation.SET],
                    [ObjectAttribute.DYING_GRAPHIC, 852, Operation.SET],
                    [ObjectAttribute.WALKING_GRAPHIC, 859, Operation.SET],
                    [ObjectAttribute.RUNNING_GRAPHIC, 859, Operation.SET],
                    [ObjectAttribute.MAX_RANGE, 7, Operation.SET],
                ],
            }
    ]
)

ambush_janisary_A.new_effect.script_call(
    message=script_ambush_janisary_projectile_a,
)

ambush_janisary_B = modify_attributes_trigger( #sword form
        scenario,
        name="combo janisary sword form",
        player=PlayerId.EIGHT,
        units=[
            {
                "unit": UnitInfo.HAND_CANNONEER.ID,
                "modifications": [
                    [ObjectAttribute.STANDING_GRAPHIC, 7598, Operation.SET],
                    [ObjectAttribute.DYING_GRAPHIC, 7595, Operation.SET],
                    [ObjectAttribute.WALKING_GRAPHIC, 7602, Operation.SET],
                    [ObjectAttribute.RUNNING_GRAPHIC, 7602, Operation.SET],
                    [ObjectAttribute.MAX_RANGE, 0, Operation.SET],
                ],
            }
    ]
)

ambush_janisary_B.new_effect.script_call(
    message=script_ambush_janisary_projectile_b,
)
################################################
#                                              #
#               Combo janisary                 #
#                                              #
################################################
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "combo janisary gun form"), None)
trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "combo janisary sword form"), None)
evergreen_unlock_c_area.new_effect.activate_trigger( #Because we need to start the cycle
    trigger_id=trigger_id_1,
)
ambush_janisary_A.new_condition.timer(
    timer=cycle_timer,
)
ambush_janisary_A.new_effect.activate_trigger(
    trigger_id=trigger_id_2,
)
ambush_janisary_A.new_effect.deactivate_trigger(
    trigger_id=trigger_id_1,
)

ambush_janisary_B.new_condition.timer(
    timer=cycle_timer,
)
ambush_janisary_B.new_effect.activate_trigger(
    trigger_id=trigger_id_1,
)
ambush_janisary_B.new_effect.deactivate_trigger(
    trigger_id=trigger_id_2,
)


spawn_data = [
    #Building                   #Unit                #Cooridnate of the tower   #Timer  #Amount   #The res that will count or None for support # Name of the trigger
        [BuildingInfo.WATCH_TOWER.ID, UnitInfo.MANGUDAI.ID,ambush_coord_b_area[0] ,ambush_coord_b_area[1] ,spawn_time_mangudai,amount_mangudai,Attribute.UNUSED_RESOURCE_76,spawn_rate_mangudai, "adv_evergreen_ambush_Mangudai"],
        [BuildingInfo.WATCH_TOWER.ID, UnitInfo.HAND_CANNONEER.ID, ambush_coord_b_area[2] , ambush_coord_b_area[3] , spawn_time_combo_hand_canon, amount_bf_combo_hand_canon,Attribute.UNUSED_RESOURCE_102,spawn_rate_combo_hand_canon, "adv_evergreen_ambush_hand_canon"],
# A tower

]
for data in spawn_data:
    create_spawn_trigger(scenario, data)

activation_wave_c_MID = create_toggle_trigger_range(
        scenario,
        name="START_MID_WAVE_C",
        start_trigger_name="adv_evergreen_tent_summon_ele_z_c",
        end_trigger_name="adv_evergreen_knight_a_z_c",
        enable=True
)
activation_wave_c_A_B = create_toggle_trigger_range(
        scenario,
        name="START_A_B_WAVE",
        start_trigger_name="adv_evergreen_mangonel_a_z_c",
        end_trigger_name="adv_evergreen_longsworman_b_z_c",
        enable=True
)
activation_wave_c_C = create_toggle_trigger_range(
        scenario,
        name="START_C_WAVE",
        start_trigger_name="adv_evergreen_crossbow_c_z_c",
        end_trigger_name="adv_evergreen_sew_c_z_c",
        enable=True
)
activation_wave_ambush = create_toggle_trigger_range(
        scenario,
        name="START_ambush_WAVE",
        start_trigger_name="adv_evergreen_ambush_Mangudai",
        end_trigger_name= "adv_evergreen_ambush_hand_canon",
        enable=True
)


for i in range(len(supp_trigger_names)):
    trigger_name = supp_trigger_names[i] + "_activation_condition"
    activation_support_id = create_toggle_trigger_range(
        scenario,
        name=trigger_name,
        start_trigger_name=supp_trigger_names[i],
        end_trigger_name=supp_trigger_names[i],
        enable=True,
    )
    support_add_condition = scenario.trigger_manager.get_trigger(activation_support_id)

    # On définit check_unit, check_attribute, unit_quantity correctement
    if i == 0:
        check_unit = [list_unit[0], list_unit[1]]
        check_attribute = [list_attribute[0], list_attribute[1]]
        unit_quantity = [amount_mangonel, amount_knight]
    elif i == 1 or i == 2:
        check_unit = [list_unit[2], list_unit[3]]
        check_attribute = [list_attribute[2], list_attribute[3]]
        unit_quantity = [amount_battalion_teuton_knights, amount_longswordman]
    else:
        check_unit = [list_unit[4], list_unit[5]]
        check_attribute = [list_attribute[4], list_attribute[5]]
        unit_quantity = [amount_bf_crossbow, amount_sew]

    # Boucle accumulate_attribute
    for y in range(len(check_unit)):
        support_add_condition.new_condition.accumulate_attribute(
            source_player=P8,
            attribute=check_attribute[y],
            quantity=unit_quantity[y],
            inverted=False,
        )

    # Optionnel : gestion objects_in_area sauf i == 3
    if i != 3:
        for j in range(len(check_unit)):
            support_add_condition.new_condition.objects_in_area(
                source_player=P8,
                object_list=check_unit[j],
                **area.select_entire_map().to_dict(),
                quantity=1,
                inverted=True,
            )
activation_wave_support = create_toggle_trigger_range(
        scenario,
        name="START_support_WAVE",
        start_trigger_name="adv_evergreen_skirmisher_a_z_c_s_activation_condition",
        end_trigger_name= "adv_evergreen_slinger_c_z_c_s_activation_condition",
        enable=True
)
#adv_evergreen_surprise_camel_Archer_b_z_c_s
active_ambush_condition = trigger_manager.get_trigger(activation_wave_ambush)
active_ambush_condition.new_condition.timer(
    timer=timer_ambush,
)
active_ambush_condition.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.WATCH_TOWER.ID,
    location_x=ambush_coord_b_area[0],
    location_y=ambush_coord_b_area[1],
)
active_ambush_condition.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.WATCH_TOWER.ID,
    location_x=ambush_coord_b_area[2],
    location_y=ambush_coord_b_area[3],
)
active_ambush_condition.new_effect.display_instructions(
    source_player=P1,
    object_list_unit_id=UnitInfo.LONG_SWORDSMAN.ID,
    message=text_ambush,
    display_time=60,
)

list_active=[activation_wave_c_MID,activation_wave_c_A_B,activation_wave_c_C,activation_wave_ambush,activation_wave_support,trigger_id_tent]
add_timer = trigger_manager.get_trigger(activation_wave_c_A_B)
add_timer_2 = trigger_manager.get_trigger(activation_wave_c_C)
add_timer.new_condition.timer(
    timer=spawn_timer,
)
add_timer_2.new_condition.timer(
    timer=spawn_timer_C,
)

for i in range (len(list_active)):
    evergreen_unlock_c_area.new_effect.activate_trigger(
        trigger_id=list_active[i],
    )


blacksmith_zone = get_blacksmith_zone(scenario, taille=10)
print(blacksmith_zone)
blacksmith_X_A = blacksmith_zone['blacksmith_X_A']
blacksmith_Y_A = blacksmith_zone['blacksmith_Y_A']
blacksmith_X_B = blacksmith_zone['blacksmith_X_B']
blacksmith_Y_B = blacksmith_zone['blacksmith_Y_B']


for y in range(1,8):
    player = Liste_joueur[y]
    trigger_name_check=f"Area blacksmith detection positive {player}"
    trigger_name_revcheck = f"Area blacksmith detection negative {player}"
    list_blacksmith_function_name.append(trigger_name_check)
    list_blacksmith_function_name.append(trigger_name_revcheck)
    activate_blacksmith.append(trigger_name_check)
    zone_detection = trigger_manager.add_trigger(
        name=trigger_name_check,
        enabled=False,
        looping=True,
    )
    zone_revdetection = trigger_manager.add_trigger(
        name=trigger_name_revcheck,
        enabled=False,
        looping=True,
    )
    trigger_id_blacksmith_area = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_check), None)
    trigger_id_blacksmith_revarea = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == trigger_name_revcheck), None)
    zone_detection.new_condition.objects_in_area(
        source_player=player,
        quantity=1,
        inverted=False,
        area_x1=blacksmith_X_A,
        area_y1=blacksmith_Y_A,
        area_x2=blacksmith_X_B,
        area_y2=blacksmith_Y_B,
    )
    zone_detection.new_effect.modify_resource(
        source_player=P8,
        tribute_list=Attribute.UNUSED_RESOURCE_104,
        quantity=1,
        operation=Operation.ADD,
    )
    zone_detection.new_effect.deactivate_trigger(
        trigger_id=trigger_id_blacksmith_area
    )
    zone_detection.new_effect.activate_trigger(
        trigger_id=trigger_id_blacksmith_revarea
    )
####################### pour le rev
    zone_revdetection.new_condition.objects_in_area(
        source_player=player,
        quantity=1,
        inverted=True,
        area_x1=blacksmith_X_A,
        area_y1=blacksmith_Y_A,
        area_x2=blacksmith_X_B,
        area_y2=blacksmith_Y_B,
    )
    zone_revdetection.new_effect.modify_resource(
        source_player=P8,
        tribute_list=Attribute.UNUSED_RESOURCE_104,
        quantity=1,
        operation=Operation.SUBTRACT,
    )
    zone_revdetection.new_effect.deactivate_trigger(
        trigger_id=trigger_id_blacksmith_revarea
    )
    zone_revdetection.new_effect.activate_trigger(
        trigger_id=trigger_id_blacksmith_area
    )
blacksmith_defence_trigger = trigger_manager.add_trigger(
        name=blacksmith_defence,
        enabled=False,
        looping=True,
)
activate_blacksmith.append(blacksmith_defence)
list_blacksmith_function_name.append(blacksmith_defence)
blacksmith_defence_trigger.new_condition.timer(
    timer=blacksmith_timer_spawn,
)
blacksmith_defence_trigger.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_104,
    quantity=1,
)
blacksmith_defence_trigger.new_effect.display_instructions(
    display_time=BL_D_TIME,
    message=BL_WARNING,
    object_list_unit_id=UnitInfo.PALADIN.ID,
    source_player=P8,
    instruction_panel_position=0,

)
for i in range (0,amount_paladin):
    blacksmith_defence_trigger.new_effect.create_garrisoned_object(
        source_player=P8,
        object_list_unit_id=BuildingInfo.BLACKSMITH.ID,
        object_list_unit_id_2=UnitInfo.PALADIN.ID,
        area_x1=blacksmith_X_A,
        area_y1=blacksmith_Y_A,
        area_x2=blacksmith_X_B,
        area_y2=blacksmith_Y_B,
    )
blacksmith_death = trigger_manager.add_trigger(
        name=Blacksmith_dead,
        enabled=False,
        looping=False,
)
blacksmith_death.new_condition.objects_in_area(
    source_player=P8,
    object_list=BuildingInfo.BLACKSMITH.ID,
    **area.select_entire_map().to_dict(),
    object_state=ObjectState.DYING,
    quantity=1,
)
blacksmith_death.new_effect.display_instructions(
    source_player=P1,
    message=BL_destroy,
    instruction_panel_position=1,
    display_time=BL_death_time_text,
    object_list_unit_id=UnitInfo.CHAMPION.ID,
)


ID_stop_text = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == blacksmith_defence), None)
list_blacksmith_function_name.append(blacksmith_defence)
list_blacksmith_function_name.append(Blacksmith_dead)
blacksmith_death.new_effect.deactivate_trigger(
    trigger_id=ID_stop_text,
)

activate_blacksmith.append(Blacksmith_dead)
activation_blacksmith = trigger_manager.add_trigger(
    name="START BLACKSMITH",
    enabled=False,
    looping=False,
)
print(f"Activate blackmist composition: {activate_blacksmith}")
ID_for_activation_zone_c = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "START BLACKSMITH"), None)
i = 0
for y in range (len(activate_blacksmith)):
    trigger_id_blacksmith_area = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == activate_blacksmith[y]), None)
    activation_blacksmith.new_effect.activate_trigger(
        trigger_id=trigger_id_blacksmith_area,
    )

evergreen_unlock_c_area.new_effect.activate_trigger(
        trigger_id=ID_for_activation_zone_c,
 )

x, y = coordinate_c_area[6], coordinate_c_area[7]
size = 5

xa, xb, ya, yb = calculate_square_bounds(x, y, size)
bombard_area_detection = trigger_manager.add_trigger(
        name=T_name_cart[0],
        enabled=False,
        looping=False,
)
for p in range (1,8):
    player=Liste_joueur[p]
    bombard_area_detection.new_condition.objects_in_area(
        source_player=player,
        object_list=HeroInfo.EMPEROR_IN_A_BARREL.ID,
        quantity=1,
        area_x1=xa,
        area_x2=xb,
        area_y1=ya,
        area_y2=yb,
    )
    bombard_area_detection.new_effect.remove_object(
        source_player=player,
        object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
        **area.select_entire_map().to_dict(),
        object_state=ObjectState.ALIVE,
    )
    if p != 7:
        bombard_area_detection.new_condition.or_()
    else:
        break
bombard_area_detection.new_effect.display_instructions(
    message="<AQUA>The cart has reached the area, bombard tower has been greetly damaged",
    object_list_unit_id=UnitInfo.ARCHER.ID,
    display_time=60,
)
bombard_area_detection.new_effect.damage_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.BOMBARD_TOWER.ID,
    quantity=15000,
    **area.select_entire_map().to_dict()
)

spawn_cart = trigger_manager.add_trigger(
        name=T_name_cart[1],
        enabled=False,
        looping=False,
)
spawn_cart.new_effect.modify_attribute(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    object_attributes=ObjectAttribute.MOVEMENT_SPEED,
    quantity=carts_speed_reduce,
    operation=Operation.DIVIDE,
)
spawn_cart.new_effect.modify_attribute(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    object_attributes=ObjectAttribute.HIT_POINTS,
    quantity=hp_cart,
    operation=Operation.SET,
)
spawn_cart.new_effect.modify_attribute(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
    quantity=1,
    message=name_cart,
    operation=Operation.SET,
)
spawn_cart.new_effect.modify_attribute(
    source_player=P1,
    object_list_unit_id=BuildingInfo.BLACKSMITH.ID,
    object_attributes=ObjectAttribute.GARRISON_CAPACITY,
    quantity=1,
    operation=Operation.SET,
)
spawn_cart.new_effect.create_garrisoned_object(
    source_player=P1,
    object_list_unit_id=BuildingInfo.BLACKSMITH.ID,
    object_list_unit_id_2=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    **area.select_entire_map().to_dict(),
)
spawn_cart.new_effect.create_garrisoned_object(
    source_player=P1,
    object_list_unit_id=BuildingInfo.BLACKSMITH.ID,
    object_list_unit_id_2=OtherInfo.FLARE.ID,
    **area.select_entire_map().to_dict(),
)
spawn_cart.new_effect.task_object(
    source_player=P1,
    object_list_unit_id=BuildingInfo.BLACKSMITH.ID,
    **area.select_entire_map().to_dict(),
    action_type=ActionType.UNGARRISON,
)
non_selectable  = trigger_manager.add_trigger(
        name=T_name_cart[2],
        enabled=False,
        looping=False,
)
non_selectable.new_condition.objects_in_area(
    source_player=P1,
    object_list=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    **area.select_entire_map().to_dict(),
    quantity=1,
)
non_selectable.new_effect.disable_object_selection(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    **area.select_entire_map().to_dict(),
)
non_selectable.new_effect.disable_object_deletion(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    **area.select_entire_map().to_dict(),
)
cart_moving_to_tower  = trigger_manager.add_trigger(
        name=T_name_cart[3],
        enabled=False,
        looping=True,
)
cart_moving_to_tower.new_condition.objects_in_area(
    source_player=P1,
    object_list=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    **area.select_entire_map().to_dict(),
    quantity=1,
)
cart_moving_to_tower.new_effect.task_object(
    source_player=P1,
    location_x=coordinate_c_area[6],
    location_y=coordinate_c_area[7],
    **area.select_entire_map().to_dict(),
    action_type=ActionType.MOVE,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
)
text_trigger_id = create_display_text_trigger(
        scenario,
        name=bomb_objective_name,
        description_order=bomb_description_order,
        text=bomb_description_text,
)

trigger_2 = next((trigger for trigger in trigger_manager.triggers if trigger.name == bomb_objective_name), None)
if trigger_2 is not None:
    trigger_2.remove_condition(condition_index=0)
trigger_2.new_condition.objects_in_area(
    source_player=P1,
    object_list=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    area_x1=xa,
    area_x2=xb,
    area_y1=ya,
    area_y2=yb,
    quantity=1,
)
T_name_cart.append(bomb_objective_name)
activation_bomb_evergreen_c = create_toggle_trigger_range(
        scenario,
        name="BOMB CART EVERGREEN C",
        start_trigger_name=T_name_cart[0],
        end_trigger_name= T_name_cart[-1],
        enable=True
)
#adv_evergreen_surprise_camel_Archer_b_z_c_s
active_bomb_condition = trigger_manager.get_trigger(activation_bomb_evergreen_c)
activation_blacksmith.new_effect.activate_trigger(
        trigger_id=activation_bomb_evergreen_c,
)

active_bomb_condition.new_condition.timer(
    timer=timer_cart,
)
active_bomb_condition.new_effect.display_instructions(
    source_player=P1,
    object_list_unit_id=HeroInfo.EMPEROR_IN_A_BARREL.ID,
    message="<BLUE>HEY YOU! Help me reach that tower! I have a device that will completely destroy it",
    display_time=40,
    instruction_panel_position=0,
)

for move in range (len(list_blacksmith_function_name)):
    trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == list_blacksmith_function_name[move]), None)
    print(f"test debug {list_blacksmith_function_name[move]}")
    trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "----B ADV MISSION EVERGREEN EXPOSITION C-----"), None)
    trigger_manager.move_triggers([trigger_id_1], trigger_id_2)
turn_off_blacksmith= create_toggle_trigger_range(
    scenario,
    name="Turn off blacksmith evergreen",
    start_trigger_name="----E ADV MISSION EVERGREEN EXPOSITION B-----",
    end_trigger_name="----B ADV MISSION EVERGREEN EXPOSITION C-----",
    enable=False,
)
blacksmith_death.new_effect.activate_trigger(
    trigger_id=turn_off_blacksmith,
)
trigger_id_1 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "Turn off blacksmith evergreen"), None)
trigger_id_2 = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == "----B ADV MISSION EVERGREEN EXPOSITION C-----"), None)
trigger_manager.move_triggers([trigger_id_1], trigger_id_2)

end_zone_c_evergreen = trigger_manager.add_trigger(
    name=end_zone_c,
    enabled=False,
    looping=False,
)
### end of the C area in EVERGREEN
#
#
#
#
#
#
#
#
#
#
#
#
#
#
###
# Zone bonus
start_bonus_area = "----B ADV MISSION EVERGREEN EXPOSITION BONUS-----"
end_bonus_area = "----E ADV MISSION EVERGREEN EXPOSITION BONUS-----"
P_X = 200
P_X_2 = 202
P_Y = 146
P_Y_2 = 141
K_X = 211
K_Y= 186

boss_spawn_time = 5
spawn_evergreen_script_drakar = "Script attack"
spawn_evergreen_drakar = "Bonus Area boss evergreen"
Bonus_area_evergreen_text="<ORANGE>By entering this area, you agree to fight me, if you can defeat me I give you 2000 stones"
reward_name="boss reward evergreen bonus area"
reward_txt="<ORANGE>OH NO I'M SINKING !!!! I'm sorry guys and girls I don't have 2000 stone only 1200, but... I can give you those projectile for your siege weapon"
reward_txt_2="Instead of receiving 2000 stones, you just get 1200 stones and +6 damages to your sieges weapons"
Bonus_area_evergreen_time=60
script_attack_evergreen_longboat="""void longboat_evergreen_boss() {
xsEffectAmount(cSetAttribute, 686, 8, 256*3 + 5, 8);
}
"""
evergreen_bonus_area_start = trigger_manager.add_trigger(
    name=start_bonus_area,
    enabled=False,
    looping=False,
)
evergreen_bonus_area_check = trigger_manager.add_trigger(
    name=start_bonus_area,
    enabled=False,
    looping=False,
)
for i in range (1,8):
    player=Liste_joueur[i]
    evergreen_bonus_area_check.new_condition.objects_in_area(
        source_player=player,
        quantity=1,
        inverted=False,
        area_x1=P_X,
        area_x2=P_X_2,
        area_y1=P_Y,
        area_y2=P_Y_2,
    )
    if i != 7:
        evergreen_bonus_area_check.new_condition.or_()
evergreen_bonus_area_check.new_effect.display_instructions(
    source_player=P8,
    object_list_unit_id=UnitInfo.LONGBOAT.ID,
    message=Bonus_area_evergreen_text,
    display_time=Bonus_area_evergreen_time,
)
evergreen_bonus_area_stat = modify_attributes_trigger( #Gun form
        scenario,
        name="Evergreen bonus boss",
        player=PlayerId.EIGHT,
        units=[
            {
                "unit": HeroInfo.ARCHER_OF_THE_EYES.ID,
                "modifications": [
                    [ObjectAttribute.STANDING_GRAPHIC, 2872, Operation.SET],
                    [ObjectAttribute.DYING_GRAPHIC, 2871, Operation.SET],
                    [ObjectAttribute.WALKING_GRAPHIC, 2873, Operation.SET],
                    [ObjectAttribute.RUNNING_GRAPHIC, 2873, Operation.SET],
                    [ObjectAttribute.MAX_RANGE, 10, Operation.SET],
                    [ObjectAttribute.COMBAT_ABILITY, 0, Operation.SET],
                    [ObjectAttribute.MAX_TOTAL_MISSILES,4,Operation.SET],
                    [ObjectAttribute.TOTAL_MISSILES,4, Operation.SET],
                    [ObjectAttribute.HIT_POINTS,2500, Operation.SET],
                    [ObjectAttribute.PROJECTILE_UNIT,374, Operation.SET],
                    [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Evergreen longboat"]
                ],
            },
{
                "unit": 374,
                "modifications": [
                    [ObjectAttribute.MOVEMENT_SPEED, 5, Operation.SET],
                    [ObjectAttribute.BLOOD_UNIT, 692, Operation.SET],
                    [ObjectAttribute.DEAD_UNIT_ID, 361, Operation.SET],
                ],
            }
    ]
)
evergreen_spawn_script = trigger_manager.add_trigger(
    name=spawn_evergreen_script_drakar,
    enabled=False,
    looping=False,
)
evergreen_spawn_script.new_effect.script_call(
    message=script_attack_evergreen_longboat,
)
activation_bonus_area = create_toggle_trigger_range(
        scenario,
        name="START_bonus_area_stat_and_config",
        start_trigger_name=start_bonus_area,
        end_trigger_name= spawn_evergreen_script_drakar,
        enable=True
)
evergreen_spawn_boss = trigger_manager.add_trigger(
    name=spawn_evergreen_drakar,
    enabled=False,
    looping=False,
)
evergreen_spawn_boss.new_condition.timer(
    timer=boss_spawn_time,
)
evergreen_spawn_boss.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=HeroInfo.ARCHER_OF_THE_EYES.ID,
    location_x=K_X,
    location_y=K_Y,
)
coordinate_map=area.select_entire_map().to_dict(),

ID_for_a_boss_spawn= next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == spawn_evergreen_drakar), None)
evergreen_bonus_area_check.new_effect.activate_trigger(
    trigger_id=ID_for_a_boss_spawn,
)
evergreen_reward_boss = trigger_manager.add_trigger(
    name=reward_name,
    enabled=False,
    looping=False,
)
evergreen_reward_boss.new_condition.objects_in_area(
    source_player=P8,
    object_list=HeroInfo.ARCHER_OF_THE_EYES.ID,
    **area.select_entire_map().to_dict(),
    object_state=ObjectState.DYING,
    quantity=1,

)
for i in range (1,8):
    evergreen_reward_boss.new_effect.tribute(
        source_player=PlayerId.GAIA,
        target_player=Liste_joueur[i],
        tribute_list=Attribute.STONE_STORAGE,
        quantity=1200,
    )
    siege_script=f"void siege_script_{Liste_joueur[i]}()"
    siege_script+="{"
    siege_script+=f"xsEffectAmount(cAddAttribute, 913, 9, 256*4 + 5, {Liste_joueur[i]});"
    siege_script +=f"xsEffectAmount(cAddAttribute, 955, 9, 256*3 + 5, {Liste_joueur[i]});"
    siege_script +="}"
    evergreen_reward_boss.new_effect.script_call(
        message=siege_script,
    )

evergreen_reward_boss.new_effect.remove_object(
    source_player=P8,
    **area.select_entire_map().to_dict(),
    object_list_unit_id=HeroInfo.ARCHER_OF_THE_EYES.ID,
    object_state=ObjectState.DYING,
)
evergreen_reward_boss.new_effect.display_instructions(
    source_player=P8,
    message=reward_txt,
    object_list_unit_id=UnitInfo.LONGBOWMAN.ID,
    instruction_panel_position=0,
    display_time=display_time

)
evergreen_reward_boss.new_effect.display_instructions(
    source_player=P8,
    message=reward_txt_2,
    instruction_panel_position=1,
    display_time=display_time

)
ID_for_a_boss_spawn= next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == reward_name), None)
evergreen_bonus_area_check.new_effect.activate_trigger(
    trigger_id=ID_for_a_boss_spawn,
)
### end of the C area in EVERGREEN
#
#
#
#
#
#
#
#
#
#
#
#
#
#
###
start_last_area = "----B ADV MISSION EVERGREEN LAST AREA-----"
end_last_area = "----E ADV MISSION EVERGREEN EXPOSITION LAST AREA-----"
name_unlock_last_area ="Last area evergreen"
timer_text_last_area = 120
display_text_instruction_1 = "<AQUA>The final area is unlocked, BURN THE DONJON and complete this mission. You have reached the imperial age and everyone receives 800 stones."
display_text_instruction_2 = "<AQUA>If you lack the firepower to break enemy defenses, we can head to the bonus area to gather some"
Stone_reward=800
name_attribute_d="Zone d attribute evergreen"
taunt_hyper_shotgun_janissary="<ORANGE>Our employer has provided us with a new rifle to spice things up. I hope you don’t mind turning into Swiss cheese."
taunt_timer=120
id_collector=[]
################################## Spawn function
tower_location_zone_d = [
    175,193, #A
    180,200, #b
    127,216, #C
    162,200 #NORMAND
]
#---------- Tower c
timer_C_tower=30
spawn_time_banner_kipchak = 22
spawn_rate_banner_kipchak = 1
amount_banner_kipchak= 9
spawn_time_cav_archer = 11
spawn_rate_cav_archer = 10
amount_cav_archer=80
spawn_time_scorpion= 33
spawn_rate_scorpion=5
amount_scorpion=15
#--------------------- Tower B
spawn_rate_cavalier=10
spawn_time_cavalier=20
amount_cavalier=80
spawn_time_tarkan=20
spawn_rate_tarkan=5
amount_tarkan=50
#------------------ Tower C
timer_AB_tower_spawn=120
spawn_rate_coustiller=20
spawn_time_coustiller=25
amount_coustiller=100
spawn_time_multi_shot_arambai=25
spawn_rate_multi_shot_arambai=10
amount_multi_shot_arambai=50
#---------------------- Norman dungeon
timer_last_activation_evergreen= 180
hyper_janisary_spawn_time=12
hyper_janisary_spawn_rate=5
amount_hyper_janisary=60
Limit_hyper_shotgun_janisary=16
#------------------------- support
#--- A tower
spawn_time_cretan_archer=40
spawn_rate_cretan_archer=20

spawn_time_instant_attack_pikeman= 50
spawn_rate_instant_attack_pikeman = 15
#--- B tower
spawn_time_e_huskarl= 14
spawn_rate_e_huskarl= 15
spawn_time_EJW=  19
spawn_rate_EJW = 15
spawn_time_EKD= 21
spawn_rate_EKD=15
#---- c tower
spawn_time_f_hand_canon = 12
spawn_rate_f_hand_canon = 12
lines_evergreen_D = ["void Buff_D_evergreen(){"]
unlock_c_area_reward= 1200
for unit_id in XS_general_ID:
    lines_evergreen_D.append(f"xsEffectAmount(cMulAttribute, {unit_id}, 10, 0.90, 8);")
    lines_evergreen_D.append(f"xsEffectAmount(cMulAttribute, {unit_id}, 0, 1.20, 8);")
# Ajouts fixes pour l’unité 785
lines_evergreen_D += [
    "xsEffectAmount(cMulAttribute, 557, 9, 256*3 * 4, 8);",
    f"xsEffectAmount(cAddAttribute, {BuildingInfo.DONJON.ID}, 9, 256*3 * 10, 8);",
    "}"
]
spawn_triggers= []
script_buff_d = "\n".join(lines_evergreen_D)
script_banner_kipchak = f"void banner_kipchak()"
script_banner_kipchak += """ {
    xsTaskAmount(0, 2);
    xsTaskAmount(1, 1);
    xsTaskAmount(2, 5);
    xsTaskAmount(3, 0);
    xsTaskAmount(4, 9);
    xsTaskAmount(5, 5);
    xsTaskAmount(6, 4);
    xsTask(1231, 155, 936, 8);
}
"""
spawn_data = [
    #Building                   #Unit                #Cooridnate of the tower   #Timer  #Amount   #The res that will count or None for support # Name of the trigger
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.KIPCHAK.ID,tower_location_zone_d[4] ,tower_location_zone_d[5] #C TOWER
    ,spawn_time_banner_kipchak,amount_banner_kipchak,Attribute.UNUSED_RESOURCE_140,spawn_rate_banner_kipchak, "adv_evergreen_banner_kipchack_d"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.CAVALRY_ARCHER.ID,tower_location_zone_d[4] ,tower_location_zone_d[5]
    ,spawn_time_cav_archer,amount_cav_archer,Attribute.UNUSED_RESOURCE_141,spawn_rate_cav_archer, "adv_evergreen_cav_archer_d"],
    [BuildingInfo.SEA_TOWER.ID, UnitInfo.SCORPION.ID,tower_location_zone_d[4] ,tower_location_zone_d[5]
    ,spawn_time_scorpion,amount_scorpion,Attribute.UNUSED_RESOURCE_142,spawn_rate_scorpion, "adv_evergreen_scorpion_d"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.CAVALIER.ID,tower_location_zone_d[0] ,tower_location_zone_d[1] # A tower
    ,spawn_time_cavalier,amount_cavalier,Attribute.UNUSED_RESOURCE_143,spawn_rate_cavalier, "adv_evergreen_cavalier_d"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.CAVALIER.ID,tower_location_zone_d[0] ,tower_location_zone_d[1]
    ,spawn_time_tarkan,amount_tarkan,Attribute.UNUSED_RESOURCE_144,spawn_rate_tarkan, "adv_evergreen_tarkan_d"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.COUSTILLIER.ID,tower_location_zone_d[2] ,tower_location_zone_d[3] #B TOWER
    ,spawn_time_coustiller,amount_coustiller,Attribute.UNUSED_RESOURCE_145,spawn_rate_coustiller, "adv_evergreen_coustiller_d"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.ELITE_ARAMBAI.ID,tower_location_zone_d[2] ,tower_location_zone_d[3]
    ,spawn_time_multi_shot_arambai,amount_multi_shot_arambai,Attribute.UNUSED_RESOURCE_146,spawn_rate_multi_shot_arambai, "adv_evergreen_arambai_d"],

    [BuildingInfo.DONJON.ID, UnitInfo.ELITE_JANISSARY.ID,tower_location_zone_d[6] ,tower_location_zone_d[7]
    ,hyper_janisary_spawn_time,amount_hyper_janisary,Attribute.UNUSED_RESOURCE_147,hyper_janisary_spawn_rate, "adv_evergreen_hyper_shotgun_janisary_d"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.CRETAN_ARCHER.ID, tower_location_zone_d[0] ,tower_location_zone_d[1],
     spawn_time_cretan_archer,   None, None,  spawn_rate_cretan_archer, "adv_evergreen_SUPP_cretan_archer_d_area"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.PIKEMAN.ID, tower_location_zone_d[0] ,tower_location_zone_d[1],
     spawn_time_instant_attack_pikeman,   None, None,  spawn_rate_instant_attack_pikeman, "adv_evergreen_SUPP_Instant_attack_pikeman_d_area"],

    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.ELITE_HUSKARL.ID, tower_location_zone_d[2] ,tower_location_zone_d[3],
     spawn_time_e_huskarl,   None, None,  spawn_rate_e_huskarl, "adv_evergreen_SUPP_huskarl_d_area"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.ELITE_JAGUAR_WARRIOR.ID, tower_location_zone_d[2] ,tower_location_zone_d[3],
     spawn_time_EJW,   None, None,  spawn_rate_EJW, "adv_evergreen_SUPP_EJW_d_area"],
    [BuildingInfo.GUARD_TOWER.ID, UnitInfo.ELITE_KONNIK_DISMOUNTED.ID, tower_location_zone_d[2] ,tower_location_zone_d[3],
     spawn_time_EKD,   None, None,  spawn_rate_EKD, "adv_evergreen_SUPP_EDK_d_area"],

    [BuildingInfo.SEA_TOWER.ID, UnitInfo.HAND_CANNONEER.ID, tower_location_zone_d[4] ,tower_location_zone_d[5],
     spawn_time_f_hand_canon,   None, None,  spawn_rate_f_hand_canon, "adv_evergreen_SUPP_hand_canon_d_area"],
]
id_compo_wave_d = []
Evergreen_composition_d = [
    "<ORANGE> " + line for line in [
        "DEFENCE COMPOSITION LAST AREA",
        f"{amount_banner_kipchak} banner Kipchak",
        f"{amount_cav_archer} cavalry archer",
        f"{amount_scorpion} scorpion",
        f"{amount_cavalier} cavalier",
        f"{amount_multi_shot_arambai} Multi shot arambai",
        f"{amount_coustiller} coustiller",
        f"{amount_hyper_janisary} hyper shotgun janissary",
        "Support: cretan archer, instant attack pikeman, elite huskarl, elite jaguar warrior, elite dismounted konnik, fast hand cannoneer",
        "Tent support : Ghulam, Chakram Thrower",
        "Blacksmith protector: Paladin"
    ]
]
evergreen_last_area_objective=["+ Destroy the donjon to win the mission","- Destroy the sea tower (800 stones reward)"]
evergreen_start_limit = trigger_manager.add_trigger(
    name=start_last_area,
    enabled=False,
    looping=False,
)
unlock_last_area_evergreen = trigger_manager.add_trigger(
    name=name_unlock_last_area,
    enabled=False,
    looping=False,
)
for o in range (len(Evergreen_composition_d)):
    timer = 5 + o
    wave_compo_name = f"Zone d compo {o}"
    id_compo_wave_d.append(wave_compo_name)
    evergreen_wave_compo_d = trigger_manager.add_trigger(
        name=wave_compo_name,
        enabled=False,
        looping=False,
    )
    evergreen_wave_compo_d.new_condition.timer(
        timer=timer,
    )
    wave_compo_name_list.append(wave_compo_name)
    for p in range (1,8):
        player = Liste_joueur[p]
        evergreen_wave_compo_d.new_effect.send_chat(
            source_player=player,
            message=Evergreen_composition_d[o],
        )
for i in range (len(evergreen_last_area_objective)):
    objective_last_area = create_display_text_trigger(
        scenario,
        name="Display last area evergreen objective",
        description_order=199 + i,
        text=evergreen_last_area_objective[i],
    )
    id_collector.append(objective_last_area)


turn_off_area_c_evergreen = create_toggle_trigger_range(
        scenario,
        name="Turn off area C",
        start_trigger_name=start_zone_c,
        end_trigger_name= end_zone_c,
        enable=False,
)
unlock_last_area_evergreen.new_effect.activate_trigger(
    trigger_id=turn_off_area_c_evergreen,
)
unlock_last_area_evergreen.new_condition.accumulate_attribute(
    source_player=P8,
    attribute=Attribute.UNUSED_RESOURCE_105,
    quantity=2,

)
unlock_last_area_evergreen.new_effect.remove_object(
    source_player=P8,
    **area.select_entire_map().to_dict(),
    object_list_unit_id=BuildingInfo.GUARD_TOWER.ID,
)
unlock_last_area_evergreen.new_effect.remove_object(
    source_player=P8,
    **area.select_entire_map().to_dict(),
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
)
unlock_last_area_evergreen.new_effect.display_instructions(
    source_player=P8,
    message=display_text_instruction_1,
    display_time=timer_text_last_area,
    instruction_panel_position=0,
    object_list_unit_id=UnitInfo.ARCHER.ID,
)
unlock_last_area_evergreen.new_effect.display_instructions(
    source_player=P8,
    message=display_text_instruction_2,
    display_time=timer_text_last_area,
    instruction_panel_position=1,
)

unlock_last_area_evergreen.new_effect.activate_trigger(
    trigger_id=activation_bonus_area,
)
for i in range (1,8):
    player=Liste_joueur[i]
    unlock_last_area_evergreen.new_effect.research_technology(
        source_player=player,
        technology=TechInfo.IMPERIAL_AGE.ID,
        force_research_technology=True,
    )
    unlock_last_area_evergreen.new_effect.tribute(
        source_player=player,
        tribute_list=Attribute.STONE_STORAGE,
        quantity=Stone_reward,
    )
unlock_last_area_evergreen.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.GUARD_TOWER.ID,
    location_x=tower_location_zone_d[0],
    location_y=tower_location_zone_d[1],
)
unlock_last_area_evergreen.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.GUARD_TOWER.ID,
    location_x=tower_location_zone_d[2],
    location_y=tower_location_zone_d[3],
)
unlock_last_area_evergreen.new_effect.remove_object(
    source_player=P8,
    area_x1=132,
    area_x2=149,
    area_y1=172,
    area_y2=187,
    object_type=ObjectType.BUILDING,
    
)
unlock_last_area_evergreen.new_effect.create_object(
    source_player=P8,
    object_list_unit_id=BuildingInfo.SEA_TOWER.ID,
    location_x=tower_location_zone_d[4],
    location_y=tower_location_zone_d[5],
)
unlock_last_area_evergreen.new_effect.script_call(
    message=script_banner_kipchak
)
unlock_last_area_evergreen.new_effect.script_call(
    message=script_buff_d,
)
ID_unlock = next((i for i, trigger in enumerate(trigger_manager.triggers) if trigger.name == name_unlock_last_area), None)
evergreen_unlock_c_area.new_effect.activate_trigger(
    trigger_id=ID_unlock,
)
trigger = modify_attributes_trigger(
    scenario,
    name=name_attribute_d,
    player=PlayerId.EIGHT,
    units=[
        {
            "unit": UnitInfo.PIKEMAN.ID,
            "modifications": [
                [ObjectAttribute.HIT_POINTS, 360, Operation.SET],
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Instant pikeman attack"],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 2 , Operation.SET],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 12 , Operation.DIVIDE],
            ],
        },
{
            "unit": UnitInfo.ELITE_JANISSARY.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Hyper shotgun janisary"],
                [ObjectAttribute.TOTAL_MISSILES, 5, Operation.SET],
                [ObjectAttribute.MAX_TOTAL_MISSILES, 5, Operation.SET],

            ],
        },
{
            "unit": UnitInfo.ELITE_ARAMBAI.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID, 0, Operation.SET,"Multi shot arambai"],
                [ObjectAttribute.HIT_POINTS, 216, Operation.SET],
                [ObjectAttribute.TOTAL_MISSILES, 5, Operation.SET],
                [ObjectAttribute.MAX_TOTAL_MISSILES, 5, Operation.SET],
                [ObjectAttribute.COMBAT_ABILITY,16,Operation.SET],
            ],
        },
{
            "unit": UnitInfo.HAND_CANNONEER.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Fast fire hand canon"],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 2, Operation.DIVIDE],
                [ObjectAttribute.HIT_POINTS, 180,Operation.SET],
            ],
        },
{
            "unit": UnitInfo.KIPCHAK.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Banner Kipchak"],
                [ObjectAttribute.COMBAT_ABILITY, 48, Operation.SET],
                [ObjectAttribute.HIT_POINTS, 180,Operation.SET],
            ],
    },
{
            "unit": BuildingInfo.DONJON.ID,
            "modifications": [
                [ObjectAttribute.OBJECT_NAME_ID,0,Operation.SET,"Destroy this tower to win"],
                [ObjectAttribute.HIT_POINTS, 25000, Operation.SET],
                [ObjectAttribute.REGENERATION_RATE, 400,Operation.SET],
                [ObjectAttribute.ATTACK_RELOAD_TIME, 0.16, Operation.SET],
            ],
        },
    ]
)
activate_attribute=trigger.trigger_id
unlock_last_area_evergreen.new_effect.activate_trigger(
    trigger_id=activate_attribute,
)
print (f"spawn data {spawn_data}")
for data in spawn_data:
    trigger = create_spawn_trigger(scenario, data)
    spawn_triggers.append(trigger)
hyper_shotgun_condition = spawn_triggers[7]
print(f"Hyper shotgun janissary {hyper_shotgun_condition}")
hyper_shotgun_condition.new_condition.objects_in_area(
    source_player=P8,
    object_list=UnitInfo.ELITE_JANISSARY.ID,
    quantity=Limit_hyper_shotgun_janisary,
    **area.select_entire_map().to_dict(),
    inverted=True,
)
activation_main_wave_C_tower = create_toggle_trigger_range(
        scenario,
        name="C tower activated",
        start_trigger_name="adv_evergreen_banner_kipchack_d",
        end_trigger_name= "adv_evergreen_scorpion_d",
        enable=True
)
id_collector.append(activation_main_wave_C_tower)
activation_main_wave_C_tower_add = scenario.trigger_manager.get_trigger(activation_main_wave_C_tower)
activation_main_wave_C_tower_add.new_condition.timer(
    timer=timer_C_tower,
)

activation_main_wave_AB_tower = create_toggle_trigger_range(
        scenario,
        name="A and B tower activated",
        start_trigger_name="adv_evergreen_cavalier_d",
        end_trigger_name= "adv_evergreen_arambai_d",
        enable=True
)
id_collector.append(activation_main_wave_AB_tower)
activation_main_wave_AB_tower_add = scenario.trigger_manager.get_trigger(activation_main_wave_AB_tower)
activation_main_wave_AB_tower_add.new_condition.timer(
    timer=timer_AB_tower_spawn,
)
activation_main_wave_NORMAND_tower = create_toggle_trigger_range(
        scenario,
        name="Hyper and supp tower activated",
        start_trigger_name="adv_evergreen_hyper_shotgun_janisary_d",
        end_trigger_name= "adv_evergreen_SUPP_hand_canon_d_area",
        enable=True
)
id_collector.append(activation_main_wave_NORMAND_tower)
activation_main_wave_NORMAND_tower_add = scenario.trigger_manager.get_trigger(activation_main_wave_NORMAND_tower)
activation_main_wave_NORMAND_tower_add.new_condition.timer(
    timer=timer_last_activation_evergreen,
)
activation_compo_wave = create_toggle_trigger_range(
    scenario,
    name="Activate wave compo d area",
    start_trigger_name=id_compo_wave_d[0],
    end_trigger_name=id_compo_wave_d[-1],
    enable=True
)
id_collector.append(activation_compo_wave)
activation_main_wave_NORMAND_tower_add.new_effect.display_instructions(
    message=taunt_hyper_shotgun_janissary,
    object_list_unit_id=UnitInfo.ELITE_JANISSARY.ID,
    instruction_panel_position=0,
    source_player=P8,
    display_time=taunt_timer,
)
for i in range (len(id_collector)):
    unlock_last_area_evergreen.new_effect.activate_trigger(
        trigger_id=id_collector[i]
    )

scenario.write_to_file(output_path)
print (f"test {UnitInfo.CAVALIER.DEAD_ID}")
flag_positions = get_flag_positions(scenario)
#Liste des coordonnées des drapeaux pour pas les oubliers quand je créer mes missions
for flag_key, players_coords in flag_positions.items():
    print(f"{flag_key}:")
    for player_id, coords_list in players_coords.items():
        print(f"  Player {player_id}:")
        for x, y in coords_list:
            print(f"    → (x={x}, y={y})")
