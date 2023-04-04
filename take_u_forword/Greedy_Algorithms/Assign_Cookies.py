"""
https://leetcode.com/problems/assign-cookies/description/
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        i = 0
        ans = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans


solve = Solution()
print(solve.findContentChildren(g=[1,2,3], s=[1,1]))
print(solve.findContentChildren(g=[1,2], s=[1,2,3]))
print(solve.findContentChildren(g=[1,2,3], s=[3]))