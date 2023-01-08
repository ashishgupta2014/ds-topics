"""
https://www.youtube.com/watch?v=-zI4mrF2Pb4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=27
"""
class Solution:
    def get_lcs_string(self, s1: str, s2: str) -> str:
        rows = len(s1)+1
        cols = len(s2)+1
        dp = [[0]*cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                if s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])

        result = ['']*dp[-1][-1]
        i = dp[-1][-1]
        row = rows-1
        col = cols-1
        while row > 0 and col > 0:
            if s1[row-1] == s2[col-1]:
                i -= 1
                result[i] = s1[row-1]
                row -= 1
                col -= 1
            else:
                if dp[row][col-1] > dp[row-1][col]:
                    col -= 1
                else:
                    row -= 1
        return ''.join(result)

solve = Solution()
print(solve.get_lcs_string(s1="workattech", s2="branch"))