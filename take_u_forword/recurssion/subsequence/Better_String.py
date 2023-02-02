"""
https://practice.geeksforgeeks.org/problems/better-string/1
"""
class Solution:

    def countSubsequence(self, strn):

        last = [-1] * 127
        N = len(strn)
        dp = [0] * (N + 1)

        dp[0] = 1

        for i in range(1, N + 1):

            # print("{} {}".format(dp[i-1], last[ord(strn[i-1])]))

            dp[i] = 2 * dp[i - 1]

            if last[ord(strn[i - 1])] != -1:
                dp[i] = dp[i] - dp[last[ord(strn[i - 1])]]

            last[ord(strn[i - 1])] = i - 1

        return dp[N]
    def betterString(self, str1, str2):
        if self.countSubsequence(str1) < self.countSubsequence(str2):
            return str2
        return str1

solve = Solution()
print(solve.betterString(str1='gfg', str2='ggg'))
print(solve.betterString(str1='a', str2='b'))
print(solve.betterString(str1='ggg', str2='fff'))