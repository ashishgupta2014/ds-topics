"""
https://workat.tech/problem-solving/practice/divide-without-division-multiplication-mod

https://iq.opengenus.org/bitwise-division/
"""
class Solution:
    def divide(self, a: int, b: int) -> int:
        ans = 0  # the quotient is initialized

        neg = a < 0 or b < 0  # Checking if one of the numbers is negative

        if neg and a < 0 and b < 0:
            neg = False

        a = abs(a)  # making sure both the numbers
        b = abs(b)  # are positive

        for i in range(31, -1, -1):  # starting our loop

            if b << i <= a:  # checking if b multiplied by 2**i is <= a
                a -= b << i  # subtracting b << i from a
                ans += 1 << i  # adding 2 power i to the answer

        # and finally checking if the output should be negative and returning it
        return ans if neg == 0 else -1 * ans



solve = Solution()

print(solve.divide(a=15, b=4))

print(solve.divide(a=6, b=2))

print(solve.divide(a=15, b=-4))

print(solve.divide(a=-15, b=-4))