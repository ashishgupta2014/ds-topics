"""
https://leetcode.com/problems/power-of-two/description/
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return False if n & (n-1) else True

solve = Solution()
print(solve.isPowerOfTwo(n=6))
print(solve.isPowerOfTwo(n=8))