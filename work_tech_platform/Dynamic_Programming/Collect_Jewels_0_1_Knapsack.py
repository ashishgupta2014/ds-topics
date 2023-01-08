"""
https://workat.tech/problem-solving/practice/collect-jewels

https://www.youtube.com/watch?v=GqOmJHQZivw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=20
"""


from typing import List

class JewelStone:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value


class Solution:

    def backtracking(self, stones, capacity, i, dp):
        if i == 0:
            if stones[i].weight <= capacity:
                return stones[i].value
            else:
                return 0
        if dp[i][capacity] > 0:
            return dp[i][capacity]
        pickup = 0
        # not pick up
        not_pickup = 0 + self.backtracking(stones, capacity, i-1, dp)
        if stones[i].weight < capacity:
            # pick up
            pickup = stones[i].value + self.backtracking(stones, capacity-stones[i].weight, i-1, dp)
        dp[i][capacity] = max(not_pickup, pickup)
        return dp[i][capacity]
    def getMaxValue(self, stones: List[JewelStone], capacity: int) -> int:
        # dp = [[0]*(capacity+1) for _ in range(len(stones)+1)]
        # return self.backtracking(stones, capacity, len(stones)-1, dp)

        rows = len(stones)+1
        cols = capacity+1
        dp = [[0]*cols for _ in range(rows)]
        for row in range(1, rows):
            for col in range(1, cols):
                if stones[row-1].weight > col:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row-1][col-stones[row-1].weight]+stones[row-1].value)
        return dp[-1][-1]


solve = Solution()
jewel_stones = [JewelStone(1, 3), JewelStone(2, 4), JewelStone(3, 5), JewelStone(4, 7)]
print(solve.getMaxValue(stones=jewel_stones, capacity=5))

jewel_stones = [JewelStone(2, 4), JewelStone(6, 14), JewelStone(5, 13), JewelStone(9, 21), JewelStone(8, 18)]

print(solve.getMaxValue(stones=jewel_stones, capacity=25))
