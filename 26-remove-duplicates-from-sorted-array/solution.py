// 0 ms | 20.4 MB
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        if n == 0:
            return 0
        while j<n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1