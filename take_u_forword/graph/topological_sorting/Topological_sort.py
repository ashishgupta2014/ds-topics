"""
https://practice.geeksforgeeks.org/problems/topological-sort/1

DFS
    https://www.youtube.com/watch?v=5lZ0iJMrUMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22

    https://takeuforward.org/data-structure/topological-sort-algorithm-dfs-g-21/

BFS
    https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=23
    https://takeuforward.org/data-structure/kahns-algorithm-topological-sort-algorithm-bfs-g-22/
"""
class Solution:

    def dfs(self, node, visited, adj, stack):
        visited[node] = True
        for n in adj[node]:
            if not visited[n]:
                self.dfs(n, visited, adj, stack)
        stack.append(node)
    def topoSort(self, V, adj):
        visisted = [False]*V
        stack = []
        for v in range(V):
            if not visisted[v]:
                self.dfs(v, visisted, adj, stack)
        return stack[::-1]

# Code here


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':

        ob = Solution()
        N = 4
        adj = [[1, 2], [2], [0, 3], [3]]
        res = ob.topoSort(N, adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
