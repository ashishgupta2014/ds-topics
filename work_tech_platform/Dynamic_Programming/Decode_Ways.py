"""
https://workat.tech/problem-solving/practice/decode-ways
https://leetcode.com/problems/decode-ways/description/

https://www.youtube.com/watch?v=6aEyTjOwlJU
"""
class Solution:
    dp = {}
    def dfs(self, st, i):

        if i in self.dp:
            return self.dp[i]

        if st[i] == '0':
            return 0

        res = self.dfs(st, i+1)

        if i+1 < len(st) and (st[i] == '1' or (st[i] == '2' and st[i+1] in "0123456")):
            res += self.dfs(st, i+2)
        self.dp[i] = res

        return res

    def tabuler(self, st):
        dp = {len(st): 1}
        for i in range(len(st)-1, -1, -1):
            if st[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i+1 < len(st) and (st[i] == '1' or (st[i] == '2' and st[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]
    def numDecodings(self, st: str) -> int:
        # self.dp = {len(st): 1}
        # return self.dfs(st, 0)
        return self.tabuler(st)



solve = Solution()
print(solve.numDecodings(st='123'))
# [1, 2, 3], [12, 3], [1, 23]
# [123]