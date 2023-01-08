"""
https://workat.tech/problem-solving/practice/word-break-ii

"""
from typing import List


class Solution:
    res = []
    def dfs(self, s, w, i, temp):
        if i >= len(s):
            self.res.append(' '.join(temp))
            return
        for j in range(i, len(s)):
            if s[i:j+1] in w:
                temp.append(s[i:j+1])
                self.dfs(s, w, j+1, temp)
                temp.pop()


    def wordBreak(self, s: str, w: List[str]) -> List[str]:
        self.res = []
        self.dfs(s, w, 0, [])
        return self.res


solve = Solution()
print(solve.wordBreak(s="workattech", w=["tech", "work", "problem", "at", "workattech"]))

print(solve.wordBreak(s="roundandround", w=["and", "round", "roundand"]))



