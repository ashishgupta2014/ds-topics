"""
https://leetcode.com/problems/shortest-common-supersequence/description/

https://www.youtube.com/watch?v=xElxAuBcvsU
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)+1
        m = len(str2)+1
        dp = [[0]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = n-1
        j = m-1
        ans = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                i -= 1
                j -= 1
                ans.append(str1[i])
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                    ans.append(str1[i])
                else:
                    j -= 1
                    ans.append(str2[j])
        while i > 0:
            i-=1
            ans.append(str1[i])
        while j > 0:
            j -= 1
            ans.append(str2[j])

        return ''.join(ans[::-1])



solve = Solution()
print(solve.shortestCommonSupersequence(str1='abac', str2='cab'))
print(solve.shortestCommonSupersequence(str1='brute', str2='groot'))