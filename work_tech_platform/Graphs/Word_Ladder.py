"""
https://workat.tech/problem-solving/practice/word-ladder

https://www.youtube.com/watch?v=tRPda0rcf8E
"""

from typing import List


class Solution:
    def shortestLadderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [(beginWord, 1)]
        wordList = set(wordList)
        while queue:
            word, seq = queue.pop(0)
            arr = list(word)
            for i in range(len(word)):
                for ch in range(97, 123):
                    if chr(ch) != word[i]:
                        arr[i] = chr(ch)
                        temp = ''.join(arr)
                        if temp == endWord:
                            return seq+1
                        if temp in wordList:
                            queue.append((temp, seq+1))
                            wordList.remove(temp)
                arr[i] = word[i]
        return 0





solve = Solution()
print(solve.shortestLadderLength(beginWord='work', endWord='tech', wordList=["toch","worh","wock","woch","tech","werh"]))



