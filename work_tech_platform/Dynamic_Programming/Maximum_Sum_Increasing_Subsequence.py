"""
https://workat.tech/problem-solving/practice/maximum-sum-increasing-subsequence

https://www.youtube.com/watch?v=R7DrJsTkK8w
"""
class Solution:
    def maxSumSubsequence(self, arr) -> int:
        n = len(arr)
        dp = arr.copy()

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if arr[i] <= arr[j]:
                    dp[i] = max(dp[i], arr[i]+dp[j])
        return max(dp)

solve = Solution()

print(solve.maxSumSubsequence(arr=[101, 4, 98, 103]))
print(solve.maxSumSubsequence(arr=[101, 4, 95, 103]))



