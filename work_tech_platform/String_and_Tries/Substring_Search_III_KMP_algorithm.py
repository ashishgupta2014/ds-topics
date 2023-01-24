"""
https://workat.tech/problem-solving/practice/substring-search-kmp

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

https://www.youtube.com/watch?v=JoF0Z7nVSrA
https://www.youtube.com/watch?v=V5-7GzOfADQ
https://github.com/neetcode-gh/leetcode/blob/main/python/0028-find-the-index-of-the-first-occurrence-in-a-string.py
"""
class Solution:
    def findStartIndexOfSubstring(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1

solve = Solution()
print(solve.findStartIndexOfSubstring(haystack="helloworld", needle="low"))
print(solve.findStartIndexOfSubstring(haystack="aaaaab", needle="aab"))
print(solve.findStartIndexOfSubstring(haystack="ccaccaaedba", needle="dba"))
print(solve.findStartIndexOfSubstring(haystack="a", needle="a"))