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
    count_range, rule_to_check, text = line.split(' ')

    count_start = int(count_range.split('-')[0])
    count_end = int(count_range.split('-')[1])
    rule_to_check = rule_to_check.split(':')[0]

    if (text.count(rule_to_check)>=count_start and text.count(rule_to_check)<=count_end):
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