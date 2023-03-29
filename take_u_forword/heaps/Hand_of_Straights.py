"""
https://leetcode.com/problems/hand-of-straights/

https://www.youtube.com/watch?v=amnrMCVd2YI
"""
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counter = {}
        for num in hand:
            counter[num] = 1 + counter.get(num, 0)
        min_heap = list(counter.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for num in range(first, first+groupSize):
                if num not in counter:
                    return False
                counter[num] -= 1
                if counter[num] == 0:
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True



solve = Solution()
print(solve.isNStraightHand(hand=[1,2,3,6,2,3,4,7,8], groupSize=3))
print(solve.isNStraightHand(hand=[1,2,3,4,5], groupSize=4))