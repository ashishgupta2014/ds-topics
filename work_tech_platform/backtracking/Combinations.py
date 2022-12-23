"""
https://workat.tech/problem-solving/practice/combinations
"""
class Solution:

    def backtracking(self, n, k, index, res, cur):

        if len(cur) == k:
            res.append(cur[:])
            return
        if index == n:
            return
        # include num
        cur.append(index)
        self.backtracking(n, k, index + 1, res, cur)
        cur.pop()
        # exclude num
        self.backtracking(n, k, index + 1, res, cur)

    def combinations(self, n: int, k: int):
        res = []
        cur = []
        self.backtracking(n+1, k, 1, res, cur)
        return res

solve = Solution()

N = 4
K = 2

print(solve.combinations(N, K))

N = 3
K = 3

print(solve.combinations(N, K))