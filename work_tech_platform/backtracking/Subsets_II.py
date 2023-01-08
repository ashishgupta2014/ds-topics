"""
https://workat.tech/problem-solving/practice/subsets-ii

https://leetcode.com/problems/subsets-ii/description/

https://www.youtube.com/watch?v=RIn3gOkbhQE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=11
https://www.youtube.com/watch?v=Vn2v6ajA7U0
"""
class Solution:

    nums = []
    res = []
    def backtracking(self, index, cur):
        if index >= len(self.nums):
            self.res.append(cur[:])
            return
        # Include element
        cur.append(self.nums[index])
        self.backtracking(index+1, cur)
        cur.pop()

        # Not include element
        while index < len(self.nums)-1 and self.nums[index] == self.nums[index+1]:
            index += 1
        self.backtracking(index + 1, cur)
    def subsets(self, A):
        self.nums = sorted(A)
        self.res = []
        self.backtracking(0, [])
        return self.res


solve = Solution()
a = [5]
print(solve.subsets(a))
a = [2, 4]
print(solve.subsets(a))
a = [1, 3, 3]
print(solve.subsets(a))