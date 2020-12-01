

INPUT_FILE = "2020/Day1/inputdata"
SUM_TARGET = 2020

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []
 
def convert_to_int(str_list):
    return list(map(int, str_list))

def loop_method(int_list):
    for value1 in int_list:
        for value2 in int_list:
            if value1+value2==SUM_TARGET:
                return value1, value2
            else:
                #print(f"value1: {value1} and value2: {value2} -> {value1+value2} do not match, iterate!")
                pass
        

def main():
    int_list = convert_to_int(load_data(INPUT_FILE))
    #print(f"value list: {int_list}")
    value1, value2 = loop_method(int_list)
    print(f"Value match on {value1} and {value2}, result: {value1*value2}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")