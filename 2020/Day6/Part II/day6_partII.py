INPUT_FILE = "2020/Day6/inputdata"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except:
        print("exception on file read")
        return ""

def preprocess_data(raw_data):
    tmp_data=raw_data.split('\n\n')
    data = []

    for line in tmp_data:
        item = line.strip().split('\n')
        data.append(item)

    print(f"Clean data {data}")
    return data

def check_letter(letter, list_):
    for item in list_:
        if not letter in item:
            return False
    return True

def calculate_list(list_):
    first_item = list_[0]
    if len(list_)==1:
        return len(first_item)
    else:
        value = 0
        for letter in first_item:
            if check_letter(letter, list_):
                print(f"{letter} was found in all items at {list_}")
                value=value+1
            else:
                print(f"{letter} was NOT found in all items at {list_}")
        return value
   

def loop_method(lists_list):
    cnt = 0
    for list_ in lists_list:
        cnt = cnt + calculate_list(list_)
    return cnt

def main():
    raw_data = load_data(INPUT_FILE)
    lists_list = preprocess_data(raw_data)
    cnt = loop_method(lists_list)
    print(f"Detected {cnt} unique answers")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")