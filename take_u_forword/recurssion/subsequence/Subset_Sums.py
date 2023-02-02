"""
https://practice.geeksforgeeks.org/problems/subset-sums2234/1

https://www.youtube.com/watch?v=rYkfBRtMJr8&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=10
"""
class Solution:

    def dfs(self, arr, i, cur_sum, result):
        if i >= len(arr):
            result.append(cur_sum)
            return
        self.dfs(arr, i+1, cur_sum+arr[i], result)
        self.dfs(arr, i+1, cur_sum, result)

    def subsetSums(self, arr, N):
        result = []
        self.dfs(arr, 0, 0, result)
        return result

solve = Solution()
print(solve.subsetSums(arr=[5, 2, 1], N=3))
print(solve.subsetSums(arr=[2, 3], N=2))