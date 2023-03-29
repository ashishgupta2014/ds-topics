"""
https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
"""
import heapq
class Solution:
    def mergeKArrays(self, arr, K):
        ans=[]
        for i in arr:
            for j in i:
                heapq.heappush(ans,j)
        res=[]
        while ans:
            c=heapq.heappop(ans)
            heapq.heappush(res,c)
        return res


solve = Solution()
print(solve.mergeKArrays(arr=[[1,2,3],[4,5,6],[7,8,9]], K=3))