INPUT_FILE = "2020/Day11/inputdata"
LIMIT = 5

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f]
    except:
        print("exception on file read")
        return []

def get_seat(seat_x, seat_y, delta_x, delta_y, seat_map):
    if (seat_x < 0 or seat_y < 0):
        return '?'

    seat = seat_map[seat_y][seat_x]

    try:
        if (seat_x+delta_x>=0 and seat_y+delta_y>=0 and seat_x+delta_x<len(seat_map[seat_y]) and seat_y+delta_y<len(seat_map)):
            neigbor = seat_map[seat_y + delta_y][seat_x + delta_x]
        else:
            return '?'

        if neigbor!=".":
            return neigbor
        elif seat_x+delta_x<0 or seat_y+delta_y<0 or seat_x+delta_x==len(seat_map[seat_y]) or seat_y+delta_y==len(seat_map):
            return "?"
        else:
            #print(f"recursive on {seat_x} {seat_y}, going {seat_x+delta_x} {seat_y+delta_y}")
            return get_seat(seat_x+delta_x, seat_y+delta_y, delta_x, delta_y, seat_map)
    except:
        return "?"

def get_adjacents(x, y, seat_map):
    adjacent_list = {
        "front": "?",
        "rear": "?",
        "left": "?",
        "right": "?",
        "front-right": "?",
        "front-left": "?",
        "rear-right": "?",
        "rear-left": "?"
    }

    cnt = 0

    #print(f"pos x={x}@{len(seat_map[y])}, y={y}@{len(seat_map)}")

    if (x>=0):
        adjacent_list["left"]=get_seat(x, y, -1, 0, seat_map)#  seat_map[y][x-1]

    if (y>=0):
        adjacent_list["front"]=get_seat(x, y, 0, -1, seat_map)#  seat_map[y-1][x]

    if (x<len(seat_map[y])-1):
        adjacent_list["right"]=get_seat(x, y, 1, 0, seat_map)#  seat_map[y][x+1]

    if (y<len(seat_map)-1):
        adjacent_list["rear"]=get_seat(x, y, 0, 1, seat_map)#  seat_map[y+1][x]

    if (x>0 and y>0):
        adjacent_list["front-left"]=get_seat(x, y, -1, -1, seat_map)#  seat_map[y-1][x-1]

    if (x<len(seat_map[y])-1 and y>0):
        adjacent_list["front-right"]=get_seat(x, y, 1, -1, seat_map)#  seat_map[y-1][x+1]

    if (x>0 and y<len(seat_map)-1):
        adjacent_list["rear-left"]=get_seat(x, y, -1, 1, seat_map)#  seat_map[y+1][x-1]

    if (x<len(seat_map[y])-1 and y<len(seat_map)-1):
        adjacent_list["rear-right"]=get_seat(x, y, 1, 1, seat_map)#  seat_map[y+1][x+1]

    return adjacent_list

def calculate_seat_params(adjacents):
    free=0
    occupy=0
    space=0

    for position in adjacents:
        if adjacents[position]=="#":
            occupy=occupy+1
        elif adjacents[position]=="L":
            free=free+1
        elif adjacents[position]==".":
            space=space+1
        elif adjacents[position]=="?":
            pass
        else:
            #print(f"Unknown symbol {adjacents[position]}")
            pass
    
    adjacents["occupy"]=occupy
    adjacents["free"]=free
    adjacents["space"]=space

    return adjacents

def seat_with_no_neigbors(adjacents):
    
    if adjacents["occupy"]==0:
        #print(f"Debug {adjacents}, return True")
        return True
    else:
        #print(f"Debug {adjacents}, return False")
        return False

def seat_with_too_much_neigbors(adjacents, neigbor_limit):
    if adjacents["occupy"]>=neigbor_limit:
        return True
    else:
        return False

def calculate_seat_map_next_state(seat_map, neigbor_limit):
    next_seat_map = []

    for y,row in enumerate(seat_map):
        next_seat_map.append("")
        for x,seat in enumerate(row):
            adj = get_adjacents(x, y, seat_map)
            adj = calculate_seat_params(adj)

            if seat!=".":
                #print(f"Processing seat x={x}, y={y} -> {seat} | Free={adj['free']}, Occupy={adj['occupy']}-{adj}")
                pass

            if (seat=="L" and seat_with_no_neigbors(adj)):
                #print(f"+ OCCUPY seat x={x}, y={y}")
                next_seat_map[y]=next_seat_map[y]+"#"
            elif (seat=="#" and seat_with_too_much_neigbors(adj, neigbor_limit)):
                #print(f"- RELEASE seat x={x}, y={y}")
                next_seat_map[y]=next_seat_map[y]+"L"
            else:
                next_seat_map[y]=next_seat_map[y]+seat
        #print(f"New seat map: {next_seat_map}")

    return next_seat_map

def print_seat_map(seat_map):
    for index, row in enumerate(seat_map):
        print(f"{index}->\t{row}")

def get_seat_map_stats(seat_map):
    free = 0
    occupy = 0
    space = 0

    for row in seat_map:
        for seat in row:
            if seat=="L":
                free=free+1
            elif seat=="#":
                occupy=occupy+1
            else:
                space=space+1
    return occupy, free, space

def main():
    seat_map = load_data(INPUT_FILE)
    
    for i in range(100):
        print(f"Iteration {i}")
        print_seat_map(seat_map)
        new_seat_map = calculate_seat_map_next_state(seat_map, LIMIT)

        if new_seat_map == seat_map:
            print(f"Unchanged on iteration {i}")
            break
        else:
            seat_map=new_seat_map

    print(f"\n\n  **** FINAL RESULT ****  \n")
    print_seat_map(seat_map)
    occupy, free, space = get_seat_map_stats(seat_map)
    
    print(f"Free={free}, Occupy={occupy}, Space={space}")


if __name__ == "__main__":
    main()

print("NeoTheRack - completed!")