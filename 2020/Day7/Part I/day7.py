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

def check_color_map(data_map, color_list, target, log):
    if color_list == {}:
        print(f"<0 Found END branch at {log} [[ret=0]]")
        return 0
    else:
        for color in color_list:
            if color==target:
                print(f"<1 Found target {target} at {log}\t>\t{color} [[ret=1]]")
                return 1
            else:
                print(f">> Going deep on list at {log}\t>\t{color}")
                deep = check_color_map(data_map, data_map[color], target, f"{log}\t>\t{color}")
                if (deep>0):
                    return deep

        print(f"<0 {target} N/F at {log}\t>\t{color}")
        return 0

def scan_map(data_map, target):
    cnt = 0

    for color_map in data_map:
        if color_map==target:
            print(f"## Iteration PRUNED for color {color_map}")
            pass
        else:
            print(f"\n$$ Iteration for color {color_map}")
            cnt = cnt + check_color_map(data_map, data_map[color_map], target, color_map)
    return cnt

def main():
    raw_data = load_data(INPUT_FILE)
    data_map = preprocess_data(raw_data)
    cnt = scan_map(data_map, TARGET_VALUE)
    print(f"Found {cnt} bag")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")