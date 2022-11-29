class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        arr = list('0123456')
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if 0 <= i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in arr)):
                dp[i] += dp[i + 2]
        return dp[0]


solve = Solution()
num = '226'
print(solve.numDecodings(num))
