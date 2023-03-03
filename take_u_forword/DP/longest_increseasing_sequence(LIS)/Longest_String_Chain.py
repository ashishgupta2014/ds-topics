"""
https://leetcode.com/problems/longest-string-chain/description/

https://takeuforward.org/data-structure/longest-string-chain-dp-45/

https://www.youtube.com/watch?v=YY8iBaYcc4g
"""
from typing import List


class Solution:

    def is_chain(self, str1, str2):
        if len(str1)+1 != len(str2):
            return False
        first = 0
        second = 0
        while second < len(str2):
            if first < len(str1) and str1[first] == str2[second]:
                first += 1
                second += 1
            else:
                second += 1
        if first == len(str1) and second == len(str2):
            return True
        return False

    def dfs(self, words, i, prev):
        if i >= len(words):
            return 0
        not_take = self.dfs(words, i+1, prev)
        take = 0
        if prev == -1 or self.is_chain(str1=words[prev], str2=words[i]):
            take = 1 + self.dfs(words, i+1, i)
        return max(not_take, take)

    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words,key=lambda x:len(x))
        # return self.dfs(words, 0, -1)
        n = len(words)
        dp = [1]*n
        for i in range(n):
            for prev in range(i+1):
                if self.is_chain(str1=words[prev], str2=words[i]):
                    dp[i] = max(dp[i], 1+dp[prev])
        return max(dp)

solve = Solution()
print(solve.longestStrChain(words=["a","b","ba","bca","bda","bdca"]))
print(solve.longestStrChain(words=["xbc","pcxbcf","xb","cxbc","pcxbc"]))