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

def turn(current, rotation):
    #print(f"Previous {translate_direction(current)} ({current})")
    rotation_angle = int(rotation[1:]) % 360
    rotation_flow = rotation[:1]

    if (rotation_flow=="L"):
        #print(f"Turn LEFT {rotation_angle}")
        rotation_angle = rotation_angle * -1
    else:
        #print(f"Turn RIGHT {rotation_angle}")
        pass

    tmp_angle = current + rotation_angle
    new_dir = tmp_angle % 360

    print(f"New direction {translate_direction(new_dir)} ({new_dir})")
    return new_dir

def recalculate_coord(x, y, current_dir, instruction):
    command = instruction[:1]
    step = int(instruction[1:])

    if command=="R" or command=="L":
        return x, y, turn(current_dir, instruction)

    elif command=="F":
        if current_dir==0:
            y = y + step
        elif current_dir==90:
            x = x + step
        elif current_dir==180:
            y = y - step
        elif current_dir==270:
            x = x - step
        else:
            raise ValueError(f"cannot calculate next direction {instruction}")
        
        return x, y, current_dir

    elif command=="N":
        y = y + step
    elif command=="E":
        x = x + step
    elif command=="S":
        y = y - step
    elif command=="W":
        x = x - step
    else:
        raise ValueError(f"unknown command {instruction}")

    return x, y, current_dir

def main(ns, we, angle):
    instructions = load_data(INPUT_FILE)
    x = we
    y = ns
    ang = angle

    for instruction in instructions:
        x, y, angle = recalculate_coord(x, y, angle, instruction)
        print(f"I'm now in x:{x} y:{y}")

    print(f"Result N:{y} - E:{x} -> RESULT {abs(x)+abs(y)}")    

if __name__ == "__main__":
    starting_angle = 90
    starting_NS = 0
    starting_WE = 0
    main(starting_NS, starting_WE, starting_angle)
    #turn(90, "R810")

print("NeoTheRack - completed!")