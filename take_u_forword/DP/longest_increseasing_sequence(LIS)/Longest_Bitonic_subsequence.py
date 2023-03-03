"""
https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1

https://www.youtube.com/watch?v=y4vN0WNdrlg
"""
class Solution:

    def lis(self, nums):
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i+1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return dp

    def LongestBitonicSequence(self, nums):
        asc = self.lis(nums)
        dsc = self.lis(nums[::-1])[::-1]
        n = len(nums)
        return max([asc[i]+dsc[i]-1 for i in range(n)])

solve = Solution()
print(solve.LongestBitonicSequence(nums=[1, 11, 2, 10, 4, 5, 2, 1]))
print(solve.LongestBitonicSequence(nums=[20,7, 9, 6, 9, 21, 12, 3, 12, 16, 1, 27]))