"""
https://leetcode.com/problems/expression-add-operators/description/

https://www.youtube.com/watch?v=171aA2ir8GE
https://www.youtube.com/watch?v=8wmks4LX2F8
"""
from typing import List


class Solution:

    def dfs(self, nums, target, result, i, temp, s, prev):
        if i >= len(nums):
            if s == target:
                result.append(''.join(temp))
            return
        for j in range(i, len(nums)):
            cand = int(nums[i:j+1])
            if not temp:
                self.dfs(nums, target, result, j + 1, temp + [nums[i:j + 1]], cand, cand)
            else:
                self.dfs(nums, target, result, j+1, temp+['+']+[nums[i:j+1]], s+cand, cand)
                self.dfs(nums, target, result, j + 1, temp + ['-'] + [nums[i:j + 1]], s-cand, -cand)
                self.dfs(nums, target, result, j + 1, temp + ['*'] + [nums[i:j + 1]], s-prev+cand*prev, cand*prev)
            if nums[i] == '0':
                break

    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.dfs(num, target, result, 0, [], 0, 0)
        return result

solve = Solution()
print(solve.addOperators(num='123', target=6))
print(solve.addOperators(num='00', target=0))
print(solve.addOperators(num='105', target=5))