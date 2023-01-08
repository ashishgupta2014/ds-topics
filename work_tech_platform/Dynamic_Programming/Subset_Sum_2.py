"""
https://workat.tech/problem-solving/practice/subset-sum-2

"""
from typing import List


class Solution:

    def backtracking(self, A, target, index, cur):
        if cur == target:
            return True
        if index >= len(A) or cur > target:
            return False
        cur += A[index]
        if self.backtracking(A, target, index + 1, cur):
            return True
        cur -= A[index]
        if self.backtracking(A, target, index + 1, cur):
            return True
        return False

    def subsetSum(self, A: List[int], target: int) -> int:
        return self.backtracking(A, target, 0, 0)

solve = Solution()

print(solve.subsetSum(A=[3, 0, 4, 9, 5], target=13))

print(solve.subsetSum(A=[3, 0, 4, 9, 5], target=20))

print(solve.subsetSum(A=[2, 2, 5, 4, 8], target=16))

print(solve.subsetSum(A=[1], target=2))
