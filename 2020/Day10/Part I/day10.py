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
    
def evaluate(instruction, position, position_map):
    aux = instruction.split(' ')
    operation = aux[0].strip()
    argument = aux[1].strip()
    value_ret = 0
    jump_step = 0

    if valid_position(position_map, position):
        position_map = annotate_position(position_map, position)
    else:
        return 0, 0, None

    if operation=="nop":
        jump_step=1
        value_ret=0
        print(f" {jump_step}  {value_ret} NOP operation")
    elif operation=="acc":
        jump_step=1
        value_ret=int(argument)
        print(f" {jump_step}  {value_ret} ACC operation")
    elif operation=="jmp":
        jump_step=int(argument)
        value_ret=0
        print(f" {jump_step}  {value_ret} JMP operation")
    else:
        jump_step=1
        value_ret=0
        print(f" ?  ? Unkown operation found!")

    #ret value modificator, jump step, position map
    return value_ret, jump_step, position_map

def scan_instruction_list(instruction_list):
    value = START_ACC
    position_map = {}

    i = 0

    while i < len(instruction_list):
        print(f"Will evaluate position {i} -> {instruction_list[i]}")
        value_modif, jump_step, position_map = evaluate(instruction_list[i], i, position_map)
        value = value + value_modif

        if position_map is None:
            break

        i=i + jump_step
    return value

def main():
    instruction_list = load_data(INPUT_FILE)
    cnt = scan_instruction_list(instruction_list)
    print(f"Calculated accumulator is {cnt}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")