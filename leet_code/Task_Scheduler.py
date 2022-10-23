import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int):
        max_heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(max_heap)
        time = 0
        queue = []
        while max_heap or queue:
            time += 1
            if max_heap:
                task_count = 1 + heapq.heappop(max_heap)
                if task_count:
                    queue.append((task_count, time + n))
            if queue and queue[0][1] == time:
                task_count, _ = queue.pop(0)
                heapq.heappush(max_heap, task_count)
        return time


# tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
# n = 2

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
solve = Solution()
print(solve.leastInterval(tasks, n))
