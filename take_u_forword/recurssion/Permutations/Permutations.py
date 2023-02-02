"""
https://leetcode.com/problems/permutations/description/

https://www.youtube.com/watch?v=YK78FU5Ffjw&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=12

space optimized: https://www.youtube.com/watch?v=f2ic2Rsc9pU&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=13
"""
from typing import List


class Solution:

    def dfs(self, nums, ds, ans):
        if len(ds) == len(nums):
            ans.append(list(ds.keys()))
            return
        for i in nums:
            if i not in ds:
                ds[i] = True
                self.dfs(nums, ds, ans)
                del ds[i]

    def dfs_swap(self, nums, i, ans):
        if i >= len(nums):
            ans.append(nums[:])
            return
        for j in range(i, len(nums)):
            nums[i],  nums[j] = nums[j], nums[i]
            self.dfs_swap(nums, i+1, ans)
            nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # ds = {}
        # self.dfs(nums, ds, ans)
        self.dfs_swap(nums, 0, ans)
        return ans


solve = Solution()
print(solve.permute(nums=[1, 2, 3]))
