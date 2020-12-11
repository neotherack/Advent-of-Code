INPUT_FILE = "2020/Day9/inputdata"
PREAMBLE_LENGTH = 25

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def map_to_int(str_list):
    return list(map(int, str_list))

def analyze_number(position, value, filtered_list):
    if (position <= PREAMBLE_LENGTH):
        print(f"$ {value} is detected as PREAMBLE")
        return False
    else:
        for value1 in filtered_list:
            for value2 in filtered_list:
                if value1+value2==value:
                    print(f"+ FOUND valid SUM {value1} + {value2} equals {value} | position in list:{position}")
                    return False
        print(f"# DEFAULT EXIT scanning for {value} in {filtered_list}")
        return True

def loop_method(int_list):
    print(f"SCANNING SUM failure in {int_list}")
    for index, value in enumerate(int_list):
        delta = index-PREAMBLE_LENGTH
        filtered_list = int_list[delta:index]
        result = analyze_number(index, value, filtered_list)
        if result==False:
            pass
        else:
            print(f"! CANNOT find any valid SUM at position {index} @ {value} for {filtered_list}")
            return value

    return -1

def get_weakness(detected_number, int_list):
    print(f"SCANNING for SUM set list...")
    for index, value in enumerate(int_list):
        if (index<= PREAMBLE_LENGTH):
            print(f"$ {value} is detected as PREAMBLE")
            continue

        tmp_list = int_list[:index]
        print(f"& tmp list is {tmp_list}")
        for i in range(1, len(tmp_list)):
            growing_tmp_list = tmp_list[(i*-1):]
            print(f"& tmp growing list is {growing_tmp_list}")
            sum_result = sum(growing_tmp_list)

            if sum_result > detected_number:
                print(f"- INVALID SUM found {sum_result} on {growing_tmp_list}")
                continue_main_for=False
                break
            
            if sum_result == detected_number:
                print(f"+ VALID SUM found {sum_result} on {growing_tmp_list}")
                return growing_tmp_list

            if sum_result < detected_number:
                #print(f"% Not enough sum is {sum_result} using {growing_tmp_list}")
                pass

    return []

def main():
    int_list = map_to_int(load_data(INPUT_FILE))
    calculated = loop_method(int_list)
    print(f"result {calculated}")
    result_list = get_weakness(calculated, int_list)
    print(f"result list: {result_list}. MAX {max(result_list)}, MIN {min(result_list)} -> expected weakness result {max(result_list)+min(result_list)}")


if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")