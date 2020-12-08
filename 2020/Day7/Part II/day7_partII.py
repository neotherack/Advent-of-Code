INPUT_FILE = "2020/Day7/inputdata"
TARGET_VALUE = "shiny gold"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        print("exception on file read")
        return ""

def preprocess_data(raw_data):
    raw_list=raw_data.split('\n')
    data = {}

    for line in raw_list:
        #print(line)
        aux = line.replace('bags', '').replace('bag','').replace('.','').strip().split('contain')
        parent = aux[0].strip()

        if "contain no other bags" in line:
            data[parent]={}
        else:
            children_raw = aux[1].strip().split(',')
            children = {}
            for child_raw in children_raw:
                child_aux = child_raw.strip().split(' ',1)
                children[child_aux[1].strip()]=child_aux[0].strip()
            
            data[parent]=children

    return data

def check_color_map(data_map, color_list, target, log, depth):
    if color_list == {}:
        print(f"<1\t\tBLANK at {log} [[ret=1]]")
        return 1
    else:
        cnt = 0
        for color in color_list:
            next_level_log = f"{log}\t>\t{color_list[color]} {color}"
            next_level_factor = int(color_list[color])
            print(f">>\t\tGo deep for {next_level_log}")
            next_level_count = check_color_map(data_map, data_map[color], target, next_level_log, depth+1)
            print(f"@\t\tGot {next_level_count} from {next_level_log}")
    
            cnt = cnt + (next_level_factor * next_level_count)
            print(f"<{cnt}\t\tCurrent SUM {cnt}")

        print(f"<{cnt+1}\t\tRet ({depth}) at {log}")
        return cnt +1

def scan_map(data_map, target):
    return check_color_map(data_map, data_map[target], target, target, 1)

def main():
    raw_data = load_data(INPUT_FILE)
    data_map = preprocess_data(raw_data)
    print(data_map)
    cnt = scan_map(data_map, TARGET_VALUE)
    print(f"Found {cnt-1} bag")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")