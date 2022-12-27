"""
https://workat.tech/problem-solving/practice/square-without-multiply-divide-pow

https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/
"""
class Solution:
    def findSquare(self, num: int) -> int:
        # Base case
        if num == 0:
            return 0

        # Handle negative number
        if num < 0:
            num = -num

        # Get floor(n/2) using
        # right shift
        x = num >> 1

        # If n is odd
        if num & 1:
            return ((self.findSquare(x) << 2)
                    + (x << 2) + 1)

        # If n is even
        else:
            return self.findSquare(x) << 2



solve = Solution()

print(solve.findSquare(num=1))

print(solve.findSquare(num=5))

print(solve.findSquare(num=10))