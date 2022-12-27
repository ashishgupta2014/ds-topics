"""
https://workat.tech/problem-solving/topics/maths-and-bits/practice

https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
"""
class Solution:
    def countSetBits(self, n: int) -> int:
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count

solve = Solution()
print(solve.countSetBits(10))



