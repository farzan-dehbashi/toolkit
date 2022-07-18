class Solution:
    @staticmethod
    def merge(nums1, nums2, n, m) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        while p1 < len(nums1) - 1 and p2 < len(nums2) - 1:
            if nums2[p2] == nums1[p1] or (nums1[p1] < nums2[p2] and nums1[p1 + 1] > nums2[p2]):
                nums1.insert(p1 + 1, nums2[p2])
                p1 += 1
                p2 += 1
            else:
                p1 +=1
        if p2 < len(nums2) -1:
            nums1 = nums1 + nums2 [p2:]
        print(nums1)
print(Solution.merge([1,2,3],[2,5,6],1,2))