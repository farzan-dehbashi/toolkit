class Solution:
    def mergeTwoLists(self, l1, l2):
        l1_insert_p = 0
        l2_delete_p = 0
        ans = []
        while len(l1) != 0 or len(l2) != 0:
            if len(l1) == 0:
                return ans.append(l2)
            if len(l2) == 0:
                return ans.append(l1)
            if l1[0] >= l2[0]:
                ans.append(l1[0])
                del l1[0]
            elif l2[0] > l1[0]:
                ans.append(l2[0])
                del l2[0]
        return ans

l1 = [1,2,3,4]
l2 = [2,2,3,4,4,5]
solution = Solution()
print(solution.mergeTwoLists(l1,l2))
