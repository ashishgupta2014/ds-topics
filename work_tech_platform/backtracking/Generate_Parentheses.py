"""
https://workat.tech/problem-solving/practice/generate-parentheses

https://www.youtube.com/watch?v=s9fokUqJ76A
"""
class Solution:
    res = []
    def backtracking(self, n, open, close, cur):
        if open == n and close == n:
            self.res.append(''.join(cur))
            return
        if n > open:
            cur.append('(')
            self.backtracking(n, open+1, close, cur)
            cur.pop()
        if open > close:
            cur.append(')')
            self.backtracking(n, open, close+1, cur)
            cur.pop()


    def generateParentheses(self, n: int):
        self.res = []
        self.backtracking(n, 0, 0, [])
        return self.res


solve = Solution()

print(solve.generateParentheses(n=2))

print(solve.generateParentheses(n=3))


