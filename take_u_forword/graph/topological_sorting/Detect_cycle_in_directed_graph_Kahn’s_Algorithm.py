"""
https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

https://www.youtube.com/watch?v=iTBaI90lpDQ&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=24
"""
class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        in_order = [0]*V
        for v in range(V):
            for e in adj[v]:
                in_order[e] += 1
        queue = [i for i, e in enumerate(in_order) if e == 0]
        count = 0
        while queue:
            node = queue.pop(0)
            count += 1
            for n in adj[node]:
                in_order[n] -= 1
                if in_order[n] == 0:
                    queue.append(n)
        if count == V:
            return False
        return True



if __name__ == '__main__':

        ob = Solution()
        N = 4
        adj = [[1, 2], [2], [0, 3], [3]]
        res = ob.isCyclic(N, adj)
        print(res)

        N = 3
        adj = [[1], [2], []]
        res = ob.isCyclic(N, adj)
        print(res)