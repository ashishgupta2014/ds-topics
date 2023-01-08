"""
https://workat.tech/problem-solving/practice/longest-increasing-subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/

https://www.youtube.com/watch?v=cjWnW0hdF1Y
"""
class Solution:
    def getLengthOfLIS(self, A) -> int:
        dp = [1] * len(A)

        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A)):
                if A[i] < A[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)



solve = Solution()

print(solve.getLengthOfLIS(A=[1, 2, 4, 3]))
print(solve.getLengthOfLIS(A=[10, 20, 2, 5, 3, 8, 8, 25, 6]))