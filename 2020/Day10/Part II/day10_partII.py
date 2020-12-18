INPUT_FILE = "2020/Day10/inputdata"
SWAP_COUNTER = 1

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def map_to_int(str_jolt_list):
    return list(map(int, str_jolt_list))

def count():
    global SWAP_COUNTER
    SWAP_COUNTER = SWAP_COUNTER+1
    return SWAP_COUNTER-1


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

def count_non_mandatory_values(value_list, offset, deleted_items, depth):

    #print(f"Input list {value_list}")

    for index, value in enumerate(value_list):
        if (depth==0):
            print(f"Main iterator, progress {index}/{len(value_list)}")
            deleted_items=[]

        if (index<=0 or index>=len(value_list)-1):
            #print(f"Skipped index {index}, list lenght is {len(value_list)}")
            pass
        else:
            previous_item = value_list[index-1]
            next_item = value_list[index+1]
            gap = next_item - previous_item
            try:
                last_deleted = deleted_items[-1:][0]
            except:
                last_deleted=0

            if gap<=3 and value not in deleted_items and value>last_deleted:
                copy_list = value_list[:]
                copy_list.remove(value)
                val = count()
                deleted_items.append(value)
                #print(f"+ Deleted: {deleted_items} @ {depth} to DELETE -----> {value}, counter {val}")
                count_non_mandatory_values(copy_list, index, deleted_items, depth+1)
                deleted_items.remove(value)
            else:
                #print(f"- Values {previous_item} and {next_item} are on step {gap}, that's too much")
                #count()
                pass

    #print(f"{value_list}")

def setup_add_custom_adapter(value_list):
    value_list.append(0)
    value_list.append(max(value_list)+3)
    return sorted(value_list)

def main():
    int_jolt_list = map_to_int( load_data(INPUT_FILE) )
    res = count_non_mandatory_values(setup_add_custom_adapter(int_jolt_list), 0, [], 0)
    print(f"Counter: {SWAP_COUNTER}")
if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")