INPUT_FILE = "2020/Day3/inputdata"
VERTICAL_START = 0
HORIZONTAL_START = 0

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []


def loop_method(slope, horizontal_step, vertical_step):
    slope_high = len(slope)
    slope_matrix_width = len(slope[0])
    #we can ignore width, since it repeats to both sides (left and right)
    hori = HORIZONTAL_START
    trees = 0
    blanks = 0

    #print(f"Slope scan starting...")

    for high in range(VERTICAL_START, slope_high, vertical_step):
        #print(f"Scanning slope on position {high} {hori}")
        thing = slope[high][hori]
        #print(f"Found {thing} ( dot means blank, hash means tree )")
        if (thing == "."): #it's blank
            blanks = blanks+1
        elif (thing == "#"): #it's a tree
            trees = trees+1
        else: #just in case, for part II
            pass
        #calculate hori for the next iteration
        hori = (hori + horizontal_step) % slope_matrix_width
        #print(f"Horizontal coordenate for next iteration will be {hori}")

    #print(f"Slope scan completed!")
    
    return trees, blanks


def iterate_plan(slope, step_plan):
    result = 1

    for index, step in enumerate(step_plan):
        trees, blanks = loop_method(slope, step[0], step[1])
        print(f"Result was {result}, on step {index} apply step rule: r{step[0]}:d{step[1]}, it's updated to {result*trees}")
        result = result * trees

    return result


def main():
    step_plan = [(1, 1),(3, 1),(5, 1),(7, 1), (1, 2)]
    slope = load_data(INPUT_FILE)
    result = iterate_plan(slope, step_plan)
    print(f"Final result is {result}")

if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")