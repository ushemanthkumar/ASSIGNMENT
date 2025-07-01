

nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

rotate(nums, k)

print("nums =",nums) 
