"""
https://workat.tech/problem-solving/practice/sort-almost-sorted

https://www.geeksforgeeks.org/nearly-sorted-algorithm/
"""
import heapq


class Solution:
    def sortAlmostSorted(self, A, k: int):
        minheap = A[:k + 1]
        heapq.heapify(minheap)

        index = 0
        for i in range(k + 1, len(A)):
            A[index] = heapq.heappop(minheap)
            index += 1
            heapq.heappush(minheap, A[i])
        while minheap:
            A[index] = heapq.heappop(minheap)
            index += 1

solve = Solution()
arr = [2, 4, 1, 5, 3, 7, 8, 6, 10, 9]
solve.sortAlmostSorted(arr, k=2)
print(arr)



