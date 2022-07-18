def three_sum(arr):
    sums = dict()
    res = list()
    for element_1 in arr:
        for element_2 in arr:
            if element_1 != element_2:
                sums[element_1 + element_2] = (element_1, element_2)
    for element_3 in arr:
        if element_3 in sums.keys():
            (element_1, element_2) = sums[element_3]
            if element_3 != element_1 and element_3 != element_2 and element_2 != element_3:
                res_element = [element_1, element_2, element_3]
                res_element.sort()
                res.append(res_element)
    return res

print(three_sum([-1,0,1,2,-1,-4]))