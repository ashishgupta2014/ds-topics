"""
https://leetcode.com/problems/remove-outermost-parentheses/description/
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        open = 0
        for i in s:
            is_added = False
            if i == '(':
                open += 1
            else:
                open -= 1
                if open > 0:
                    res += i
                    is_added = True
            if open > 1 and is_added == False:
                res += i
        return res


solve = Solution()
print(solve.removeOuterParentheses(s='(()())(())'))
print(solve.removeOuterParentheses(s='(()())(())(()(()))'))
print(solve.removeOuterParentheses(s='()()'))
print(solve.removeOuterParentheses(s='(((())))'))