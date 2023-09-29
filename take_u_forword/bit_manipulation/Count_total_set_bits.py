"""
https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
"""
class Solution:
    def countSetBits(self, n):
        count = 0
        i = 1

        while i <= n:
            quotient = n // (i << 1)
            count += quotient * i

            remainder = n % (i << 1)
            count += max(remainder - i + 1, 0)

            i = i << 1

        return count

solve = Solution()
print(solve.countSetBits(n=2))