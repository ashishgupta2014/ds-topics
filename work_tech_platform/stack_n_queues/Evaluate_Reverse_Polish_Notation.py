"""
https://workat.tech/problem-solving/practice/evaluate-reverse-polish-notation/editorial
"""


class Solution:
    def evalRPN(self, tokens) -> int:
        i = 0
        n = len(tokens)
        stack = []
        while i < n:
            if tokens[i] not in ['+', '*', '-', '/']:
                stack.append(tokens[i])
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop(-1))
                if tokens[i] == '+':
                    x = n1 + n2
                elif tokens[i] == '-':
                    x = n1 - n2
                elif tokens[i] == '*':
                    x = n1 * n2
                else:
                    x = n1 // n2
                stack.append(x)
            i += 1
        return stack[-1]


solve = Solution()
arr = ["6", "3", "+", "5", "/"]

arr1 = ["6", "-3", "+", "5", "-"]

arr2 = ["6", "3", "2", "+", "*", "5", "/"]
print(solve.evalRPN(arr))
