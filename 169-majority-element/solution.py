// 13 ms | 21.7 MB
class Solution:
    def majorityElement(self, nums):
        # Moore's voting algorithm
        n = len(nums)
        freq = 0
        ans = 0
        for i in range(n):
            if freq == 0:
                ans = nums[i]
            if ans == nums[i]:
                freq = freq+1
            else:
                freq = freq-1
        return ans

        