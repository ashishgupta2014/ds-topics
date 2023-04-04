"""
https://practice.geeksforgeeks.org/problems/shortest-job-first/1
"""
class Solution:
    def solve(self, bt):
        bt.sort()
        n = len(bt)
        prefix = [0]*n
        prefix[0] = bt[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1]+bt[i]
        s = 0
        for i in range(n-1):
            s += prefix[i]
        return s//n


solve = Solution()
print(solve.solve(bt=[4,3,7,1,2]))