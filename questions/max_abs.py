class Solution:
    @staticmethod
    def maxAbsoluteSum(nums) -> int:
        max_val = abs(nums[0])
        current_sum = abs(nums[0])
        sign = -1 if nums[0] < 0 else 1
        for num in nums[1:]:
            if (sign == -1 and num > 0) or (sign == 1 and num < 0):
                if (num + sign * current_sum) < 0  and sign == 1:
                    sign = -1
                if (num + sign * current_sum) > 0 and sign == -1:
                    sign = 1
            else:
                current_sum = max(abs(current_sum + num), abs(num))


            max_val = max(max_val, current_sum)
            print(f'num= {num}, current= {current_sum}, max= {max_val}')
        return max_val


print(Solution.maxAbsoluteSum([2,-5,1,-4,3,-2]))