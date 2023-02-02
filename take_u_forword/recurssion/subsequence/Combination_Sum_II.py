"""
https://leetcode.com/problems/combination-sum-ii/description/

https://www.youtube.com/watch?v=G1fRTGRxXU8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=9
"""
from typing import List


class Solution:

    def dfs(self, arr, target, i, cur, result):
        if target == 0:
            result.append(cur[:])
            return
        if i >= len(arr):
            return
        if target >= arr[i]:
            cur.append(arr[i])
            self.dfs(arr, target-arr[i], i+1, cur, result)
            cur.pop()
        while i < len(arr)-1 and arr[i] == arr[i+1]:
            i += 1
        self.dfs(arr, target, i+1, cur, result)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result

solve = Solution()
print(solve.combinationSum2(candidates=[10,1,2,7,6,1,5], target=8))