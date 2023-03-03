"""
https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/

https://www.youtube.com/watch?v=xwomavsC86c
"""
from typing import List


class Solution:

    def dfs(self, cuts, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i > j:
            return 0

        min_cost = float('inf')
        for ind in range(i, j+1):
            cost = cuts[j+1] - cuts[i-1] + self.dfs(cuts, i, ind-1, dp) + self.dfs(cuts, ind+1, j, dp)
            min_cost = min(min_cost, cost)
        dp[(i, j)] = min_cost
        return min_cost
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        return self.dfs(cuts, 1, len(cuts)-2, {})

solve = Solution()
print(solve.minCost(n=7, cuts=[1,3,4,5]))