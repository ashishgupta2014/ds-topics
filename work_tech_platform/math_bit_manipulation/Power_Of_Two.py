"""
https://workat.tech/problem-solving/practice/power-of-two

https://www.geeksforgeeks.org/program-to-find-whether-a-given-number-is-power-of-2/
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2

        return True

solve = Solution()
print(solve.isPowerOfTwo(10))
print(solve.isPowerOfTwo(16))
print(solve.isPowerOfTwo(17))
print(solve.isPowerOfTwo(18))
print(solve.isPowerOfTwo(22))

