"""
https://workat.tech/problem-solving/practice/subset-sum
https://www.youtube.com/watch?v=kyLxTdsT8ws
"""
class Solution:
    def backtracking(self, A, target, index, cur):
        if cur == target:
            return True
        elif len(A) <= index or cur > target:
            return False
        cur += A[index]
        if self.backtracking(A, target, index+1, cur):
            return True

        cur -= A[index]
        if self.backtracking(A, target, index + 1, cur):
            return True
        return False

    def hasValidSubset(self, A, target: int) -> bool:
        return self.backtracking(A, target, 0, 0)


solve = Solution()

a = [1, 3, 4, 2, 9]
t = 13
print(solve.hasValidSubset(a, t))


