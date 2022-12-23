"""
https://workat.tech/problem-solving/practice/merge-k-sorted-arrays

https://www.codingninjas.com/codestudio/problems/merge-k-sorted-arrays_975379?leftPanelTab=2
https://www.interviewbit.com/problems/merge-k-sorted-arrays/discussion/p/python-1-line-solution-using-heapq/302266/2019/#

https://www.youtube.com/watch?v=sI1oummM1OA
"""

import heapq
from heapq import merge


class Solution:
    def mergeKArrays(self, arr):
        # return list(merge(*arr))
        result = []
        k = len(arr)
        minHeap = []
        for row in range(k):
            heapq.heappush(minHeap, (arr[row][0], row, 0))

        while len(minHeap) > 0:
            ele, row, col = heapq.heappop(minHeap)
            result.append(ele)
            if col+1 < len(arr[row]):
                heapq.heappush(minHeap, (arr[row][col+1], row, col+1))
        return result




solve = Solution()
mat = [[1, 3, 7, 10],
        [3, 3, 6, 8],
        [2, 4, 7, 9]]
print(solve.mergeKArrays(mat))