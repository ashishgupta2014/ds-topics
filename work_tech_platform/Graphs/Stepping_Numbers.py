"""
https://workat.tech/problem-solving/practice/stepping-numbers

https://workat.tech/problem-solving/approach/sn/stepping-numbers
"""
from typing import List


class Solution:
    def getSteppingNumbers(self, begin: int, end: int) -> List[int]:
        initial_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        queue = []
        queue.extend(initial_values[1:])
        if begin == 0:
            ans = [0]
        else:
            ans = []

        while queue:
            num = queue.pop(0)
            if begin <= num <= end:
                ans.append(num)
            last_digit = num % 10
            num *= 10
            if last_digit:
                child = num + initial_values[last_digit-1]
                if child <= end:
                    queue.append(child)
            if last_digit != 9:
                child = num + initial_values[last_digit+1]
                if child <= end:
                    queue.append(child)
        return ans

solve = Solution()
print(solve.getSteppingNumbers(begin=8, end=15))
print(solve.getSteppingNumbers(begin=15, end=15))
print(solve.getSteppingNumbers(begin=10, end=10))




