INPUT_FILE = "2020/Day2/inputdata"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []


def loop_method(pass_list):
    valid_count = 0

    for pass_item in pass_list:
        if valid_line(pass_item):
            print(f"{pass_item} is valid")
            valid_count = valid_count+1
        else:
            print(f"{pass_item} is NOT valid :(")
    
    return valid_count


def valid_line(line):
    position_range, rule_to_check, text = line.split(' ')

    position_start = int(position_range.split('-')[0])
    position_end = int(position_range.split('-')[1])
    rule_to_check = rule_to_check.split(':')[0]

    if (text[position_start-1]==rule_to_check and not text[position_end-1]==rule_to_check) or (not text[position_start-1]==rule_to_check and text[position_end-1]==rule_to_check):
        return True
    else:
        return False


def main():
    pass_list = load_data(INPUT_FILE)
    count = loop_method(pass_list)
    print(f"Valid passwords found {count}")


if __name__ == "__main__":
    main()


print("NeoTheRack - completed!")