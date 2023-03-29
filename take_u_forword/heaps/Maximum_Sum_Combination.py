"""
https://practice.geeksforgeeks.org/problems/maximum-sum-combination/1
"""
import heapq


class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort()
        B.sort()
        ans = []
        pq = []
        for i in range(N):
            heapq.heappush(pq, (-(A[i] + B[N - 1]), i, N - 1))

        while pq and K > 0:
            vl, i, N = heapq.heappop(pq)
            ans.append(-vl)
            if N > 0:
                heapq.heappush(pq, (-(A[i] + B[N - 1]), i, N - 1))
            K -= 1

        return ans

solve = Solution()
print(solve.maxCombinations(N=4, K=3, A=[1, 4, 2, 3], B=[2, 5, 1, 6]))