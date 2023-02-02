"""
https://workat.tech/problem-solving/practice/combination-sum-1

https://leetcode.com/problems/combination-sum/description/

https://www.youtube.com/watch?v=GBKI9VSKdGg
"""
class Solution:
    res = []
    def backtracking(self, A, target, index, cur):
        if target == sum(cur):
            self.res.append(cur[:])
            return
        elif target < sum(cur):
            return
        elif len(A) <= index:
            return
        cur.append(A[index])
        # include num
        self.backtracking(A, target, index, cur)
        cur.pop()

        # exclude num
        self.backtracking(A, target, index+1, cur)

    def combinationSum(self, A, val: int):
        self.res = []
        self.backtracking(A, val, 0, [])
        return self.res

solve = Solution()

arr =  [1, 2]
t = 4
print(solve.combinationSum(arr, t))
print(solve.combinationSum(A=[2, 3, 6, 7], val=7))
