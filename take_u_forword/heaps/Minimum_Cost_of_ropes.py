"""
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
"""
import heapq


class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        heapq.heapify(arr)

        cost = 0
        while len(arr) > 1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            cost += a + b
            heapq.heappush(arr, a + b)
        return cost
solve = Solution()
print(solve.minCost(arr=[4, 3, 2, 6], n=4))