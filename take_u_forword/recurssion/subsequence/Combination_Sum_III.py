"""
https://leetcode.com/problems/combination-sum-iii/description/
"""
from typing import List


class Solution:
    arr = list(range(1, 10))

    def dfs(self, k, n, i, temp, result):
        if len(temp) == k and sum(temp) == n:
            result.append(temp[:])
            return
        if i >= len(self.arr):
            return
        temp.append(self.arr[i])
        self.dfs(k, n, i+1, temp, result)
        temp.pop()
        self.dfs(k, n, i+1, temp, result)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.dfs(k, n, 0, [], result)
        return result

solve = Solution()
print(solve.combinationSum3(k=3, n=7))
print(solve.combinationSum3(k=3, n=9))
print(solve.combinationSum3(k=3, n=1))