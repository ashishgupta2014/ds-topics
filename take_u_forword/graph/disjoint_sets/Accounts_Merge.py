"""
https://leetcode.com/problems/accounts-merge/description/

https://takeuforward.org/data-structure/accounts-merge-dsu-g-50/

https://www.youtube.com/watch?v=FMwpt_aQOGw
"""
from typing import List

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        map_mail_node = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if map_mail_node.get(mail) is None:
                    map_mail_node[mail] = i
                else:
                    ds.union_by_size(i, map_mail_node[mail])
        merge_mail = [[] for _ in range(n)]
        for key, value in map_mail_node.items():
            node = ds.find_parent(value)
            merge_mail[node].append(key)

        ans = []
        for i in range(n):
            if len(merge_mail[i]) == 0:
                continue
            merge_mail[i].sort()
            temp = [accounts[i][0]]
            temp.extend(merge_mail[i])
            ans.append(temp)
        return ans



solve = Solution()
print(solve.accountsMerge(accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],
                                    ["John","johnsmith@mail.com","john00@mail.com"],
                                    ["Mary","mary@mail.com"],
                                    ["John","johnnybravo@mail.com"]]))