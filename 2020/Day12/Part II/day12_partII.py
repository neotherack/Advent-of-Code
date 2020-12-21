INPUT_FILE = "2020/Day12/inputdata"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def translate_direction(angle):
    if angle==0:
        return "NORTH"
    elif angle==90:
        return "EAST"
    elif angle==180:
        return "SOUTH"
    elif angle==270:
        return  "WEST"
    else:
        raise ValueError(f"Wrong turn angle {angle}")

def turn(wx, wy, current, rotation):
    #print(f"Previous {translate_direction(current)} ({current})")
    rotation_angle = int(rotation[1:]) % 360
    rotation_flow = rotation[:1]

    if (rotation_flow=="L"):
        #print(f"Turn LEFT {rotation_angle}")
        rotation_angle = rotation_angle * -1
    else:
        #print(f"Turn RIGHT {rotation_angle}")
        pass

    equivalent_instruction = f"R{rotation_angle}"
    print(f"Equivalent rotation {equivalent_instruction}")
    if equivalent_instruction=="R90" or equivalent_instruction=="R-270":
        wx, wy = wy, (wx*-1)
    elif equivalent_instruction=="R-90" or equivalent_instruction=="R270":
        wx, wy = (wy*-1), wx
    elif equivalent_instruction=="R180" or equivalent_instruction=="R-180":
        wx, wy = (wx*-1), (wy*-1)
    else:
        print(f"Not expected turn instruction, equivalent {equivalent_instruction}")
        pass

    tmp_angle = current + rotation_angle
    new_dir = tmp_angle % 360
    new_dir_str = translate_direction(new_dir)

    print(f"New direction {new_dir_str} ({new_dir})")
    return wx, wy, new_dir

def recalculate_coord(x, y, wx, wy, current_dir, instruction):
    command = instruction[:1]
    step = int(instruction[1:])

    if command=="R" or command=="L":
        new_wx, new_wy, new_angle = turn(wx, wy, current_dir, instruction)
        return x, y, new_wx, new_wy, new_angle

    elif command=="F":
        print(f"Ship was x:{x} y:{y}, waypoint was wx:{wx} wy:{wy}")
        move_x = wx * step
        move_y = wy * step
        print(f"Movement dx:{move_x}  dy:{move_y}")
        return x+move_x, y+move_y, wx, wy, current_dir

    elif command=="N":
        wy = wy + step
    elif command=="E":
        wx = wx + step
    elif command=="S":
        wy = wy - step
    elif command=="W":
        wx = wx - step
    else:
        raise ValueError(f"unknown command {instruction}")

    return x, y, wx, wy, current_dir

def main(ns, we, wns, wwe, angle):
    instructions = load_data(INPUT_FILE)
    x = we
    y = ns

    wx = wwe
    wy = wns

    ang = angle

    for instruction in instructions:
        x, y, wx, wy, angle = recalculate_coord(x, y, wx, wy, angle, instruction)
        print(f"Boat x:{x} y:{y} | Waypoint wx:{wx} wy:{wy}")

    print(f"Result N:{y} - E:{x} -> RESULT {abs(x)+abs(y)}")    

if __name__ == "__main__":
    starting_angle = 90
    starting_NS = 0
    starting_WE = 0
    starting_waypoint_NS = 1
    starting_waypoint_WE = 10
    main(starting_NS, starting_WE, starting_waypoint_NS, starting_waypoint_WE, starting_angle)
    #turn(90, "R810")

print("NeoTheRack - completed!")