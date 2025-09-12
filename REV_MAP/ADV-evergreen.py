from Main_script import trigger_manager

print("Success")# Le script pose les fonctions de base de la carte
#C'est à dire:
# - Les coordonées des drapeaux pour placer les tours
# - Les coordonnées des drapeaux M pour les pierres
# - Les statistiques de base des joueurs (Workrate, resource, diplomatie, vision)
# - Le menu pour choisir la carte.
#---------------------------------------------------------------------------------------------
quantity_number_0 = 0
quantity_number_3 = 3
quantity_number_8 = 8
quantity_number_9 = 9
quantity_number_10 = 10
quantity_number_32 = 32
quantity_number_35 = 32
quantity_number_40 = 40
quantity_number_60 = 60
quantity_number_500 = 500
quantity_number_50 = 50
quantity_number_2500 = 2500
quantity_number_20000 = 20000
Timer_20s= 20
u = 1
FLAG_O_ID = 2011
FLAG_P_ID = 2012
FLAG_ATHENIAN_2 = 2257
FLAG_ATHENIAN_3 = 2258
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
from pyexpat.errors import messages
from unicodedata import category
#Dictionnaire pour le script
from AoE2ScenarioParser.objects.support.area import Area
from Upgrade_station_dictionnary import technologie_page_desc_icon, technology_cost_icon, special_case_3, special_case_7
from Upgrade_station_dictionnary import Techno_message
from Upgrade_station_dictionnary import Techno_xs
import os
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from flag_utils import get_flag_positions

scenario = AoE2DEScenario.from_file("C:\\Users\\redma\\Games\\Age of Empires 2 DE\\76561198382316787\\resources\\_common\\scenario\\REV 7 VS 1 AI MAP BETA.aoe2scenario")
flag_positions = get_flag_positions(scenario)

os.environ['TCL_LIBRARY'] = r'C:\Users\redma\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\redma\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

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

# Accès au dictionnaire
for flag_name, players_data in flag_positions.items():
    print(f"{flag_name}:")
    for player_id, coords in players_data.items():
        coord_str = ", ".join([f"({x},{y})" for x, y in coords])
        print(f"  Joueur {player_id} : {coord_str}")

Test_trigger = trigger_manager.add_trigger(
    name="Test",
    enabled=True,
    looping=False,
)
scenario.write_to_file(output_path)