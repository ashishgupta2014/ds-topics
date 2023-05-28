"""
https://leetcode.com/problems/network-delay-time/description/

https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        queue = [(k, 0)]
        heapq.heapify(queue)
        arr = [-1]*n
        arr[k-1] = 0
        while queue:
            u, wt = heapq.heappop(queue)
            for v, w in graph[u]:
                cur_wt = wt+w
                if arr[v-1] == -1 or arr[v-1] > cur_wt:
                    arr[v-1] = cur_wt
                    heapq.heappush(queue, (v, cur_wt))
        return -1 if min(arr) == -1 else max(arr)



solve = Solution()
print(solve.networkDelayTime(times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2))