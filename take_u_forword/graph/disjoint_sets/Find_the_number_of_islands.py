"""
https://leetcode.com/problems/number-of-islands-ii/
https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/305.html
https://leetcode.ca/all/305.html
https://takeuforward.org/graph/number-of-islands-ii-online-queries-dsu-g-51/

https://www.youtube.com/watch?v=Rn6B-Q4SNyA
"""
class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        return self.find_parent(self.parent[node])

    def union_by_rank(self, u, v):
        parent_of_u = self.find_parent(u)
        parent_of_v = self.find_parent(v)
        if self.rank[parent_of_u] < self.rank[parent_of_v]:
            self.parent[parent_of_u] = parent_of_v
        elif self.rank[parent_of_u] > self.rank[parent_of_v]:
            self.parent[parent_of_v] = parent_of_u
        else:
            self.parent[parent_of_v] = parent_of_u
            self.rank[parent_of_u] += 1

    def union_by_size(self, u, v):
        parent_of_u = self.find_parent(u)
        parent_of_v = self.find_parent(v)
        if parent_of_v == parent_of_u:
            return
        elif self.size[parent_of_u] < self.size[parent_of_v]:
            self.parent[parent_of_u] = parent_of_v
            self.size[parent_of_v] += self.size[parent_of_u]
        else:
            self.parent[parent_of_v] = parent_of_u
            self.size[parent_of_u] += self.size[parent_of_v]

class Solution:
    def numIslands(self, grid, m, n):
        ds = DisjointSet(m*n)
        visited = [[False]*m for _ in range(n)]
        count = 0
        ans = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for row, col in grid:
            if visited[row][col]:
                ans.append(count)
                continue
            visited[row][col] = True
            count += 1
            for x, y in directions:
                r = row+x
                c = col+y
                if 0 <= r < n and 0 <= c < m and visited[r][c]:
                    node_no = row*m+col
                    adj_node_no = r*m+c
                    if ds.find_parent(node_no) != ds.find_parent(adj_node_no):
                        count -= 1
                        ds.union_by_size(node_no, adj_node_no)
            ans.append(count)
        return ans



solve = Solution()
print(solve.numIslands(grid=[[0, 0],
                             [0, 0],
                             [1, 1],
                             [1, 0],
                             [0, 1],
                             [0, 3],
                             [1, 3],
                             [0, 4],
                             [3, 2],
                             [2, 2],
                             [1, 2],
                             [0, 2]], m=5, n=4))