"""
https://leetcode.com/problems/repeated-string-match/description/

https://www.youtube.com/watch?v=66oFU0xtg_g
"""
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        s = a
        move = 1
        while len(a) < len(b):
            move += 1
            a += s
        if b in a:
            return move
        a += s
        move += 1
        if b in a:
            return move
        return -1


solve = Solution()
print(solve.repeatedStringMatch(a="abcd", b="cdabcdab"))
print(solve.repeatedStringMatch(a="a", b="aa"))