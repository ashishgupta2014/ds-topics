"""
https://workat.tech/problem-solving/practice/subsets

https://leetcode.com/problems/subsets/description/

https://www.youtube.com/watch?v=REOH22Xwdkk
"""
class Solution(object):
    nums = []
    res = []
    def backtracking(self, index, cur):
        if len(self.nums) <= index:
            self.res.append(cur[:])
            return
        # include the element
        cur.append(self.nums[index])
        self.backtracking(index+1, cur)
        cur.pop()

        # not include the element
        self.backtracking(index+1, cur)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.res = []
        self.backtracking(0, [])
        return self.res

solve = Solution()

A = [1, 3, 2]

print(solve.subsets(A))

