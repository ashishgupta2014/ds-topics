"""
https://workat.tech/problem-solving/practice/kth-largest-from-data-stream

https://leetcode.com/problems/kth-largest-element-in-a-stream/solutions/534144/python-sol-by-min-heap-80-w-hint/?orderBy=most_relevant&languageTags=python3

https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
"""
import heapq
class KthLargest:
    def __init__(self, k: int):
        """initialize your data structure here."""
        self.k = k
        self.arr = []
        heapq.heapify(self.arr)

    def add(self, num: int) -> int:
        ans = -1
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, num)
            if len(self.arr) == self.k:
                ans  = self.arr[0]
        else:
            heapq.heappushpop(self.arr, num)
            ans = abs(self.arr[0])
        return ans

arr = [2, 4, 3, 7, 4, 5, 8]
solve = KthLargest(k=3)
for i in arr:
    print(solve.add(i))