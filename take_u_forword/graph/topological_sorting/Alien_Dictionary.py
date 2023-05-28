"""
https://practice.geeksforgeeks.org/problems/alien-dictionary/1

https://www.youtube.com/watch?v=U3N_je7tWAs&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=27
"""
from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def number_of_nodes(self):
        return len(self.graph)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def find_dependency(self):
        in_order = [0]*self.V
        for v in range(self.V):
            for x in self.graph[v]:
                in_order[x] += 1
        queue = [i for i, x in enumerate(in_order) if x == 0]

        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for v in self.graph[node]:
                in_order[v] -= 1
                if in_order[v] == 0:
                    queue.append(v)
        return result

class Solution:
    def findOrder(self, alien_dict, N, K):
        graph = Graph(K)
        for i in range(1, N):
            word1 = alien_dict[i-1]
            word2 = alien_dict[i]
            j = 0
            k = 0
            while j < len(word1) and k < len(word2):
                if word1[j] != word2[k]:
                    v = ord(word1[j])-97
                    w = ord(word2[k])-97
                    graph.addEdge(v, w)
                    break
                j += 1
                k += 1
        return [chr(i+97) for i in graph.find_dependency()]





class sort_by_order:
    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    n = 5
    k = 4
    alien_dict = ["baa","abcd","abca","cab","cad"]
    duplicate_dict = alien_dict.copy()
    ob = Solution()
    order = ob.findOrder(alien_dict, n, k)
    s = ""
    for i in range(k):
        s += chr(97 + i)
    l = list(order)
    l.sort()
    l = "".join(l)
    if s != l:
        print(0)
    else:
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)

        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)

# } Driver Code Ends