"""
https://practice.geeksforgeeks.org/problems/bit-manipulation-1666686020/1
"""
class Solution:
    def bitManipulation(self, n, i):
        get_i_bit = (n & (1 << (i - 1))) >> (i - 1)
        mask = 1 << i-1
        set_i_bit = (mask | n)
        clear_i_bit = (~mask & n)
        return get_i_bit, set_i_bit, clear_i_bit

solve = Solution()
print(solve.bitManipulation(n=70, i=3))
print(solve.bitManipulation(n=8, i=1))