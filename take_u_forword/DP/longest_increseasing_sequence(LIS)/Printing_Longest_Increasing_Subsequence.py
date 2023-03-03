"""
https://practice.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1


https://takeuforward.org/data-structure/printing-longest-increasing-subsequence-dp-42/
"""
class Solution:
    result = []
    def dfs(self, arr, N, i, temp):

        if i >= N:
            if len(self.result) < len(temp):
                self.result = temp[:]
            return

        if len(temp) == 0 or arr[i] > temp[-1]:
            temp.append(arr[i])
            self.dfs(arr, N, i+1, temp)
            temp.pop()
        self.dfs(arr, N, i+1, temp)

    def longestIncreasingSubsequence(self, N, arr):
        # self.result = []
        # self.dfs(arr, N, 0, [])
        # return self.result
        dp = [1]*N
        hash = [0]*N
        max_len = 0
        last_index = 0

        for i in range(N):
            hash[i] = i
            for prev in range(i+1):
                if arr[i] > arr[prev] and dp[i] < 1+dp[prev]:
                    dp[i] = 1 + dp[prev]
                    hash[i] = prev
            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i
        result = [arr[last_index]]
        while hash[last_index] != last_index:
            last_index = hash[last_index]
            result.append(arr[last_index])
        return result[::-1]


solve = Solution()
print(solve.longestIncreasingSubsequence(N=16, arr=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))