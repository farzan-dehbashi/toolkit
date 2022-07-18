def mergeTwoLists(list1, list2):
    merge_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] <= list2[0]:
            merge_list.append(list1[0])
            del list1[0]
        else:
            merge_list.append(list2[0])
            del list2[0]
    if len(list1) != 0:
        merge_list += list1
    if len(list2) != 0:
        merge_list += list2
    return merge_list

list1 = [1,2,4]
list2 = [1,3,4,5]
print(mergeTwoLists(list1, list2))