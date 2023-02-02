"""
https://leetcode.com/problems/count-good-numbers/
https://www.youtube.com/watch?v=CctVpEGgNf0
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
    def countGoodNumbers(self, n: int) -> int:
        # even = n//2 + n%2
        # odd = n//2
        # return (self.power(5, even) * self.power(4, odd)) % 1_000_000_007
        evenplace = (n // 2)
        oddplace = ((n // 2) + n % 2)

        t1 = pow(4, evenplace, 1000000007)
        t2 = pow(5, oddplace, 1000000007)

        return (t1 * t2) % 1000000007

solve = Solution()
print(solve.countGoodNumbers(n=1))
print(solve.countGoodNumbers(n=50))