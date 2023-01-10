"""
This is the Train class definition

https://workat.tech/problem-solving/practice/trains-and-platforms

"""
from typing import List


class Train:
    def __init__(self, arrival: int, departure: int):
        self.arrival = arrival
        self.departure = departure



class Solution:
    def minPlatforms(self, trains: List[Train]) -> int:
        arrival = [t.arrival for t in trains]
        departure = [t.departure for t in trains]
        arrival.sort()
        departure.sort()
        platform_needed = max_platform = 1
        d = 0
        a = 1
        n = len(arrival)

        while a < n and d < n:
            if arrival[a] <= departure[d]:
                platform_needed += 1
                max_platform = max(max_platform, platform_needed)
                a += 1
            else:
                platform_needed -= 1
                d += 1
        return max_platform

solve = Solution()
print(solve.minPlatforms(trains=[Train(120, 130), Train(130, 150), Train(125, 145), Train(150, 180)]))
print(solve.minPlatforms(trains=[Train(360, 400), Train(320, 380), Train(260, 320), Train(210, 250), Train(420, 450),
Train(440, 480), Train(370, 420)]))

#


