INPUT_FILE = "2020/Day10/inputdata"
START_ACC = 0
MAX_REPEAT = 1

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def valid_position(position_map, position):
    if not position in position_map:
        return True

    if position_map[position] >= MAX_REPEAT:
        return False
    else:
        return True

def annotate_position(position_map, position):
    if position in position_map:
        position_map[position] = position_map[position]+1
    else:
        position_map[position] = 1
    return position_map

def get_swap_list(instruction_list):
    swap_list = [-1]
    for index, instruction in enumerate(instruction_list):
        if instruction.startswith("jmp") or instruction.startswith("nop"):
            swap_list.append(index)
    return swap_list

def flip_instruction(instruction_list, position):
    if position==-1:
        return instruction_list

    print(f"Review applied on {position}, old list: {instruction_list}")
    if instruction_list[position].startswith("jmp"):
        #print(f"it was {instruction_list[position]}")
        instruction_list[position]=instruction_list[position].replace("jmp", "nop")
        #print(f"not it's {instruction_list[position]}")

    elif instruction_list[position].startswith("nop"):
        #print(f"it was {instruction_list[position]}")
        instruction_list[position]=instruction_list[position].replace("nop", "jmp")
        #print(f"not it's {instruction_list[position]}")

    print(f"Flip applied in postion {position}, new list: {instruction_list}")
    return instruction_list
    
def evaluate(instruction, position, position_map):
    aux = instruction.split(' ')
    operation = aux[0].strip()
    argument = aux[1].strip()
    value_ret = 0
    jump_step = 0

    if valid_position(position_map, position):
        position_map = annotate_position(position_map, position)
    else:
        return 0, 0, position_map, True

    if operation=="nop":
        jump_step=1
        value_ret=0
        #print(f" {jump_step}  {value_ret} NOP operation")
    elif operation=="acc":
        jump_step=1
        value_ret=int(argument)
        #print(f" {jump_step}  {value_ret} ACC operation")
    elif operation=="jmp":
        jump_step=int(argument)
        value_ret=0
        #print(f" {jump_step}  {value_ret} JMP operation")
    else:
        jump_step=1
        value_ret=0
        #print(f" ?  ? Unkown operation found!")

    #ret value modificator, jump step, position map
    return value_ret, jump_step, position_map, False

def scan_instruction_list(instruction_list):
    value = START_ACC
    position_map = {}

    i = 0

    while i < len(instruction_list):
        print(f"Will evaluate position {i} -> {instruction_list[i]}")
        value_modif, jump_step, position_map, stop = evaluate(instruction_list[i], i, position_map)
        value = value + value_modif

        if stop is True:
            break

        i=i + jump_step
    return value, stop

def main():
    orig_instruction_list = load_data(INPUT_FILE)
    swap_list = get_swap_list(orig_instruction_list)

    for swap_attempt in swap_list:
        orig_instruction_list = load_data(INPUT_FILE)
        print(f"Original list {orig_instruction_list}")
        instruction_list = flip_instruction(orig_instruction_list, swap_attempt)
        print(f"Will try with instruction list {instruction_list}")
        cnt, stop = scan_instruction_list(instruction_list)

        if stop==False:
            print(f"FOUND valid solution by swapping position {swap_attempt}, so it's {instruction_list}")
            break
        else:
            print(f"Invalid solution found when swapping on position {swap_attempt} for {instruction_list} will retry...")

    print(f"Calculated accumulator is {cnt}, stop value is {stop}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")