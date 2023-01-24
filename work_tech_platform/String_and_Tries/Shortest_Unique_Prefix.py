"""
https://workat.tech/problem-solving/practice/shortest-unique-prefix

https://www.youtube.com/watch?v=CB-WeyCFjlc
"""
from typing import List

class Trie:
    def __init__(self):
        self.character = {}
        self.freq = 0

class Solution:

    def insert(self, root, word):
        cur = root
        for ch in word:
            cur.freq += 1
            cur = cur.character.setdefault(ch, Trie())
    def getShortestUniquePrefixes(self, words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            self.insert(root, word)
        prefix =[]
        for word in words:
            cur = root
            pre = []
            for w in word:
                cur = cur.character[w]
                freq = cur.freq
                pre.append(w)
                if freq == 1:
                    break
            prefix.append(''.join(pre))

        return prefix

solve = Solution()
print(solve.getShortestUniquePrefixes(words=["program", "code", "process", "coding", "type", "print"]))



