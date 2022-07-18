

def find_start_loc(costs, gases):
    calculated_costs = []
    for index, cost in enumerate(costs):
        calculated_costs.append(gases[index] - costs[index])
    map = []
    for index, item in enumerate(calculated_costs):
        if item < 0:
            map.append(False)
        elif calculated_costs[index-1] > 0:
            map.append(False)
        else:
            map.append(True)
    first_possible_start_loc = None
    for index, possible_start in enumerate(map):
        if possible_start == True:
            first_possible_start_loc = index
            break
    relative_costs = {}
    for index, posibility in enumerate(map):
        if posibility == True:
            if index != first_possible_start_loc:
                relative_cost = 0
                for cost in costs[first_possible_start_loc:index]:
                    relative_cost += cost
                relative_costs[index] = relative_cost
    max_val = 0
    for value in relative_costs.values():
        if value > max_val:
            max_val = value

    for key, value in relative_costs.items():
        if value == max_val:
            return key



if __name__ == '__main__':
    costs = [1,5,3,3,5,3,1,3,4,5]
    gas = [5,2,2,8,2,4,2,5,1,2]
    print(find_start_loc(costs, gas))