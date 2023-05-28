"""
https://leetcode.com/problems/word-ladder-ii/description/

https://www.youtube.com/watch?v=DREutrv2XD0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32
"""
from typing import List


class Solution:


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        queue = [[beginWord]]
        usedOnLvl = []
        level = 0
        result = []
        while queue:
            words = queue.pop(0)
            if len(words) > level:
                level += 1
                for w in usedOnLvl:
                    if w in wordList:
                        wordList.remove(w)
                usedOnLvl = []
            last = words[-1]
            if last == endWord:
                if not result:
                    result.append(words)
                elif len(result[0]) == len(words):
                    result.append(words)
            arr = list(last)
            for i in range(len(last)):
                for ch in range(97, 123):
                    if chr(ch) != last[i]:
                        arr[i] = chr(ch)
                        temp = ''.join(arr)
                        if temp in wordList:
                            words.append(temp)
                            queue.append(words.copy())
                            words.pop()
                            usedOnLvl.append(last)
                    arr[i] = last[i]

        return result

solve = Solution()
print(solve.findLadders(beginWord="hit", endWord="cog", wordList=["hot","hiv", "dot","dog","lot","log","cat","cog"]))
print(solve.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))

# Optimized version of the problem

class Solution2:

    def dfs(self, shortest_path_rank, word, beginWord, result, carry):
        if beginWord == word:
            a = carry[:]
            a.append(beginWord)
            result.append(a[::-1])
            return
        steps = shortest_path_rank[word]
        arr = list(word)
        for i in range(len(word)):
            for ch in range(97, 123):
                if chr(ch) != word[i]:
                    arr[i] = chr(ch)
                    temp = ''.join(arr)
                    if temp in shortest_path_rank and shortest_path_rank[temp]+1 == steps:
                        carry.append(word)
                        self.dfs(shortest_path_rank, temp, beginWord, result, carry)
                        carry.pop()
            arr[i] = word[i]


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        queue = [(beginWord, 0)]
        shortest_path_rank = {beginWord: 0}
        while queue:
            word, seq = queue.pop(0)
            if word == endWord:
                break
            arr = list(word)
            for i in range(len(word)):
                for ch in range(97, 123):
                    if chr(ch) != word[i]:
                        arr[i] = chr(ch)
                        temp = ''.join(arr)
                        if temp in wordList:
                            seq += 1
                            queue.append((temp, seq))
                            shortest_path_rank[temp] = seq
                            wordList.remove(temp)
                arr[i] = word[i]
        result = []
        self.dfs(shortest_path_rank, endWord, beginWord, result, [])
        return result

solve = Solution2()
print(solve.findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot","dog","lot","log","cog"]))
print(solve.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))