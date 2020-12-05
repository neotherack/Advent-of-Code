import json

INPUT_FILE = "2020/Day5/inputdata"
MAPPER = {"F":"0", "B":"1", "L":"0", "R":"1"}
FACTOR = 8

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def translate_digit(digit_char):
    return MAPPER[digit_char]

def decode_data(str_data):
    #print(f"To be decoded: {str_data}")
    res = "".join(list(map(translate_digit, str_data)))
    #print(f"Decoded: {res}, which is {int(res,2)}")
    return res

def get_values(str_data):
    decoded = decode_data(str_data)

    try:
        row = int(decoded[:-3],2)
        col = int(decoded[-3:],2)
    except Exception as e:
        row = 0
        col = 0
        print(f"Ex01 - Exception while converting row {decoded[:-3]} and col {decoded[-3:]} from bin to dec")

    return row, col

def calculate_id(row, col):
    return FACTOR * row + col

def loop_method(passes):
    id_list = []
    for pass_ in passes:
        row, col = get_values(pass_)
        id_list.append(calculate_id(row, col))
    return id_list


def main():
    passes = load_data(INPUT_FILE)
    id_list = loop_method(passes)
    sorted_list = sorted(id_list)
    for i in range(min(sorted_list),max(sorted_list)):
        if not i in sorted_list:
            print(f"{i} not found in list!")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")