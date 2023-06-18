"""
https://practice.geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/1
"""
class Solution:
    def findMatching(self, text, pattern):
        if text[:len(pattern)] == pattern:
            return 0
        window = len(pattern)
        i = 1
        while i < len(text):
            if text[i:window+i] == pattern:
                return i
            i += 1
        return -1


solve = Solution()
print(solve.findMatching(text='gffgfg', pattern='gfg'))