"""
https://workat.tech/problem-solving/practice/trailing-zeroes

https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
"""
class Solution:
    def trailingZeroesInFactorial(self, n: int) -> int:
        count = 0

        while n >= 5:
            n //= 5
            count += n
        return count

solve = Solution()
print(solve.trailingZeroesInFactorial(n=0))
print(solve.trailingZeroesInFactorial(n=5))
print(solve.trailingZeroesInFactorial(n=10))
print(solve.trailingZeroesInFactorial(n=100))