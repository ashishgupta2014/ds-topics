"""
https://workat.tech/problem-solving/practice/longest-common-subsequence

https://www.youtube.com/watch?v=NPZn9jBrX8U
https://www.youtube.com/watch?v=Ua0GhsJSlWM
"""
class Solution:
    def getLengthOfLCS(self, s1: str, s2: str) -> int:
        rows = len(s1)+1
        cols = len(s2)+1
        dp = [[0]*cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                if s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])
        return dp[-1][-1]


solve = Solution()
print(solve.getLengthOfLCS(s1="workattech", s2="branch"))



