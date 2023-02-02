"""
https://leetcode.com/problems/generate-parentheses/description/


"""
from typing import List


class Solution:

    def dfs(self, n, open, closed, temp, result):
        if n <= 0 and open == closed:
            result.append(''.join(temp))
            return
        if n > 0:
            temp.append('(')
            self.dfs(n-1, open+1, closed, temp, result)
            temp.pop()

        if open > closed:
            temp.append(')')
            self.dfs(n, open, closed+1, temp, result)
            temp.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, 0, 0, [], result)
        return result

solve = Solution()
print(solve.generateParenthesis(n=3))