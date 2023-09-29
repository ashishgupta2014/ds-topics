"""
https://practice.geeksforgeeks.org/problems/odd-or-even3618/1
"""
class Solution:
    def oddEven (ob, N):
        return 'even' if N == (N >> 1) << 1 else 'odd'

solve = Solution()
print(solve.oddEven(N=8))