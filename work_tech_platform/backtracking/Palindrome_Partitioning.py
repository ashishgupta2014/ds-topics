"""
https://workat.tech/problem-solving/practice/palindromic-partitioning

https://www.youtube.com/watch?v=3jvWodd7ht0
https://www.youtube.com/watch?v=WBgsABoClE0
"""
class Solution:
    res = []

    def is_palindrome(self, s, left, right):
        while left < right and s[left]:
            if s[left] != s[right]:
                return False
            left+= 1
            right -=1
        return True
    def backtrack(self, s, i, part):
        if i >= len(s):
            self.res.append(part[:])
            return
        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                part.append(s[i:j+1])
                self.backtrack(s, j+1, part)
                part.pop()

    def getPartitions(self, s: str):
        self.res = []
        self.backtrack(s, 0, [])
        return self.res


solve = Solution()

print(solve.getPartitions(s='aabc'))



