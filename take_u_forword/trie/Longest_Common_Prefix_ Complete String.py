"""
https://www.codingninjas.com/codestudio/problems/complete-string_2687860

https://www.youtube.com/watch?v=AWnBa91lThI&list=PLgUwDviBIf0pcIDCZnxhv0LkHf5KzG9zp&index=4

https://github.com/striver79/StriversTrieSeries/blob/main/L3_Complete_String_Java
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.endofword = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur.word_count += 1
            cur = cur.children[ch]
        cur.endofword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.endofword == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True

    def get_all_common_prefix_exits(self, word):
        cur = self.root
        flag = True
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            flag = flag and cur.endofword

        return flag



class Solution:
    def completeString(self, arr):
        tree  = Trie()
        for word in arr:
            tree.insert(word)
        longest = ''
        for word in arr:
            if tree.get_all_common_prefix_exits(word):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest) and word < longest:
                    longest = word
        return longest if len(longest) > 0 else None


solve = Solution()
print(solve.completeString(arr='n ni nin ninj ninja ninga'.split(' ')))
print(solve.completeString(arr='g l lm ga lmn gaz'.split(' ')))
print(solve.completeString(arr='g l lm ga lmn gaz'.split(' ')))