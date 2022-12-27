"""
https://workat.tech/problem-solving/practice/exponent-with-modulus

https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
"""

class Solution:
    def getModulatedPower(self, x: int, y: int, z: int) -> int:
        result = 1
        x %= z
        if x == 0:
            return 0

        while y > 0:
            # is odd or even y%2 == 1
            if y & 1 == 1:
                result = (result * x) % z
            # division operation y //= 2
            y >>= 1
            x = (x * x) % z
        return result

solve = Solution()

print(solve.getModulatedPower(3,3, 2))