// 0 ms | 21.7 MB
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
        