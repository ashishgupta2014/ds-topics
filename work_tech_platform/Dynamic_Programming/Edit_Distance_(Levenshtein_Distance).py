"""
https://workat.tech/problem-solving/practice/edit-distance

https://www.youtube.com/watch?v=fJaKO8FbDdo
"""
class Solution:
    dp = []
    def backtracking(self, s1, s2, i, j):
        if i < 0:
            return j+1
        if j < 0:
            return i+1

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if s1[i] == s2[j]:
            self.dp[i][j] = 0+self.backtracking(s1, s2, i-1, j-1) # no op
            return self.dp[i][j]
        if s1[i] != s2[j]:
            self.dp[i][j] = 1+ min(self.backtracking(s1, s2, i, j-1), # insert op
                       self.backtracking(s1, s2, i-1, j), # delete op
                       self.backtracking(s1, s2, i-1, j-1) # replace op
                       )
            return self.dp[i][j]
    def minOperations(self, s1: str, s2: str) -> int:
        # self.dp = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
        # return self.backtracking(s1, s2, len(s1)-1, len(s2)-1)
        rows = len(s1) + 1
        cols = len(s2)+1
        self.dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0:
                    self.dp[row][col] = col
                elif col == 0:
                    self.dp[row][col] = row
                elif s1[row-1] != s2[col-1]:
                    self.dp[row][col] = 1+min(self.dp[row][col-1],
                                              self.dp[row-1][col],
                                              self.dp[row-1][col-1])
                else:
                    self.dp[row][col] = self.dp[row-1][col-1]
        return self.dp[-1][-1]


solve = Solution()
print(solve.minOperations(s1="hello", s2="seldom"))
print(solve.minOperations(s1="horse", s2="ros"))