    def removeDuplicates(self, nums):
        to_remove_p = 1
        to_compare_p =0
        while to_compare_p < len(nums) and to_remove_p < len(nums):
            if nums[to_remove_p] > nums[to_compare_p]:
                to_compare_p = to_compare_p + 1
                to_remove_p = to_remove_p + 1
            else:
                del nums[to_remove_p]
