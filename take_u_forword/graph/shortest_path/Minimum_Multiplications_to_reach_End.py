"""
https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

https://www.youtube.com/watch?v=_BvEJ3VIDWw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=40

https://takeuforward.org/graph/g-39-minimum-multiplications-to-reach-end/
"""
from typing import List


class Solution:

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        queue = [(start, 0)]
        n = 99999
        dist = [float('inf')]*n
        dist[start] = 0

        while queue:
            node, steps = queue.pop(0)
            for x in arr:
                next_step = steps + 1
                num = (x*node) % 100000
                if next_step < dist[num]:
                    dist[num] = next_step
                    if num == end:
                        return next_step
                    queue.append((num, next_step))
        return -1


solve = Solution()
print(solve.minimumMultiplications(arr=[2, 5, 7], start=3, end=30))