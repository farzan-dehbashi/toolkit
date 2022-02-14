def rotate_arr(nums, k):
    nums = nums[len(nums) -k:] + nums[:len(nums) -k] 
    return nums

if __name__ == '__main__':
    print(rotate_arr(nums = [1,2,3,4,5,6,7], k = 3))