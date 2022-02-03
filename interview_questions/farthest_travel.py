# finds the array of shortest pathes


def shortest_distance(block, facility_map):
    block_map = []
    for facility in block:
        if facility == 1: # This facility exists in this block
            block_map[block].append(0)
        elif facility == 0:
            if block == 0:
                block_map[block].append(shortest_distance(block + 1, facility_map))
            elif block == len(facility_map) - 1:
                block_map[block].append(shortest_distance(block - 1, facility_map))
            else:
                block_map[block].append(int(min(shortest_distance(block - 1, facility_map),shortest_distance(block + 1, facility_map))))
    print(block, block_map)


# Calculate map for dp


def calc_map(blocks):
    facility_map = []
    for block in blocks:
        facility_map.append(shortest_distance(block, blocks))



# Finds optimal block where we have to travel minimum farthest distance to find all facilities


def optimal_apartment():
    pass


if __name__ == '__main__':
    existance_map = [[0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 1, 1]]
    short_path_map = calc_map(existance_map)