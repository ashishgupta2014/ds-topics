"""
https://practice.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1

https://www.youtube.com/watch?v=-zI4mrF2Pb4
"""
class Solution:

    def tabular(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        result = []
        se = set()
        self.process(text1, text2, 0, 0, [], result, dp[-1][-1], se)
        result.sort()
        return result

    def process(self,s,t,i,j,temp,ans,count,se):
        temp1=''.join(temp)
        if count==0:
            if temp1 not in se:
                se.add(temp1)
                ans.append(temp1)
            return
        if i>=len(s) or j>=len(t):
            return
        for r in range(i,len(s)):
            for c in range(j,len(t)):
                if s[r]==t[c]:
                    temp.append(s[r])
                    self.process(s,t,r+1,c+1,temp,ans,count-1,se)
                    temp.pop()

    def all_longest_common_subsequences(self, s, t):
        return self.tabular(text1=s, text2=t)

solve = Solution()
print(solve.all_longest_common_subsequences(s='abaaa', t='baabaca'))