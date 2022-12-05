"""
https://workat.tech/problem-solving/practice/is-perfect-square
"""


class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        if n == 0 or n == 1:
            return True
        low = 1
        high = n
        while low <= high:
            mid = (high + low) // 2

            if mid * mid == n:
                return True
            elif mid * mid > n:
                high = mid - 1
            else:
                low = mid + 1
        return False


solve = Solution()
n = 25
print(solve.isPerfectSquare(n))
