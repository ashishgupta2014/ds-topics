from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def dfs(self, currentNode, visited, cycle, result):
        if currentNode in cycle:
            return False
        if currentNode in visited:
            return True
        cycle.add(currentNode)
        for node in self.graph[currentNode]:
            if node not in visited:
                if not self.dfs(node, visited, cycle, result):
                    return False
        visited.add(currentNode)
        result.append(currentNode)
        cycle.remove(currentNode)
        return True

    def find_dependency(self):
        visited, cycle = set(), set()
        result = []
        for currentNode in range(self.V):
            if currentNode not in visited:
                if not self.dfs(currentNode, visited, cycle, result):
                    return []
        return result


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = Graph(numCourses)
        for v, w in prerequisites:
            graph.addEdge(v, w)
        return graph.find_dependency()


solve = Solution()
# courses = [[1, 0], [2, 0], [3, 1], [3, 2]]
# n = 4
courses = [[1, 0], [0, 1]]
n = 2
print(solve.findOrder(n, courses))
