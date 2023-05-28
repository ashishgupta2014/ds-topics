"""
https://leetcode.com/problems/word-ladder/

https://takeuforward.org/graph/word-ladder-i-g-29/
"""
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = [(beginWord, 1)]

        while queue:
            word, seq = queue.pop(0)
            arr = list(word)
            for i in range(len(word)):
                for ch in range(97, 123):
                    if chr(ch) != word[i]:
                        arr[i] = chr(ch)
                        temp = ''.join(arr)
                        if temp == endWord:
                            return seq + 1
                        if temp in wordList:
                            queue.append((temp, seq + 1))
                            wordList.remove(temp)
                arr[i] = word[i]
        return 0



solve = Solution()
#print(solve.ladderLength(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"]))
print(solve.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))