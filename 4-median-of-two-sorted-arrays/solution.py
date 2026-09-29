// 1304 ms | 19.5 MB
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median : float
        merged_array = nums1+nums2
        for passes in range(len(merged_array)):
            for i in range(0,len(merged_array)-1-passes):
                if merged_array[i] > merged_array[i+1]:
                    merged_array[i],merged_array[i+1] = merged_array[i+1],merged_array[i]
        n = len(merged_array)
        if n % 2 == 0:
            median = (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2
        else:
            median = merged_array[n // 2]
        return median              