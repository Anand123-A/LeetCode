// 0 ms | 19.1 MB
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        n = len(gain)
        max_altitude = 0
        for i in range(0,n):
            altitude = altitude + gain[i]
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude
             