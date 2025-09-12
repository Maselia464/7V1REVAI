from AoE2ScenarioParser.datasets.other import OtherInfo
from uuid import UUID

def get_flag_positions(scenario):
    FLAG_O_ID = 2011
    FLAG_P_ID = 2012

    Flag_list = [
        ("FLAG_A", OtherInfo.FLAG_A.ID),
        ("FLAG_B", OtherInfo.FLAG_B.ID),
        ("FLAG_C", OtherInfo.FLAG_C.ID),
        ("FLAG_O", FLAG_O_ID),
        ("FLAG_P", FLAG_P_ID),
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
