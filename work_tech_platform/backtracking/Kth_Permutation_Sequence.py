"""
https://workat.tech/problem-solving/practice/kth-permutation-sequence

https://www.youtube.com/watch?v=wT7gcXLYoao
"""

import math


class Solution:
    def getKthPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        fact = math.factorial(n - 1)
        ans = ''
        k -= 1
        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
        return ans


solve = Solution()

print(solve.getKthPermutation(n=4, k=3))

