"""
https://leetcode.com/problems/reverse-words-in-a-string/
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i for i in s.split(' ')[::-1] if i]).strip()

solve = Solution()
print(solve.reverseWords(s='the sky is blue'))
print(solve.reverseWords(s='a good   example'))