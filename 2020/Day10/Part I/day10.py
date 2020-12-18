INPUT_FILE = "2020/Day10/inputdata"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def map_to_int(str_jolt_list):
    return list(map(int, str_jolt_list))

def analyze(value_list):
    step1_counter = 0
    step2_counter = 0
    step3_counter = 0

    print(f"Input list {value_list}")

    for index, value in enumerate(value_list):
        previous = value_list[index-1]
        if (index<=0):
            pass
        else:
            step = value-previous
            print(f"Values {previous} and {value} are on step {step}")
            if step==1:
                step1_counter = step1_counter+1
            elif step==2:
                step2_counter = step2_counter+1
            elif step==3:
                step3_counter = step3_counter+1
            else:
                pass

    return step1_counter, step3_counter

def setup_add_custom_adapter(value_list):
    value_list.append(0)
    value_list.append(max(value_list)+3)
    return sorted(value_list)

def main():
    int_jolt_list = map_to_int( load_data(INPUT_FILE) )
    jolt_step_1, jolt_step_3 = analyze(setup_add_custom_adapter(int_jolt_list))
    print(f"Calculated jolt steps are step-1 {jolt_step_1} gaps, step-3 {jolt_step_3} gaps. Result is {jolt_step_1*jolt_step_3}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")