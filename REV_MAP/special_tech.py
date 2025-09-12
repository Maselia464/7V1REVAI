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



#trigger_manager = scenario.trigger_manager
silver_crown= 33
golden_crown= 107
food=Attribute.FOOD_STORAGE
wood=Attribute.WOOD_STORAGE
gold=Attribute.GOLD_STORAGE
stone=Attribute.STONE_STORAGE
stone_production_portugueuse_bonus= 2
INFANTRY = 906
ATK_VALUE_AREA = 1
MIN_UNIT_AREA_ACTIVATE = 1
WORK_FLAG_2_AMOUNT =0
CELT_AREA_RANGE = 4
CELT_ATK_ID = ObjectAttribute.ATTACK
AREA_DISPLAY = 5
ALLY_AREA = 4

SPEED_VALUE = 1.5
CAVALRY = 912
GEORGIAN_AREA = 8
GEORGIAN_SPEED_ID = ObjectAttribute.MOVEMENT_SPEED
EL_CID_ID = HeroInfo.EL_CID.ID
MOSCOW = HeroInfo.DMITRY_OF_MOSCOW.ID
script_constant= """
                const int KNIGHT = 38;
                const int CAVALIER = 283;
                const int PALADIN = 569;
                const int TEUTONIC_KNIGHT = 25;
                const int ELITE_TEUTONIC_KNIGHT = 554;
                const int HAND_CANON = 5;
                const int cRegenRate = 109;         
                """




Ally_stone_tribute_portugueuse= 400
parameters_special_tech = {
    1:[TechInfo.TEUTONS.ID,"The holy army","Research Holy Army <cost>: For each Relic you control (max 6), your Knights, Teutonic Knights, and hand cannoneers gain +10 HP regeneration.",golden_crown,75],
    2:[TechInfo.PORTUGUESE.ID,"Carreira da India", "Research Carreira da India <cost>: Immediately grants your allies 400 stone. Furthermore, you generate +2 stone per minute for each Relic you control.",silver_crown,45],
    3:[TechInfo.CELTS.ID,"Tribe chief", "Research Tribe chief <cost>:Unlocks the Banner Tribe Chief unit at your Castle. This unique unit emits an aura that doubles the attack of all nearby infantry units (including allies).",silver_crown,75],
    4:[TechInfo.MALAY.ID, "Malaysia All in", "Research Malaysia ALl in <cost> Instantly unlocks the Karambit Warrior for all allies at their Barracks. Your own Karambit Warriors are also strengthened, gaining +10 maximum hit points.",silver_crown,35],
    5:[TechInfo.ITALIANS.ID, "Dirty Deeds Done Dirt Cheap","Research Dirty Deeds Done Dirt Cheap <cost> Immediately advances your civilization to the Imperial Age. This forbidden knowledge comes at a great cost, reducing your maximum population by 100.", silver_crown,20],
    6:[TechInfo.CHINESE.ID, "The big four", "Research The big four <cost>: Chu Ko Nu, Fire Lancer, Scorpion, and Rocket Cart units are trained 25% faster.", silver_crown,65],
    7:[TechInfo.SICILIANS.ID, "Sicilian defence", "Research Sicilian defence <cost>: Serjeant and knight-line gain +3 armor", silver_crown,75],
    8:[TechInfo.GEORGIANS.ID, "Conch horseman", "Research Conch Horseman <cost>: You unlock the Concheror horseman at your castle, The Concheror horseman has an aura that give a movement speed for all cavalry units",silver_crown,60],
    9:[TechInfo.JURCHENS.ID, "Two city operation","Research two city operation <cost>: You unlock hand cannoneers, gunpowder unit gain a second projectile",silver_crown,70],
    10:[TechInfo.LITHUANIANS.ID, "Osmium Ordinance", "Research Osnium Ordinance <cost>: Stable and archery range work 4 times fasters", silver_crown,60],
    11:[TechInfo.MALIANS.ID, "The knowledge of Mansa Moussa", "Research The knowledge of Mansa Moussa <cost>: Relic gold generation is triple for you and double for your allies",silver_crown,120],
    12:[TechInfo.KOREANS.ID, "Korean ingeniering", "Research Korean ingeniering <cost>: Siege equipement and war chariot gain +20% HP",silver_crown,75],
    13:[TechInfo.PERSIANS.ID, "Sassanid Empire", "Research Sassanid Empire <cost>: Elephant and cavalrie gain +2 armors",golden_crown,75],
    14:[TechInfo.JAPANESE.ID, "Ozutsu", "Research Ozutsu <cost>: Hand cannoneers deal 20 damage agains building, Cavalry archer deal 10 damages on building",silver_crown,75],
    15:[TechInfo.SLAVS.ID,"Orthodoxy", "Research Orthodoxy <cost>: You received 5 relics and your teammates received 3 relics",silver_crown,90],
    16:[TechInfo.HUNS.ID,"Oz Terror", "Research Oz Terror <cost>: Cavalry archer gain +2 attacks and +15% movement speed ",golden_crown,80],
    17:[TechInfo.BYZANTINES.ID, "Mercenaries program", "Research Mercenaries program <cost>: You unlock the following units, Mangudai, Beserker, Step lancer, those units gain +2 attacks",silver_crown,45],
}
Liste_joueur = {
    1: PlayerId.ONE,
    2: PlayerId.TWO,
    3: PlayerId.THREE,
    4: PlayerId.FOUR,
    5: PlayerId.FIVE,
    6: PlayerId.SIX,
    7: PlayerId.SEVEN,
}
cost_tech = {
    1:[food,gold,1200,1000],
    2:[food,stone,900,200],
    3:[food,gold,1200,100],
    4:[food,gold,850,600],
    5:[gold,None,450,0],
    6:[wood,gold,1300,1200],
    7:[food,gold,850,850],
    8:[food,gold,1000,1000],
    9:[food,stone,1200,200],
    10:[wood,gold,1300,900],
    11:[gold,food,1600,500],
    12:[wood,gold,1100,850],
    13:[food,gold,1200,750],
    14:[food,gold,1400,800],
    15:[gold,stone,1000,300],
    16:[food,gold,650,550],
    17:[gold,None,1500,None],
}
def special_tech_civ(scenario):
    for i in parameters_special_tech:
        for p, player in Liste_joueur.items():
            scenario_uuid = scenario.uuid
            area = Area.from_uuid(scenario_uuid)
            player=Liste_joueur[p]
            the_tech=TechInfo.TECHNOLOGY_PLACEHOLDER_01.ID
            location=BuildingInfo.CASTLE.ID
            current_civ=parameters_special_tech[i][0]
            The_crown = parameters_special_tech[i][3]
            special_tech_trigger = scenario.trigger_manager.add_trigger(
                name=f"Special tech for {current_civ},{player}",
                enabled=True,
                looping=False,
            )
            special_tech_trigger.new_condition.research_technology(
                source_player=player,
                technology=current_civ,
                inverted=False,
            )
            if i == 1 and p == 1:
                special_tech_trigger.new_effect.script_call(
                    message=script_constant,
                )
            if The_crown == silver_crown:
                special_tech_trigger.new_condition.research_technology(
                    source_player=player,
                    technology=TechInfo.CASTLE_AGE.ID,
                    inverted=False,
                )
                button_location_tech = 7
            else:
                special_tech_trigger.new_condition.research_technology(
                    source_player=player,
                    technology=TechInfo.IMPERIAL_AGE.ID,
                    inverted=False,
                )
                button_location_tech = 8
            special_tech_trigger.new_effect.change_technology_name(
                source_player=player,
                message=parameters_special_tech[i][1],
                technology=the_tech,
            )
            special_tech_trigger.new_effect.change_technology_description(
                source_player=player,
                message=parameters_special_tech[i][2],
                technology=the_tech,
            )
            special_tech_trigger.new_effect.change_technology_icon(
                source_player=player,
                technology=the_tech,
                quantity=The_crown,
            )

            special_tech_trigger.new_effect.change_technology_location(
                source_player=player,
                technology=the_tech,
                object_list_unit_id_2=location,
                button_location=button_location_tech
            )
            special_tech_trigger.new_effect.change_technology_research_time(
                source_player=player,
                technology=the_tech,
                quantity=parameters_special_tech[i][4],
            )
            special_tech_trigger.new_effect.change_technology_cost(
                source_player=player,
                technology=the_tech,
                resource_1=cost_tech[i][0],
                resource_2=cost_tech[i][1],
                resource_1_quantity=cost_tech[i][2],
                resource_2_quantity=cost_tech[i][3],
            )
            special_tech_trigger.new_effect.enable_disable_technology(
                source_player=player,
                technology=the_tech,
                enabled=True,
            )
            print("current_civ =", current_civ, "the_tech =", the_tech, "player =", player)
            if current_civ == TechInfo.TEUTONS.ID:
                script_xs_effect= f"""
                int gLastBonus_{player} = 0;
                rule relic_bonus_{player}
                inactive
                minInterval 1
                maxInterval 1"""
                script_xs_effect+="{"
                script_xs_effect +=f"""int relics = xsPlayerAttribute({player}, cAttributeRelics);
                    if (relics > 6) relics = 6;
                
                    int delta = relics - gLastBonus_{player};"""
                script_xs_effect +="""if (delta != 0) {"""
                script_xs_effect +=f"""int packed = delta * 10;
                    xsEffectAmount(cAddAttribute, TEUTONIC_KNIGHT, cRegenRate, packed, {player});
                    xsEffectAmount(cAddAttribute, ELITE_TEUTONIC_KNIGHT, cRegenRate, packed, {player});
                    xsEffectAmount(cAddAttribute, KNIGHT,          cRegenRate, packed, {player});
                    xsEffectAmount(cAddAttribute, CAVALIER,          cRegenRate, packed, {player});
                    xsEffectAmount(cAddAttribute, PALADIN, cRegenRate, packed,{player});
                    xsEffectAmount(cAddAttribute, HAND_CANON, cRegenRate, packed,{player});
                    gLastBonus_{player} = relics;"""
                script_xs_effect += "}"
                script_xs_effect += "}"
                activate_rule=f"void activate_rule_{player}()"
                activate_rule +="{"
                activate_rule +=f"gLastBonus_{player} = 0;"
                activate_rule +=f"""xsEnableRule("relic_bonus_{player}");"""
                activate_rule +="}"
                teuton_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Teuton bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                teuton_bonus.new_condition.research_technology(
                     source_player=player,
                     technology=current_civ,
                     inverted=False,
                )
                teuton_bonus.new_condition.research_technology(
                     source_player=player,
                     technology=the_tech,
                     inverted=False,
                )
                teuton_bonus.new_effect.script_call(
                    message=script_xs_effect
                )
                teuton_bonus.new_effect.script_call(
                    message=activate_rule
                )
                ID = teuton_bonus.trigger_id
            elif current_civ == TechInfo.PORTUGUESE.ID:
                Portugueuse_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Portugueuse bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Portugueuse_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Portugueuse_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                for f in Liste_joueur.values():
                    Ally_player=Liste_joueur[f]
                    if Ally_player != player:
                        Portugueuse_bonus.new_effect.tribute(
                            source_player=PlayerId.GAIA,
                            target_player=Ally_player,
                            tribute_list=stone,
                            quantity=Ally_stone_tribute_portugueuse,
                        )
                    else:
                        Portugueuse_bonus.new_effect.modify_resource(
                            source_player=Ally_player,
                            tribute_list=Attribute.RELIC_STONE_PRODUCTION_RATE,
                            quantity=stone_production_portugueuse_bonus,
                        )
                ID = Portugueuse_bonus.trigger_id
            elif current_civ == TechInfo.CELTS.ID:
                hp_chief_tribe=200
                area_activation=32
                food_amount=250
                gold_amount=175
                button_location= 7
                unit_to_unlock=HeroInfo.EL_CID.ID
                building_location = BuildingInfo.CASTLE.ID
                name_chief_tribe="Chief tribe banner"
                description_chief="Create chief tribe banner <cost>: Train the Celtic Chief, a unique unit that carries a banner. His aura doubles the damage of all nearby infantry units."
                aura_bonus = f"""void aura_script_celt_{player}_()"""
                aura_bonus += "{"
                aura_bonus += f"""
                        xsTaskAmount(0, {ATK_VALUE_AREA});
                        xsTaskAmount(1, {MIN_UNIT_AREA_ACTIVATE});
                        xsTaskAmount(2, {CELT_AREA_RANGE});
                        xsTaskAmount(3, {WORK_FLAG_2_AMOUNT});
                        xsTaskAmount(4, {CELT_ATK_ID});
                        xsTaskAmount(5, {AREA_DISPLAY});
                        xsTaskAmount(6, {ALLY_AREA});
                        xsTask({EL_CID_ID}, 155, {INFANTRY}, {player});
                    """
                aura_bonus += "}"
                Celt_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Celt bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Celt_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Celt_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Celt_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                    quantity=0,
                    message=name_chief_tribe,
                )
                Celt_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.REGENERATION_RATE,
                    quantity=0,
                    operation=Operation.SET,
                )
                Celt_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.HIT_POINTS,
                    quantity=hp_chief_tribe,
                    operation=Operation.SET,
                )
                Celt_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.COMBAT_ABILITY,
                    quantity=area_activation,
                    operation=Operation.SET,
                )
                Celt_bonus.new_effect.enable_disable_object(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    enabled=True,
                )
                Celt_bonus.new_effect.change_object_description(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    message=description_chief,
                )
                Celt_bonus.new_effect.change_train_location(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_list_unit_id_2=building_location,
                    button_location=button_location,
                )
                Celt_bonus.new_effect.change_object_cost(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    resource_1=food,
                    resource_1_quantity=food_amount,
                    resource_2=gold,
                    resource_2_quantity=gold_amount,
                )
                Celt_bonus.new_effect.script_call(
                    message=aura_bonus,
                )
                ID = Celt_bonus.trigger_id
            elif current_civ == TechInfo.MALAY.ID:
                button_karambit = 15
                Karambit_bonus = 10
                unit_unlock = UnitInfo.KARAMBIT_WARRIOR.ID
                Malay_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Malay bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Malay_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Malay_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )

                for f in Liste_joueur.values():
                    Ally_player = Liste_joueur[f]
                    if Ally_player != player:
                        Malay_bonus.new_effect.enable_disable_object(
                            source_player=Ally_player,
                            object_list_unit_id=unit_unlock,
                            enabled=True,
                        )
                        Malay_bonus.new_effect.change_train_location(
                            source_player=Ally_player,
                            object_list_unit_id=unit_unlock,
                            object_list_unit_id_2=BuildingInfo.BARRACKS.ID,
                            button_location=button_karambit,
                        )
                    else:
                        Malay_bonus.new_effect.modify_attribute(
                            source_player=player,
                            object_attributes=ObjectAttribute.HIT_POINTS,
                            object_list_unit_id=unit_unlock,
                            quantity=Karambit_bonus,
                            operation=Operation.ADD,
                        )
                        Malay_bonus.new_effect.modify_attribute(
                            source_player=player,
                            object_attributes=ObjectAttribute.HIT_POINTS,
                            object_list_unit_id=UnitInfo.ELITE_KARAMBIT_WARRIOR.ID,
                            quantity=Karambit_bonus,
                            operation=Operation.ADD,
                        )
                ID = Malay_bonus.trigger_id
            elif current_civ == TechInfo.ITALIANS.ID:
                pop_nerf=100
                Italian_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Italian bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Italian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Italian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Italian_bonus.new_effect.research_technology(
                    source_player=player,
                    technology=TechInfo.IMPERIAL_AGE.ID,
                    force_research_technology=True,
                )
                Italian_bonus.new_effect.modify_resource(
                    source_player=player,
                    tribute_list=Attribute.BONUS_POPULATION_CAP,
                    quantity=pop_nerf,
                    operation=Operation.SUBTRACT,
                )
                ID = Italian_bonus.trigger_id
            elif current_civ == TechInfo.CHINESE.ID:
                unit_list = [UnitInfo.CHU_KO_NU.ID,UnitInfo.ELITE_CHU_KO_NU.ID,UnitInfo.ROCKET_CART.ID,UnitInfo.HEAVY_ROCKET_CART.ID,
                             UnitInfo.FIRE_LANCER.ID,UnitInfo.ELITE_FIRE_LANCER.ID,UnitInfo.SCORPION.ID,UnitInfo.HEAVY_SCORPION.ID]
                Train_speed=0.85
                Chinese_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Chinese bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Chinese_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Chinese_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                for x in range (len(unit_list)):
                    Chinese_bonus.new_effect.modify_attribute(
                        source_player=player,
                        object_list_unit_id=unit_list[x],
                        object_attributes=ObjectAttribute.TRAIN_TIME,
                        quantity=Train_speed,
                        operation=Operation.MULTIPLY,
                    )
                ID = Chinese_bonus.trigger_id
            elif current_civ == TechInfo.SICILIANS.ID:
                script_call_sicilian= f"void sicilian_buff_{player}()"
                script_call_sicilian+= "{"
                script_call_sicilian+=f"""
                xsEffectAmount(cAddAttribute, 1658, 8, 256 * 4 + 3, {player});
                xsEffectAmount(cAddAttribute, 1659, 8, 256 * 4 + 3, {player});
                xsEffectAmount(cAddAttribute, 38, 8, 256 * 4 + 3, {player});
                xsEffectAmount(cAddAttribute, 283, 8, 256 * 4 + 3, {player});
                """
                script_call_sicilian +="}"
                Sicilian = scenario.trigger_manager.add_trigger(
                    name=f"Sicilian bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Sicilian.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Sicilian.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Sicilian.new_effect.script_call(
                    message=script_call_sicilian,
                )
                ID = Sicilian.trigger_id
            elif current_civ == TechInfo.GEORGIANS.ID:
                hp_conch = 230
                area_activation = 32
                button_location = 7
                food_amount=200
                gold_amount=150
                unit_to_unlock = MOSCOW
                building_location = BuildingInfo.CASTLE.ID
                name_conch_cav = "Concheror Horseman"
                description_conch = "Create Concheror Horseman <cost>: Train the Concheror Horseman, a unique unit that carries a concheror. His aura increase the momvement speed of Cavalry units (except scouts-line and cavalry archer)."
                aura_bonus = f"""void aura_script_georgian_{player}()"""
                aura_bonus += "{"
                aura_bonus += f"""
                                        xsTaskAmount(0, {SPEED_VALUE});
                                        xsTaskAmount(1, {MIN_UNIT_AREA_ACTIVATE});
                                        xsTaskAmount(2, {GEORGIAN_AREA});
                                        xsTaskAmount(3, {WORK_FLAG_2_AMOUNT});
                                        xsTaskAmount(4, {GEORGIAN_SPEED_ID});
                                        xsTaskAmount(5, {AREA_DISPLAY});
                                        xsTaskAmount(6, {ALLY_AREA});
                                        xsTask({MOSCOW}, 155, {CAVALRY}, {player});
                                    """
                aura_bonus += "}"
                Georgia_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Georgia bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Georgia_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Georgia_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Georgia_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.OBJECT_NAME_ID,
                    quantity=0,
                    message=name_conch_cav,
                )
                Georgia_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.REGENERATION_RATE,
                    quantity=0,
                    operation=Operation.SET,
                )
                Georgia_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.HIT_POINTS,
                    quantity=hp_conch,
                    operation=Operation.SET,
                )
                Georgia_bonus.new_effect.modify_attribute(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_attributes=ObjectAttribute.COMBAT_ABILITY,
                    quantity=area_activation,
                    operation=Operation.SET,
                )
                Georgia_bonus.new_effect.enable_disable_object(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    enabled=True,
                )
                Georgia_bonus.new_effect.change_object_description(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    message=description_conch,
                )
                Georgia_bonus.new_effect.change_train_location(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_list_unit_id_2=building_location,
                    button_location=button_location,
                )
                Georgia_bonus.new_effect.change_object_cost(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    resource_1=food,
                    resource_1_quantity=food_amount,
                    resource_2=gold,
                    resource_2_quantity=gold_amount,
                )
                Georgia_bonus.new_effect.script_call(
                    message=aura_bonus,
                )
                ID = Georgia_bonus.trigger_id
            elif current_civ == TechInfo.JURCHENS.ID:
                unit_to_unlock=UnitInfo.HAND_CANNONEER.ID
                building_location=BuildingInfo.ARCHERY_RANGE.ID
                unit_list=[unit_to_unlock,UnitInfo.GRENADIER.ID,UnitInfo.BOMBARD_CANNON.ID]
                button_location=11
                total_missile= 1
                Jurchen_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Jurchen bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Jurchen_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Jurchen_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Jurchen_bonus.new_effect.enable_disable_object(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    enabled=True,
                )
                Jurchen_bonus.new_effect.change_train_location(
                    source_player=player,
                    object_list_unit_id=unit_to_unlock,
                    object_list_unit_id_2=building_location,
                    button_location=button_location,
                )
                for i in range (len(unit_list)):
                    Jurchen_bonus.new_effect.modify_attribute(
                        source_player=player,
                        object_list_unit_id=unit_list[i],
                        object_attributes=ObjectAttribute.MAX_TOTAL_MISSILES,
                        quantity=total_missile,
                        operation=Operation.ADD,
                    )
                    Jurchen_bonus.new_effect.modify_attribute(
                        source_player=player,
                        object_list_unit_id=unit_list[i],
                        object_attributes=ObjectAttribute.TOTAL_MISSILES,
                        quantity=total_missile,
                        operation=Operation.ADD,
                    )
                ID = Jurchen_bonus.trigger_id
            elif current_civ == TechInfo.LITHUANIANS.ID:
                building_list=[BuildingInfo.ARCHERY_RANGE.ID,BuildingInfo.STABLE.ID]
                work_rate_value=4
                lithuanian_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Lithuanian bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                lithuanian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                lithuanian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                for y in range (len(building_list)):
                    lithuanian_bonus.new_effect.modify_attribute(
                        source_player=player,
                        object_list_unit_id=building_list[y],
                        object_attributes=ObjectAttribute.WORK_RATE,
                        quantity=work_rate_value,
                        operation=Operation.MULTIPLY,
                    )
                ID=lithuanian_bonus.trigger_id
            elif current_civ == TechInfo.MALIANS.ID:
                player_production_rate = 3
                ally_production_rate = 2
                Malians_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Malian bonus bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Malians_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Malians_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                unit_unlock = UnitInfo.KARAMBIT_WARRIOR.ID,
                for f in Liste_joueur.values():
                    Ally_player = Liste_joueur[f]
                    if Ally_player != player:
                        Malians_bonus.new_effect.modify_resource(
                            source_player=Ally_player,
                            tribute_list=Attribute.RELIC_GOLD_PRODUCTION_RATE,
                            quantity=ally_production_rate,
                            operation=Operation.MULTIPLY,
                        )
                    else:
                        Malians_bonus.new_effect.modify_resource(
                            source_player=player,
                            tribute_list=Attribute.RELIC_GOLD_PRODUCTION_RATE,
                            quantity=player_production_rate,
                            operation=Operation.MULTIPLY,
                        )
                ID = Malians_bonus.trigger_id
            elif current_civ == TechInfo.KOREANS.ID:
                Class_scorpion = 955
                Class_siege = 913
                war_wagon=UnitInfo.WAR_WAGON.ID
                e_war_wagon=UnitInfo.ELITE_WAR_WAGON.ID
                buff=ObjectAttribute.HIT_POINTS
                value=1.20
                operation="cMulAttribute"

                bonus_script=f"void korean_hp_bonus_{player}()"
                bonus_script +="{"
                bonus_script += f"""
                    xsEffectAmount({operation}, {Class_scorpion}, {buff}, {value}, {player});
                    xsEffectAmount({operation}, {Class_siege}, {buff}, {value}, {player});
                    xsEffectAmount({operation}, {war_wagon},  {buff}, {value}, {player});
                    xsEffectAmount({operation}, {e_war_wagon}, {buff}, {value}, {player});
                    """
                bonus_script += "}"
                Korean_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Korean bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Korean_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Korean_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Korean_bonus.new_effect.script_call(
                    message=bonus_script,
                )
                ID= Korean_bonus.trigger_id
            elif current_civ == TechInfo.PERSIANS.ID:
                Class_cavalry = 912
                Class_scout = 947
                buff = ObjectAttribute.ARMOR
                value = "256 * 4 + 2"
                operation = "cAddAttribute"
                bonus_script = f"void persian_hp_bonus_{player}()"
                bonus_script += "{"
                bonus_script += f"""
                                    xsEffectAmount({operation}, {Class_cavalry}, {buff}, {value}, {player});
                                    xsEffectAmount({operation}, {Class_scout}, {buff}, {value}, {player});
                                    """
                bonus_script += "}"
                Persian_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Persian bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Persian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Persian_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Persian_bonus.new_effect.script_call(
                    message=bonus_script,
                )
                ID = Persian_bonus.trigger_id
            elif current_civ == TechInfo.JAPANESE.ID:
                HAND_CANON_BONUS_BUILDING=20
                CAV_ARCHER_BONUS_BUILDING=10
                Japanese_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Japanese bonus,{player}",
                    enabled=False,
                    looping=True,
                )
                Japanese_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Japanese_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Japanese_bonus.new_effect.create_object_attack(
                    source_player=player,
                    object_list_unit_id=UnitInfo.HAND_CANNONEER.ID,
                    **area.select_entire_map().to_dict(),
                    armour_attack_class=DamageClass.STANDARD_BUILDINGS,
                    armour_attack_quantity=HAND_CANON_BONUS_BUILDING,
                    operation=Operation.SET,
                )
                Japanese_bonus.new_effect.create_object_attack(
                    source_player=player,
                    object_list_unit_id=UnitInfo.HAND_CANNONEER.ID,
                    **area.select_entire_map().to_dict(),
                    armour_attack_class=DamageClass.STANDARD_BUILDINGS,
                    armour_attack_quantity=CAV_ARCHER_BONUS_BUILDING,
                    operation=Operation.SET,
                )
                ID = Japanese_bonus.trigger_id
            elif current_civ == TechInfo.SLAVS.ID:
                Slav_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Slav bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Slav_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Slav_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                for f in Liste_joueur.values():
                    Ally_player = Liste_joueur[f]
                    if Ally_player != player:
                        for ally_relic in range(0,3):
                            Slav_bonus.new_effect.create_garrisoned_object(
                                source_player=Ally_player,
                                object_list_unit_id=BuildingInfo.CASTLE.ID,
                                object_list_unit_id_2=UnitInfo.MONK_WITH_RELIC.ID,
                                **area.select_entire_map().to_dict(),
                            )
                    else:
                        for host_relic in range(0, 5):
                            Slav_bonus.new_effect.create_garrisoned_object(
                                source_player=player,
                                object_list_unit_id=BuildingInfo.CASTLE.ID,
                                object_list_unit_id_2=UnitInfo.MONK_WITH_RELIC.ID,
                                **area.select_entire_map().to_dict(),
                            )
                ID = Slav_bonus.trigger_id
            elif current_civ == TechInfo.HUNS.ID:
                script_call_huns = f"void huns_buff_{player}()"
                script_call_huns += "{"
                script_call_huns += f"""
                                xsEffectAmount(cAddAttribute, 39, 9, 256 * 3 + 1, {player});
                                xsEffectAmount(cAddAttribute, 474, 9, 256 * 3 + 1, {player});
                                xsEffectAmount(cMulAttribute, 39, 5, 1.15, {player});
                                xsEffectAmount(cMulAttribute, 474, 5, 1.15, {player});
                                """
                script_call_huns += "}"
                Huns_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Huns bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Huns_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Huns_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                Huns_bonus.new_effect.script_call(
                    message=script_call_huns,
                )
                ID = Huns_bonus.trigger_id
            else:
                unit_list=[UnitInfo.MANGUDAI.ID,UnitInfo.BERSERK.ID,UnitInfo.STEPPE_LANCER.ID]
                button_location=[13,8,4]
                building_location=[BuildingInfo.ARCHERY_RANGE.ID,BuildingInfo.BARRACKS.ID,BuildingInfo.STABLE.ID]
                Mangudai = unit_list[0]
                Berserk = unit_list[1]
                Step_lancer = unit_list[2]
                buff = ObjectAttribute.ATTACK
                value_melee = "256 * 4 + 2"
                value_range = "256 * 3 + 2"
                operation = "cAddAttribute"
                bonus_script = f"void byzantine_atk_bonus_{player}()"
                bonus_script += "{"
                bonus_script += f"""
                                    xsEffectAmount({operation}, {Mangudai}, {buff}, {value_range}, {player});
                                    xsEffectAmount({operation}, {Berserk}, {buff}, {value_melee}, {player});
                                    xsEffectAmount({operation}, {Step_lancer}, {buff}, {value_melee}, {player});
                                    """
                bonus_script += "}"
                Byzantine_bonus = scenario.trigger_manager.add_trigger(
                    name=f"Byzantine bonus,{player}",
                    enabled=False,
                    looping=False,
                )
                Byzantine_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=current_civ,
                    inverted=False,
                )
                Byzantine_bonus.new_condition.research_technology(
                    source_player=player,
                    technology=the_tech,
                    inverted=False,
                )
                for h in range (len(unit_list)):
                    Byzantine_bonus.new_effect.change_train_location(
                        source_player=player,
                        object_list_unit_id=unit_list[h],
                        object_list_unit_id_2=building_location[h],
                        button_location=button_location[h],
                    )
                    Byzantine_bonus.new_effect.enable_disable_object(
                        source_player=player,
                        object_list_unit_id=unit_list[h],
                        enabled=True,
                    )
                Byzantine_bonus.new_effect.script_call(
                    message=bonus_script
                )
                ID=Byzantine_bonus.trigger_id

            special_tech_trigger.new_effect.activate_trigger(
                trigger_id=ID,
            )
    return None
