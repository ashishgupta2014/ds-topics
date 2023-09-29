"""
https://practice.geeksforgeeks.org/problems/swap-two-numbers3844/1
"""
class Solution:
    def get(self, a, b):
        s = a^b
        a = s^a
        b = s^b
        return a, b

solve = Solution()
print(solve.get(a=4, b=7))