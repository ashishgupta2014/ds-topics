"""
https://workat.tech/problem-solving/practice/longest-palindrome


https://leetcode.com/problems/longest-palindromic-substring/description/
"""
class Solution:
    res = ''
    def is_palindrome(self, s, left, right):
        while left < right and s[left]:
            if s[left] != s[right]:
                return False
            left+= 1
            right -=1
        return True

    def dfs(self, s, i):
        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                if len(self.res) < len(s[i:j+1]):
                    self.res = s[i:j+1]
                self.dfs(s, j+1)

    def getLongestPalindrome(self, s: str) -> str:
        # self.res = ''
        # self.dfs(s, 0)
        # return self.res
        res = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(res) >= j-i:
                    break
                if s[i:j] == s[i:j][::-1]:
                    if len(res) < len(s[i:j]):
                        res = s[i:j]
                        break
        return res


solve = Solution()
print(solve.getLongestPalindrome(s='abcdc'))
print(solve.getLongestPalindrome(s='mississippi'))


