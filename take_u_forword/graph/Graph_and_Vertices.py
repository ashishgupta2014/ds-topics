"""
https://practice.geeksforgeeks.org/problems/graph-and-vertices/1
"""
class Solution:
    def count(self, n):
        edges = (n * (n - 1)) // 2
        return 2 ** edges


solve = Solution()
print(solve.count(n=2))