"""
https://workat.tech/problem-solving/practice/consecutively-descending-integers
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

https://www.youtube.com/watch?v=eDtMmysldaw
"""
class Solution:

    def backtrack(self, S, index, prev):
        if index == len(S):
            return True
        for j in range(index, len(S)):
            val = int(S[index:j+1])
            if val+1 == prev and self.backtrack(S, j+1, val):
                return True
        return False

    def isConsecutivelyDescending(self, s: str) -> bool:
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if self.backtrack(s, i+1, val):
                return True
        return False

solve =  Solution()

print(solve.isConsecutivelyDescending(s='54321'))

print(solve.isConsecutivelyDescending(s='10099989796'))

print(solve.isConsecutivelyDescending(s='54320'))


