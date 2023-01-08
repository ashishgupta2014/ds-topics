"""
https://workat.tech/problem-solving/practice/regular-expression-matching
https://leetcode.com/problems/regular-expression-matching/submissions/873141586/

https://www.youtube.com/watch?v=HAA8mgxlov8
"""
class Solution:
    dp = {}
    def dfs(self, s, p, i, j):
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        if (j + 1) < len(p) and p[j + 1] == "*":
            self.dp[(i, j)] = self.dfs(s, p, i, j + 2) or (  # dont use *
                    match and self.dfs(s, p, i + 1, j)
            )  # use *
            return self.dp[(i, j)]
        if match:
            self.dp[(i, j)] = self.dfs(s, p, i + 1, j + 1)
            return self.dp[(i, j)]
        self.dp[(i, j)] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        # self.dp = {}
        # return self.dfs(s, p, 0, 0)
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]


solve = Solution()
print(solve.isMatch(s='aa', p='a*'))

print(solve.isMatch(s='abcdf', p='a*b.*'))

print(solve.isMatch(s='abcdf', p='a*bd*'))

print(solve.isMatch(s='ab', p='.*ab'))

print(solve.isMatch(s='ab', p='.*c'))

print(solve.isMatch(s='mississippi', p='mis*is*ip*.'))