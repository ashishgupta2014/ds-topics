"""
https://leetcode.com/problems/longest-palindromic-substring/
https://www.youtube.com/watch?v=XYQecbcd6_c
"""


class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]


solve = Solution()
s = "babad"
print(solve.longestPalindrome(s))
