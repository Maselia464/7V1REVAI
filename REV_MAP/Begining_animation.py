from email.header import Header
from email.headerregistry import UniqueUnstructuredHeader
from gc import enable
from idlelib.rpc import objecttable
from pickle import FALSE
from typing import ClassVar
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


instruction_panel_main=0
instruction_panel_middle=1
instruction_panel_bottom=2
activate_sequence=True,
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
camera_speed=2
text_animation = {
    "Start_text": "<AQUA>Welcome to Sisterland Pine, a 7 vs 1 map created by Maselia\n欢迎来到姐妹之地松林，这是由Maselia制作的7对1地图",
    "Second_start_text": "<ORANGE>Before we begin, a word from our sponsor: Dummy Tutorial\n在开始之前，先听听我们的赞助商：Dummy教程的一句话",

    "Section_A_text": "<AQUA>Your goal is to destroy the Norman donjon on the other side of the map\n你的目标是摧毁地图另一侧的诺曼底主塔",

    "Section_B_text": "<AQUA>To achieve this, you must complete various objectives to unlock the next area and earn important rewards, such as aging up\n为了达到目标，你需要完成多个任务以解锁下一区域，并获得重要奖励，比如升级时代",
    "Section_B_text_2": "<RED>Secondary objectives allow you to earn bonuses that will help you win the scenario\n完成副任务可以获得奖励，帮助你赢得这场战役",

    "Stone_credit_text": "<GREEN>Stone is crucial—it lets you purchase upgrades in the fortress for your units and economy. Spend it wisely, as upgrades cannot be refunded\n石头非常重要，它可以让你在要塞中为你的单位和经济购买升级。请明智地使用，因为升级无法退款",

    "Eco_part": "<AQUA>Regarding the economy, you won’t have access to villagers. To gather resources, you must use relics\n关于经济，你无法使用村民。要获取资源，你必须使用圣物",
    "Eco_part_2": "<PURPLE>You can buy relics inside your monastery and upgrade their efficiency in the fortress\n你可以在修道院购买圣物，并在要塞中提升它们的效率",
    "Eco_part_3": "<AQUA>Your military buildings are indestructible and produce units faster\n你的军事建筑不会被摧毁，并且生产单位的速度更快",

    "Mission_timer": "<AQUA>Each mission must be completed before the timer runs out. If the timer reaches zero, you lose the mission\n每个任务必须在倒计时结束前完成。如果计时器归零，你将输掉任务",
    "Fire_tower": "<AQUA>Ensure the enemy does not destroy the fire tower at the entrance of your base. Each time it is destroyed, enemy units grow stronger\n确保敌人不要摧毁你基地入口的火塔。每次火塔被摧毁，敌方单位都会变得更强",

    "End_tutorial": "<AQUA>Thank you for listening to Dummy Tutorial. You may now start the game. Your host will select a mission from three difficulty levels: intermediate, advanced, or expert\n感谢你收听Dummy教程。现在你可以开始游戏了。你的主持人将从三个难度等级中选择一个任务：中级、高级或专家级"
}

list_building_selection=[BuildingInfo.BARRACKS.ID,BuildingInfo.ARCHERY_RANGE.ID,BuildingInfo.STABLE.ID,BuildingInfo.SIEGE_WORKSHOP.ID,BuildingInfo.WONDER.ID,BuildingInfo.FORTRESS.ID,
                                    BuildingInfo.BLACKSMITH.ID,BuildingInfo.UNIVERSITY.ID]
Camera_location=[35,32,
                 158,201,
                 106,70]
display_time_animation=[40,30,50]
normand_donjon_timer=40
objective_timer=70
def begining_animation(scenario):
    scenario_uuid = scenario.uuid
    area = Area.from_uuid(scenario_uuid)
    trigger_manager = scenario.trigger_manager
    Start_animation = trigger_manager.add_trigger(
        name="Begining animation 1",
        enabled=True,
        looping=False,
    )
    Start_animation_camera = trigger_manager.add_trigger(
        name="Begining animation 1 cam",
        enabled=True,
        looping=True,
    )
    Start_animation.new_effect.display_instructions(
        source_player=Liste_joueur[1],
        message=text_animation["Start_text"],
        instruction_panel_position=instruction_panel_main,
        object_list_unit_id=UnitInfo.MONK.ID,
        display_time=display_time_animation[0],
    )
    Start_animation.new_effect.display_instructions(
        source_player=Liste_joueur[1],
        message=text_animation["Second_start_text"],
        instruction_panel_position=instruction_panel_middle,
        display_time=display_time_animation[0],
    )
    for p in range (1,7):
        player = Liste_joueur[p]
        for y in range (len(list_building_selection)):
            if (player != PlayerId.ONE and list_building_selection[y] != BuildingInfo.WONDER.ID) \
               or (player == PlayerId.ONE):
                Start_animation.new_effect.disable_object_selection(
                    source_player=player,
                    object_list_unit_id=list_building_selection[y],
                    **area.select_entire_map().to_dict(),
                )

        Start_animation_camera.new_effect.change_view(
            source_player=player,
            location_x=Camera_location[0],
            location_y=Camera_location[1],
            scroll=True,
            quantity=camera_speed,
        )
    Donjon_normand = trigger_manager.add_trigger(
        name="Donjon normand animation",
        enabled=True,
        looping=False,
    )
    Donjon_normand_camera = trigger_manager.add_trigger(
        name="Donjon normand camera",
        enabled=False,
        looping=True,
    )
    player = 0
    Donjon_normand.new_condition.timer(
        timer=normand_donjon_timer,
    )
    Donjon_normand.new_effect.display_instructions(
        source_player=Liste_joueur[1],
        message=text_animation["Section_A_text"],
        instruction_panel_position=instruction_panel_main,
        object_list_unit_id=UnitInfo.PALADIN.ID,
        display_time=display_time_animation[0],
    )
    Donjon_normand.new_effect.clear_instructions(
        instruction_panel_position=instruction_panel_middle,
    )
    activate_cams=Donjon_normand_camera.trigger_id
    stop_trigger=[Start_animation.trigger_id,Start_animation_camera.trigger_id]
    for s in range (len(stop_trigger)):
        Donjon_normand.new_effect.deactivate_trigger(
            trigger_id=stop_trigger[s],
        )
    Donjon_normand.new_effect.activate_trigger(
        trigger_id=activate_cams,
    )
    for p in range (1,7):
        player= Liste_joueur[p]
        Donjon_normand_camera.new_effect.change_view(
            source_player=player,
            location_x=Camera_location[2],
            location_y=Camera_location[3],
            scroll=True,
            quantity=camera_speed,
        )



    Objective_expo = trigger_manager.add_trigger(
        name="Objective part",
        enabled=True,
        looping=False,
    )
    Objective_expo_destroy= trigger_manager.add_trigger(
        name="destroy the object part",
        enabled=True,
        looping=False,
    )
    Objective_expo_cams = trigger_manager.add_trigger(
        name="Objective cams",
        enabled=False,
        looping=True,
    )
    X_A=104
    Y_A=66
    X_B=98
    Y_B=68
    destroy_object = objective_timer + 10
    Objective_expo.new_condition.timer(
        timer=objective_timer,
    )
    Objective_expo.new_effect.display_instructions(
        source_player=Liste_joueur[1],
        message=text_animation["Section_B_text"],
        instruction_panel_position=instruction_panel_main,
        object_list_unit_id=UnitInfo.KING.ID,
        display_time=display_time_animation[2],
    )
    Objective_expo.new_effect.display_instructions(
        source_player=Liste_joueur[1],
        message=text_animation["Section_B_text_2"],
        instruction_panel_position=instruction_panel_middle,
        display_time=display_time_animation[2],
    )
    Objective_expo.new_effect.activate_trigger(
        trigger_id=Objective_expo_cams.trigger_id,
    )
    create_obj=[BuildingInfo.ARMY_TENT_C.ID,HeroInfo.GAJAH_MADA.ID]
    Objective_expo.new_effect.create_object(
        source_player=PlayerId.EIGHT,
        object_list_unit_id=create_obj[0],
        location_y=Y_B,
        location_x=X_B,
    )
    Objective_expo.new_effect.create_object(
        source_player=PlayerId.EIGHT,
        object_list_unit_id=create_obj[1],
        location_y=Y_A,
        location_x=X_A,
    )
    stop_trigger = [Donjon_normand.trigger_id, Donjon_normand_camera.trigger_id]
    for s in range(len(stop_trigger)):
        Objective_expo.new_effect.deactivate_trigger(
            trigger_id=stop_trigger[s],
        )
    for p in range (1,7):
        player= Liste_joueur[p]
        Objective_expo_cams.new_effect.change_view(
            source_player=player,
            location_x=Camera_location[4],
            location_y=Camera_location[5],
            scroll=True,
            quantity=camera_speed,
        )
    Objective_expo_cams.new_effect.free
    Objective_expo_destroy.new_condition.timer(
        timer=destroy_object,
    )
    Objective_expo_destroy.new_effect.kill_object(
        source_player=PlayerId.EIGHT,
        object_list_unit_id=create_obj[0],
        area_x1=X_B,
        area_x2=X_B,
        area_y1=Y_B,
        area_y2=Y_B,
    )

