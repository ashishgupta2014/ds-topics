"""
https://leetcode.com/problems/combination-sum/description/

https://www.youtube.com/watch?v=OyZFFqQtu98&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=8
"""
from typing import List


class Solution:
    def dfs(self, arr, target, i, temp, result):
        if sum(temp) == target:
            result.append(temp[:])
            return
        if i >= len(arr) or sum(temp) > target:
            return
        temp.append(arr[i])
        self.dfs(arr, target, i, temp, result)
        temp.pop()
        self.dfs(arr, target, i + 1, temp, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result

solve = Solution()
print(solve.combinationSum(candidates=[2, 3, 6, 7], target=7))