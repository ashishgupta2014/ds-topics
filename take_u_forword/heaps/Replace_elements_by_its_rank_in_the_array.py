"""
https://practice.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1
"""
class Solution:

    def ranker(self, nums):
        temp = {}
        j = 0
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = j+1
                j += 1
        return temp
    def replaceWithRank(self, N, arr):
        nums = sorted(arr)
        rank = self.ranker(nums)
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        return arr



solve = Solution()
print(solve.replaceWithRank(arr=[20, 15, 26, 2, 98, 6], N=6))
print(solve.replaceWithRank(arr=[2, 20, 10, 3, 14, 16, 14], N=7))