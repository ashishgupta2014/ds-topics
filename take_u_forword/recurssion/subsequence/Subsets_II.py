"""
https://leetcode.com/problems/subsets-ii/description/

https://www.youtube.com/watch?v=RIn3gOkbhQE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=11
"""
from typing import List


class Solution:

    def dfs(self, nums, i, cur, result):
        if i >= len(nums):
            result.append(cur[:])
            return
        cur.append(nums[i])
        self.dfs(nums, i+1, cur, result)
        cur.pop()
        while i < len(nums)-1 and nums[i] == nums[i+1]:
            i += 1
        self.dfs(nums, i+1, cur, result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

solve = Solution()
print(solve.subsetsWithDup(nums=[1,2,2]))
