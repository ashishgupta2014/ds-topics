"""
https://workat.tech/problem-solving/practice/combination-sum-2
"""
class Solution:
    arr = []
    target = None
    res = []
    def backtracking(self, index, cur):
        if sum(cur) == self.target:
            self.res.append(cur[:])
            return
        elif sum(cur) > self.target or len(self.arr) <= index:
            return
        # include num
        cur.append(self.arr[index])
        self.backtracking(index+1, cur)
        cur.pop()
        # avoid repetition
        while len(self.arr)-1 > index and self.arr[index] == self.arr[index+1]:
            index += 1
        # exclude num
        self.backtracking(index+1, cur)
    def combinationSum(self, A, val: int):
        self.arr = sorted(A)
        self.target = val
        self.res = []
        self.backtracking(0, [])
        return self.res



solve = Solution()

arr = [10, 1, 2, 7, 6, 1, 5]
target = 8

print(solve.combinationSum(arr, target))