"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

https://www.youtube.com/watch?v=9XybHVqTHcQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=39
"""
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))
        queue = [(0, k, src)]
        arr = [float('inf')]*n
        while queue:
            price, stops, node = queue.pop(0)
            for adj_node, p in graph[node]:
                if stops > 0 or adj_node == dst:
                    cur_price = price+p
                    if arr[adj_node] > cur_price:
                        arr[adj_node] = cur_price
                        queue.append((cur_price, stops-1, adj_node))
        return arr[dst]

solve = Solution()
print(solve.findCheapestPrice(n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1))