"""
https://workat.tech/problem-solving/practice/word-break

https://www.youtube.com/watch?v=Sx9NNgInc3A
"""
class Solution:
    def wordBreak(self, s: str, w) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for j in w:
                if len(j) <= len(s) and s[i:i+len(j)] == j:
                    dp[i] = dp[i+len(j)]
                if dp[i]:
                    break
        return dp[0]


solve = Solution()

string = "workattech"
words = ["tech", "work", "workat"]

print(solve.wordBreak(string, words))


