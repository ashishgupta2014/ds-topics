"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
"""
class Solution:
    def minAddToMakeValid(self, string: str) -> int:
        open = 0
        close = 0
        for s in string:
            if s == ')' and open:
                open -= 1
            elif s == '(':
                open += 1
            elif s == ')':
                close += 1

        return abs(open+close)

solve = Solution()
print(solve.minAddToMakeValid("())"))
print(solve.minAddToMakeValid("((("))
print(solve.minAddToMakeValid(")(()))("))
print(solve.minAddToMakeValid("()))(("))