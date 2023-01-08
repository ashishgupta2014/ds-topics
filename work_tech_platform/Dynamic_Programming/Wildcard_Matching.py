"""
https://workat.tech/problem-solving/practice/wildcard-matching
https://leetcode.com/problems/wildcard-matching/description/

https://www.youtube.com/watch?v=ZmlQ3vgAOMo
"""
class Solution:
    dp = {}
    def dfs(self, s, p, i, j):
        if (i, j) in self.dp:
            return self.dp[(i,j)]
        if i < 0 and j < 0:
            return True
        if i >= 0 and j < 0:
            return False
        if j >= 0  and i < 0:
            for x in range(j, -1, -1):
                if p[x] != '*':
                    return False
            return True
        match = s[i] == p[j] or p[j] == '?'
        if match:
            self.dp[(i, j)] = self.dfs(s, p, i-1, j-1)
            return self.dp[(i, j)]
        elif p[j] == '*':
            self.dp[(i,j)] = self.dfs(s, p, i-1, j) or self.dfs(s, p, i, j-1)
            return self.dp[(i,j)]
        return False
    def isMatch(self, s: str, p: str) -> bool:
        self.dp = {}
        return self.dfs(s, p, len(s)-1, len(p)-1)
        # tabulation need to be implemented after watching video



solve = Solution()

print(solve.isMatch(s='a', p='a'))

print(solve.isMatch(s='aa', p='a'))

print(solve.isMatch(s='ab', p='a?'))

print(solve.isMatch(s='aabcd', p='a*'))

print(solve.isMatch(s='bacd', p='ba*cd'))

print(solve.isMatch(s='bacd', p='*'))



