// 62 ms | 29.7 MB
class Solution:
    def maxArea(self, height: list[int]) -> int:
        n =  len(height)
        width = 0
        water_height = 0
        area = 0
        max_area = 0
        left = 0
        right = n-1
        while left < right:
            width = right - left
            water_height = min(height[left],height[right])
            area = width * water_height
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left+= 1
            else:
                right-= 1
        return max_area



        