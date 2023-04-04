"""
https://practice.geeksforgeeks.org/problems/page-faults-in-lru5603/1
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity):
        self.lookup = dict()  # val to node
        self.capacity = capacity
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def __remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = None
        node.next = None

    def get(self, val):
        if val not in self.lookup:
            return False

        node = self.lookup[val]
        self.__remove(node)
        self.__add(node)
        return True

    def insert(self, val):
        if val in self.lookup:
            return False

        node = Node(val)
        if len(self.lookup) == self.capacity:
            first = self.head.next
            del self.lookup[first.val]
            self.__remove(first)
        self.__add(node)
        self.lookup[val] = node
        return True


class Solution:
    def pageFaults(self, N, C, pages):
        lru = LRU(C)
        count = 0
        for p in pages:
            if lru.get(p):
                continue

            count += 1
            lru.insert(p)
        return count


solve = Solution()
print(solve.pageFaults(N=9, C=4, pages=[5, 0, 1, 3, 2, 4, 1, 0, 5]))