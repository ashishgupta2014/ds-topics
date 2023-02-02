"""
https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/

https://leetcode.com/problems/string-to-integer-atoi/description/
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        return q1(s, sp=0, val=0, sign=1)


def q1(s: str, sp: int, val: int, sign: int):
    if sp >= len(s):
        return q3(val, sign)
    if s[sp] == " ":
        return q1(s, sp + 1, val, sign)
    if s[sp] == "+":
        return q2(s, sp + 1, val, 1)
    if s[sp] == "-":
        return q2(s, sp + 1, val, -1)
    if s[sp].isdecimal():
        return q2(s, sp + 1, val * 10 + int(s[sp]), sign)
    return q3(val, sign)


def q2(s: str, sp: int, val: int, sign: int):
    if sp >= len(s):
        return q3(val, sign)
    if s[sp].isdecimal():
        return q2(s, sp + 1, val * 10 + int(s[sp]), sign)
    return q3(val, sign)


def q3(val: int, sign: int):
    val = sign * val
    bound = 2**31
    if val < -bound:
        return -bound
    if val >= bound:
        return bound - 1
    return val

solve = Solution()
print(solve.myAtoi(s='42'))