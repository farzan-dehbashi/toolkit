class Solution:


    @staticmethod
    def findMostOccured(nums):
        dict = {}
        max = 0
        char = ''
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
            if dict[num] > max:
                max = dict[num]
                char = num
        return max, char


    @staticmethod
    def findShortestSubArray(nums) -> int:
        _, char = Solution.findMostOccured(nums)
        s_index = nums.index(char)
        nums.reverse()
        e_index = len(nums) - nums.index(char) - 1
        return s_index, e_index


print(Solution.findShortestSubArray([1,2,2,3,1,4,2]))