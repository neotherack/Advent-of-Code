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
        item = list(set(list(line.replace('\n', '').strip())))
        #print(f"item {item}")
        data.append(item)

    #print(f"Clean data {data}")
    return data

def loop_method(data_list):
    cnt = 0
    for data in data_list:
        cnt = cnt + len(data)
    return cnt

def main():
    raw_data = load_data(INPUT_FILE)
    data_list = preprocess_data(raw_data)
    cnt = loop_method(data_list)
    print(f"Detected {cnt} unique answers")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")