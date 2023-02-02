"""
https://leetcode.com/problems/subsets/
"""
class Solution:

    def dfs(self, arr, i, res, ans):
        if i >= len(arr):
            ans.append(res[:])
            return
        res.append(arr[i])
        self.dfs(arr, i+1, res, ans)
        res.pop()
        self.dfs(arr, i+1, res, ans)
    def subsequences(self, arr):
        ans = []
        self.dfs(arr, 0, [], ans)
        return ans

solve = Solution()
print(solve.subsequences(arr=[3, 2, 1]))
print(solve.subsequences(arr=[1, 2, 3]))