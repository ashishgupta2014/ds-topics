"""
https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
https://leetcode.com/problems/split-array-largest-sum/description/ same problem

https://www.youtube.com/watch?v=gYmWHvRHu-s&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=70
"""
class Solution:

    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        if M > N:
            return -1
        low = min(A)
        high = sum(A)
        res = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            if self.is_possible(mid, A, M):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res

    def is_possible(self, pages, A, M):
        std = 1
        count = 0
        for p in range(len(A)):
            if A[p] > pages:
                return False
            count += A[p]
            if count > pages:
                std += 1
                count = A[p]
        if std > M:
            return False
        return True


solve = Solution()
print(solve.findPages(A=[12,34,67,90], N=4, M=2))