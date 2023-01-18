"""
https://workat.tech/problem-solving/practice/is-graph-bipartite

https://www.youtube.com/watch?v=-vu34sct1g8

https://www.youtube.com/watch?v=KG5YFfR0j8A
"""

class Solution:
    def isBipartite(self, adjList) -> bool:
        color = [-1]*len(adjList)

        color[0] = 0
        queue = [0]

        while queue:
            node = queue.pop(0)
            connected_nodes = adjList[node]
            for n in connected_nodes:
                if color[n] == color[node]:
                    return False
                if color[n] == -1:
                    if color[node] == 0:
                        color[n] = 1
                    else:
                        color[n] = 0
                    queue.append(n)
        return True

solve = Solution()
print(solve.isBipartite(adjList=[[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]]))
print(solve.isBipartite(adjList=[[1, 3], [0, 2], [1, 3], [0, 2]]))



