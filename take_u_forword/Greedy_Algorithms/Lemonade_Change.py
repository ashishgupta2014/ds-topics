"""
https://leetcode.com/problems/lemonade-change/description/
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        for b in bills:
            d[b] = 1 + d.get(b, 0)
            if b == 10:
                if d[5] > 0:
                    d[5] -= 1
                else:
                    return False
            if b == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
        return True
solve = Solution()
print(solve.lemonadeChange(bills=[5,5,5,10,20]))
print(solve.lemonadeChange(bills=[5,5,10,10,20]))