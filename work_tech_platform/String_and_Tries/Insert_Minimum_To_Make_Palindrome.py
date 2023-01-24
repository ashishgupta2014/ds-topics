"""
https://workat.tech/problem-solving/practice/min-insertion-palindrome

https://www.youtube.com/watch?v=6i_T5kkfv4A&t=11s

https://www.youtube.com/watch?v=xPBLEj41rFU
"""
class Solution:
    def minCharactersToBeInserted(self, A: str) -> int:
        s1 = A
        s2 = A[::-1]
        rows = len(s1)+1
        cols = len(s2)+1
        dp = [[0]*cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                if s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])
        return len(A)-dp[-1][-1]


solve = Solution()
print(solve.minCharactersToBeInserted(A='baaba'))