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
#trigger_manager = scenario.trigger_manager
max_population= 500
def calculate_square_bounds(center_x, center_y, size):
    """
    Calcule un carré centré autour des coordonnées données, basé sur une taille fournie.

    Args:
        center_x (float | int): Coordonnée X centrale
        center_y (float | int): Coordonnée Y centrale
        size (float | int): Moitié de la largeur/hauteur du carré

    Returns:
        tuple: (square_x_a, square_x_b, square_y_a, square_y_b)
    """
    square_x_a = center_x - size
    square_x_b = center_x + size
    square_y_a = center_y - size
    square_y_b = center_y + size
    return square_x_a, square_x_b, square_y_a, square_y_b


def get_unit_reference_id(scenario: AoE2DEScenario, unit_id: str) -> str:
    """
    Récupère l'attribut reference_id d'une unité via son unit_id.
    Lève une ValueError si l'unité n'existe pas ou si reference_id manquant.
    """
    um = scenario.unit_manager
    # On récupère TOUTES les unités
    all_units = um.get_all_units()
    # Filtre sur l'ID de l’unité
    matching = [u for u in all_units if getattr(u, "unit_id", None) == unit_id]

    if not matching:
        raise ValueError(f"Aucune unité trouvée avec unit_id = '{unit_id}'")

    unit = matching[0]
    ref = getattr(unit, "reference_id", None)
    if ref is None:
        raise ValueError(f"L'unité '{unit_id}' n’a pas d’attribut reference_id")

    return ref
def create_display_text_trigger(scenario, name, description_order, text, display=True):
    trigger = scenario.trigger_manager.add_trigger(
        name=name,
        enabled=False,
        looping=False,
    )

    trigger.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.UNUSED_RESOURCE_359,
        quantity=1000,
        inverted=False,
    )

    trigger.short_description = text
    trigger.display_on_screen = display
    trigger.description_order = description_order

    # 📌 Récupérer et retourner son ID
    trigger_id = next(
        (i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == name),
        None
    )
    return trigger_id
def create_spawn_trigger(scenario,params):
    building_id = params[0]
    unit_id = params[1]
    x = params[2]
    y = params[3]
    timer_value = params[4]
    quantity = params[5]
    attribute = params[6]
    spawn_rate = params[7]
    base_name = params[8]

    trigger = scenario.trigger_manager.add_trigger(
        name=base_name,
        enabled=False,
        looping=True,
    )

    # Ajoute les conditions
    trigger.new_condition.timer(timer=timer_value)
    if attribute is not None:
        trigger.new_condition.accumulate_attribute(
            source_player=PlayerId.EIGHT,
            attribute=attribute,
            quantity=quantity,
            inverted=True
        )
    trigger.new_condition.accumulate_attribute(
        source_player=PlayerId.EIGHT,
        attribute=Attribute.CURRENT_POPULATION,
        inverted=True,
        quantity=max_population,
    )

    # Ajoute les effets
    for _ in range(spawn_rate):
        trigger.new_effect.create_garrisoned_object(
            source_player=PlayerId.EIGHT,
            object_list_unit_id=building_id,
            object_list_unit_id_2=unit_id,
            area_x1=x,
            area_y1=y,
            area_x2=x,
            area_y2=y
        )

    if attribute is not None:
        trigger.new_effect.modify_resource(
            source_player=PlayerId.EIGHT,
            tribute_list=attribute,
            quantity=spawn_rate,
            operation=Operation.ADD
        )


    return trigger

def modify_attributes_trigger(scenario, name, player, units):
    trigger = scenario.trigger_manager.add_trigger(
        name=name,
        enabled=False,
        looping=False,
    )

    for unit_block in units:
        unit_id = unit_block["unit"]
        modifications = unit_block["modifications"]

        for mod in modifications:
            if len(mod) == 3:
                attr, value, operation = mod
                trigger.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_id,
                    object_attributes=attr,
                    operation=operation,
                    quantity=value,
                )
            elif len(mod) == 4:
                attr, value, operation, msg = mod
                trigger.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_id,
                    object_attributes=attr,
                    operation=operation,
                    quantity=value,
                    message=msg,
                )
            else:
                raise ValueError(f"❌ Mauvais format de modification : {mod}")

    return trigger


def create_complex_toggle_trigger(scenario,name, toggle_logic):
    trigger = scenario.trigger_manager.add_trigger(
        name=name,
        enabled=False,
        looping=False,
    )

    for logic_block in toggle_logic:
        if len(logic_block) < 2:
            raise ValueError("Each block must be [True/False, trigger_names...]")

        enable = logic_block[0]
        target_names = logic_block[1:]

        for target_name in target_names:
            target_id = next(
                (i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == target_name),
                None
            )

            if target_id is None:
                print(f"[WARN] Trigger '{target_name}' not found.")
                continue

            if enable:
                trigger.new_effect.activate_trigger(trigger_id=target_id)
            else:
                trigger.new_effect.deactivate_trigger(trigger_id=target_id)

    # ⬇️ Récupération de l’ID
    trigger_id = next(
        (i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == name),
        None
    )

    return trigger_id
def create_toggle_trigger_range(scenario, name, start_trigger_name, end_trigger_name, enable):
    # Trouver les IDs des triggers de début et de fin
    start_id = next((i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == start_trigger_name), None)
    end_id = next((i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == end_trigger_name), None)

    if start_id is None or end_id is None:
        raise ValueError("Start or end trigger name not found.")

    # Assurer l'ordre (au cas où)
    if start_id > end_id:
        start_id, end_id = end_id, start_id

    # Créer le trigger
    trigger = scenario.trigger_manager.add_trigger(
        name=name,
        enabled=False,
        looping=False,
    )

    for i in range(start_id, end_id + 1):
        target_trigger = scenario.trigger_manager.triggers[i]
        if enable:
            trigger.new_effect.activate_trigger(trigger_id=i)
        else:
            trigger.new_effect.deactivate_trigger(trigger_id=i)

    # Retourner l’ID du trigger créé
    trigger_id = next((i for i, t in enumerate(scenario.trigger_manager.triggers) if t.name == name), None)
    return trigger_id
def get_blacksmith_zone(scenario, taille=2):
    BLACKSMITH_ID = 103  # ID de la forge dans AoE2 DE
    TARGET_PLAYER = 8    # Joueur 8

    blacksmith_zone = None

    for units in scenario.unit_manager.units:
        for u in units:
            if isinstance(u, UUID):
                continue
            if u.unit_const == BLACKSMITH_ID and u.player == TARGET_PLAYER:
                # Trouvé une forge du joueur 8
                x, y = int(u.x), int(u.y)

                blacksmith_zone = {
                    "blacksmith_X_A": x - taille,
                    "blacksmith_Y_A": y - taille,
                    "blacksmith_X_B": x + taille,
                    "blacksmith_Y_B": y + taille
                }
                break  # On sort dès qu'on trouve une forge
        if blacksmith_zone:
            break

    return blacksmith_zone
