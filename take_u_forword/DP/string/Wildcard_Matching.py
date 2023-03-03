"""
https://leetcode.com/problems/wildcard-matching/description/

https://www.youtube.com/watch?v=ZmlQ3vgAOMo
"""
class Solution:

    def dfs(self, s, p, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i < 0 and j < 0:
            return True
        if i >= 0 and j < 0:
            return False
        if j >= 0 and i < 0:
            for x in range(j, -1, -1):
                if p[x] != '*':
                    return False
            return False

        if s[i] == p[j] or p[j] == '?':
            dp[(i, j)] = self.dfs(s, p, i-1, j-1, dp)
            return dp[(i, j)]
        elif p[j] == '*':
            dp[(i, j)] = self.dfs(s, p, i-1, j, dp) or self.dfs(s, p, i, j-1, dp)
            return dp[(i, j)]
        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, p, len(s)-1, len(p)-1, {})

solve = Solution()
print(solve.isMatch(s='cb', p='?a'))