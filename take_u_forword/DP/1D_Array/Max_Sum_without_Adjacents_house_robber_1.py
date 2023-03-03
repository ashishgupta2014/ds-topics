"""
https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1
https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
https://leetcode.com/problems/house-robber/description/

https://www.youtube.com/watch?v=GrMBfJNk_NY
https://www.youtube.com/watch?v=3WaxQMELSkw
"""
class Solution:

    def dfs(self, arr, i, dp):
        if i == 0:
            return arr[0]
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        left = arr[i] + self.dfs(arr, i - 2, dp)
        right = self.dfs(arr, i-1, dp)
        dp[i] = max(left, right)
        return max(left, right)

    def tabluar(self, arr, n):
        dp = [0]*n
        dp[0] = arr[0]

        for i in range(1, n):
            left = arr[i] if i-2 < 0 else arr[i] + dp[i-2]
            right = dp[i-1]
            dp[i] = max(left, right)
        return dp[n-1]

    def two_pointer(self, arr, n):
        prev1 = prev2 = arr[0]
        for i in range(1, n):
            left = arr[i] if i-2 < 0 else arr[i] + prev2
            right = prev1
            cur = max(left, right)
            prev2 = prev1
            prev1 = cur
        return prev1


    def findMaxSum(self, arr, n):
        # dp = [-1]*n
        # return self.dfs(arr, n-1,  dp)
        # return self.tabluar(arr, n)
        return self.two_pointer(arr, n)

solve = Solution()
print(solve.findMaxSum(arr=[5, 5, 10, 100, 10, 5], n=6))
print(solve.findMaxSum(arr=[3, 2, 7, 10], n=4))
