"""
https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1
"""
class Solution:

    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        mask = 1 << k
        return mask & n

solve = Solution()
print(solve.checkKthBit(13, 2))