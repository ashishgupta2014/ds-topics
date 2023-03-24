"""
https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

https://leetcode.com/problems/magnetic-force-between-two-balls/solutions/794070/python-binary-search-solution-with-explanation-and-similar-questions/
"""

class Solution:
    def findSmallestMaxDist(self, stations, K):
        stations.sort()
        low = 0
        high = stations[-1] - stations[0]

        while high-low > 1e-5:
            mid = (low + high)/2
            if self.is_possible(mid, stations, K):
                high = mid
            else:
               low = mid
        return round(high, 2)

    def is_possible(self, dist, stations, k):
        new_stations = 0
        for i in range(1, len(stations)):
            new_stations += (stations[i] - stations[i-1])//dist
        return new_stations <= k


solve = Solution()
print(solve.findSmallestMaxDist(stations=[3,6,12,19,33,44,67,72,89,95], K=2))