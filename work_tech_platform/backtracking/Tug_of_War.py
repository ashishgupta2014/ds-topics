"""
https://workat.tech/problem-solving/practice/tug-of-war
"""

class Solution:
    min_diff = 0
    def backtracking(self, A, selected, start, cur_sum, total_sum):
        if len(A) <= start:
            return
        if selected == len(A)//2:
            self.min_diff = min(self.min_diff, abs(total_sum - 2*cur_sum))
            return
        self.backtracking(A, selected+1, start+1, cur_sum+A[start], total_sum)
        self.backtracking(A, selected, start+1, cur_sum, total_sum)
    def divideGroup(self, A):
        total_sum = sum(A)
        self.min_diff = float('inf')
        self.backtracking(A, 0, 0, 0, total_sum)
        return self.min_diff


solve = Solution()
arr = [5, 1, 2, 8]

print(solve.divideGroup(arr))


