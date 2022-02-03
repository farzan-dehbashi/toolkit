class Solution:
    @staticmethod
    def mergeTwoLists(list1, list2):
        l1_p = 0
        l2_p = 0
        result = []
        while l1_p < len(list1) and l2_p < len(list2):
            if list1[l1_p] <= list2[l2_p]:
                result.append(list1[l1_p])
                l1_p += 1
            else:
                result.append(list2[l2_p])
                l2_p += 1

        if l1_p != len(list1):
            result += list1[l1_p:]
        elif l2_p != len(list2):
            result += list1[l2_p:]

        return result


print(Solution.mergeTwoLists([1,2,3,4,7], [1,3,5,6]))