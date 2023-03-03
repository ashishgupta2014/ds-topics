"""
https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

https://www.youtube.com/watch?v=vRVfmbCFW7Y

https://www.youtube.com/watch?v=pDCXsbAw5Cg
"""
class Solution:

    def dfs(self, arr, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i == j:
            return 0
        min_op = float('inf')
        for k in range(i, j):
            steps = arr[i-1]*arr[k]*arr[j] + self.dfs(arr, i, k, dp) + self.dfs(arr, k+1, j, dp)
            min_op = min(min_op, steps)
        dp[(i, j)] = min_op
        return min_op
    def matrixMultiplication(self, N, arr):
        # return self.dfs(arr, 1, N-1, {})
        dp = [[0]*N for _ in range(N)]
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                min_op = float('inf')
                for k in range(i, j):
                    steps = arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                    min_op = min(min_op, steps)
                dp[i][j] = min_op

        return dp[1][N-1]

solve = Solution()
print(solve.matrixMultiplication(N=5, arr=[40, 20, 30, 10, 30]))