class Solution:
    def isBalancedParentheses(self, s: str) -> bool:
        stack = []
        d = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i in d.keys() and stack[-1] == d[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


solve = Solution()

s = '({})[]'

print(solve.isBalancedParentheses(s))



