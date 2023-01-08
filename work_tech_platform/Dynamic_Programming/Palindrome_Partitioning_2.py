"""
https://workat.tech/problem-solving/practice/palindromic-partitioning-2

https://www.youtube.com/watch?v=_H8V5hJUGd0
"""
class Solution:

    dp = []
    @staticmethod
    def is_palindrome(s, left, right):
        while left < right and s[left]:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def dfs(self, s, i):
        if i >= len(s):
            return 0
        if self.dp[i] != -1:
            return self.dp[i]
        min_cut = float('inf')
        for j in range(i, len(s)):
            if self.is_palindrome(s, left=i, right=j):
                cuts = 1 + self.dfs(s, j+1)
                min_cut = min(min_cut, cuts)
                self.dp[i] = min_cut
        return min_cut

    def getMinCuts(self, s: str) -> int:
        # self.dp = [-1]*len(s)
        # return self.dfs(s, 0)-1
        n = len(s)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            min_cut = float('inf')
            for j in range(i, n):
                if self.is_palindrome(s, left=i, right=j):
                    cuts = 1 + dp[j+1]
                    min_cut = min(min_cut, cuts)
            dp[i] = min_cut
        return dp[0]-1



solve = Solution()
print(solve.getMinCuts(s='aabc'))
print(solve.getMinCuts(s='coffee'))
print(solve.getMinCuts(s='aabb'))
print(solve.getMinCuts(s='mom'))