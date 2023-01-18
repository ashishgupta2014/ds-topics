"""
This is the Node class definition

https://workat.tech/problem-solving/practice/clone-graph

https://www.youtube.com/watch?v=mQeF6bN8hMk

"""

class Node:
    def __init__(self, value=0, neighbours=None):
        if neighbours is None:
            neighbours = []
        self.value = value
        self.neighbours = neighbours[:]


class Solution:

    def dfs(self, root: Node, visited:dict):
        if root in visited:
            return visited[root]
        copy = Node(root.value)
        visited[root] = copy
        for n in root.neighbours:
            copy.neighbours.append(self.dfs(n, visited))
        return copy

    def cloneGraph(self, node: Node) -> Node:
        visited = {}
        return self.dfs(node, visited)

solve = Solution()

node0 = Node(value=0)
node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)

node0.neighbours = [node1, node2, node3]
node1.neighbours = [node0]
node2.neighbours = [node0, node3]
node3.neighbours = [node0, node2]

print(solve.cloneGraph(node0))




