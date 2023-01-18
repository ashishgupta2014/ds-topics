"""
https://workat.tech/problem-solving/practice/detect-cycle-graph-union-find

https://iq.opengenus.org/detect-cycle-in-undirected-graph/

https://www.youtube.com/watch?v=3gbO7FDYNFQ
"""
from typing import List

class UnionFind:
    def __init__(self, n):
        self.disjoint_set = self.make_set(n)

    @staticmethod
    def make_set(n):
        return {vertex:vertex for vertex in range(n)}#Initializing n subsets and make contained vertex itself the set-representative for each subset
    def find(self,vertex):
        if self.disjoint_set[vertex]==vertex:#A set-representative can be found if v:v
            return vertex
        return self.find(self.disjoint_set[vertex])
    def union(self,x,y):
        set_representative_X=self.find(x)#find set-representative of x
        set_representative_Y=self.find(y)#find set-representative of y
        self.disjoint_set[set_representative_Y]=set_representative_X#make set-representative of y as x
class Solution:
    def isCyclic(self, n: int, adjList: List[List[int]]) -> bool:
        ds = UnionFind(n)
        for x, y in adjList:
            if ds.find(x) == ds.find(y):  # if set-representatives of both the vertices are the same then cycle exists
                # print("Cycle exists in the graph!")
                return True
            ds.union(x, y)  # merge subsets x and y
        # print("Cycle doesn't exist in the graph!")
        return False



solve = Solution()
print(solve.isCyclic(n=7, adjList=[[0, 1], [0, 3], [0, 6], [1, 2], [1, 4], [4, 5]]))

print(solve.isCyclic(n=3, adjList=[[0, 1], [1, 2], [0, 2]]))