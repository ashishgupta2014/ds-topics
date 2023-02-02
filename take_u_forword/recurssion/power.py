"""
https://leetcode.com/problems/powx-n/description/
"""
class Solution:
    def power(self, x, y):
        if y == 0:
            return 1
        elif y == -1:
            return .5
        temp = self.power(x, y // 2)

        if y % 2 == 0:
            return temp * temp
        else:
            return x * temp * temp
solve = Solution()
print(solve.power(3, -4))
print(solve.power(3, 4))