"""
https://workat.tech/problem-solving/practice/median-from-data-stream

https://www.youtube.com/watch?v=itmhHWaHupI
"""
import heapq

class MedianCalculator:
    def __init__(self):
        """initialize your data structure here."""
        self.small_max_heap = []
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max_heap, -1 * num)
        if self.small_max_heap and self.large_min_heap:
            if (-1*self.small_max_heap[0]) > self.large_min_heap[0]:
                num =  -1*heapq.heappop(self.small_max_heap)
                heapq.heappush(self.large_min_heap, num)

        if len(self.small_max_heap) > len(self.large_min_heap):
            num = -1*heapq.heappop(self.small_max_heap)
            heapq.heappush(self.large_min_heap, num)

        if len(self.small_max_heap) < len(self.large_min_heap):
            num = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap, -1*num)

    def getMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return -1*self.small_max_heap[0]
        elif len(self.small_max_heap) < len(self.large_min_heap):
            return self.large_min_heap[0]
        else:
            return ((-1*self.small_max_heap[0])+self.large_min_heap[0])/2

solve = MedianCalculator()

arr = [2, 1, 5, 4]

for i in arr:
    solve.addNum(i)
    print(solve.getMedian())