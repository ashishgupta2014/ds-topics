"""
https://practice.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1
"""
class Solution:
    def setBit(self, n):
        if n & (n + 1):
            return n | (n + 1)
        return n


solve = Solution()
print(solve.setBit(n=13))
print(solve.setBit(n=15))
print(solve.setBit(n=6))