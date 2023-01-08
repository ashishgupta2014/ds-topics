"""
https://www.codingninjas.com/codestudio/problems/longest-common-substring_1235207

https://www.youtube.com/watch?v=_wP9mWNPL5w&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=29
"""
class Solution:
    def getLengthOfLCS(self, s1: str, s2: str) -> int:
        rows = len(s1)
        cols = len(s2)
        dp = [[0]*cols for _ in range(rows)]
        max_length = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if s1[row] == s2[col]:
                    dp[row][col] = dp[row-1][col-1] + 1
                    max_length = max(dp[row][col], max_length)
        return max_length

solve = Solution()

print(solve.getLengthOfLCS(s1="abcjklp", s2="acjkp"))

print(solve.getLengthOfLCS(s1="wasdijkl", s2="wsdjkl"))