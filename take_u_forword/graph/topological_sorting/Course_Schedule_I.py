from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def dfs(self, currentNode, visited, cycle):
        if currentNode in cycle:
            return False
        if currentNode in visited:
            return True
        cycle.add(currentNode)
        for node in self.graph[currentNode]:
            if node not in visited:
                if not self.dfs(node, visited, cycle):
                    return False
        visited.add(currentNode)
        cycle.remove(currentNode)
        return True

    def find_dependency(self):
        visited, cycle = set(), set()
        for currentNode in range(self.V):
            if currentNode not in visited:
                if not self.dfs(currentNode, visited, cycle):
                    return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        graph = Graph(numCourses)
        for v, w in prerequisites:
            graph.addEdge(v, w)
        return graph.find_dependency()

solve = Solution()
print(solve.canFinish(numCourses = 2, prerequisites = [[1,0]]))

print(solve.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))