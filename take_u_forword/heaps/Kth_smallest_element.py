"""
https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1
"""
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heapq.heapify(arr)
        for _ in range(k-1):
            _ = heapq.heappop(arr)
        return heapq.heappop(arr)


solve = Solution()
print(solve.kthSmallest(arr=[7, 10, 4, 3, 20, 15], l=0, r=6, k=3))