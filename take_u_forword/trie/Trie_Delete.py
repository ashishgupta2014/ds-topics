"""
https://practice.geeksforgeeks.org/problems/trie-delete/1

https://takeuforward.org/data-structure/implement-trie-ii/
"""
class TrieNode:

    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = TrieNode()


# use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch) - ord('a')


# Function to insert string into TRIE.
def insert(root, key):
    # if not present, we insert key into trie. If the key is prefix
    # of trie node, we just mark the leaf node.
    for e in key:
        idx = charToIndex(e)

        if not root.children[idx]:
            root.children[idx] = TrieNode()

        root = root.children[idx]

    # marking last node as leaf.
    root.isEndOfWord = True


# Function to use TRIE data structure and search the given string.
def search(root, key):
    for e in key:
        idx = charToIndex(e)

        if not root.children[idx]:
            return

        root = root.children[idx]

    # returning true if key is present else false.
    return root.isEndOfWord

class Solution:
    def deleteKey(self, root, key, i=0):
        if i >= len(key):
            return
        idx = charToIndex(key[i])
        if not root.children[idx]:
            return
        prev = root
        root = root.children[idx]
        self.deleteKey(root, key, i + 1)
        if root.isEndOfWord:
            root.children[idx] = None
            root.isEndOfWord = False
            if prev is not None:
                prev.isEndOfWord = True





if __name__ == '__main__':
    n = 8
    arr = 'the a there answer any by bye their'.split()
    key = 'the'

    t = Trie()

    for s in arr:
        insert(t.root, s)

    Solution().deleteKey(t.root, key)

    if search(t.root, key):
        print(0)
    else:
        print(1)

    if search(t.root, 'there'):
        print(0)
    else:
        print(1)

    if search(t.root, 'their'):
        print(0)
    else:
        print(1)