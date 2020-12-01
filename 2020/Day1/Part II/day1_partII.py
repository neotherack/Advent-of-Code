

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

def loop_method3(int_list):
    for value1 in int_list:
        for value2 in int_list:
            for value3 in int_list:
                if value1+value2+value3==SUM_TARGET:
                    return value1, value2, value3
                else:
                    #print(f"value1: {value1} and value2: {value2} -> {value1+value2} do not match, iterate!")
                    pass

def main():
    int_list = convert_to_int(load_data(INPUT_FILE))
    value1, value2, value3 = loop_method3(int_list)
    print(f"Value match on {value1}, {value2} and {value3}, result: {value1*value2*value3}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")