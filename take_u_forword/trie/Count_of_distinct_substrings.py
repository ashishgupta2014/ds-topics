"""
https://takeuforward.org/data-structure/number-of-distinct-substrings-in-a-string-using-trie/


"""
class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.sub_string_counter = 0

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
                self.sub_string_counter += 1
            cur = cur.children[ch]

def countDistinctSubstring(s):
    tree = Trie()
    for i in range(len(s)):
        tree.insert(s[i:])
    return tree.sub_string_counter+1

print(countDistinctSubstring(s='ababa'))
print(countDistinctSubstring(s='ab'))