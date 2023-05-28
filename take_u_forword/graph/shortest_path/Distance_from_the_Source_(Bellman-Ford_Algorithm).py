"""
https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

https://www.youtube.com/watch?v=0vVofAhAYjc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42

https://takeuforward.org/data-structure/bellman-ford-algorithm-g-41/
"""
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        max_digit = 100000000
        dist = [max_digit]*V
        dist[S] = 0
        for _ in range(V-1):
            for u, v, w in edges:
                if dist[u] != max_digit and dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
        for u, v, w in edges:
            if dist[u] != max_digit and dist[u]+w < dist[v]:
                return [-1]
        return dist

solve = Solution()
print(solve.bellman_ford(V=3, edges=[[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], S=2))