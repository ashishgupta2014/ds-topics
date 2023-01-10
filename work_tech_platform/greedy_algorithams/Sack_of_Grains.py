"""
This is the Grain class definition

Fractional Knapsack | Greedy Algorithms

first sort in decreasing order and then calculate max price by reducing weight

https://workat.tech/problem-solving/practice/sack-of-grainshttps://workat.tech/problem-solving/practice/sack-of-grains

https://workat.tech/problem-solving/approach/sog/sack-of-grains

https://www.youtube.com/watch?v=F_DDzYnxO14
"""
from typing import List


class Grain:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value


class Solution:
    def maxSackValue(self, grains: List[Grain], w: int) -> float:
        grains = sorted(grains, key=lambda x: x.value/x.weight, reverse=True)
        i = 0
        max_value = 0
        while w > 0 and i < len(grains):
            grain_added = min(w, grains[i].weight)
            w -= grain_added
            max_value += grain_added*(grains[i].value/grains[i].weight)
            i += 1
        return max_value



solve = Solution()
print(solve.maxSackValue(grains=[Grain(5, 20), Grain(8, 20), Grain(4, 15), Grain(5, 8)], w=12))

print(solve.maxSackValue(grains=[Grain(10, 3), Grain(4, 8), Grain(2, 5), Grain(3, 8)], w=8))

