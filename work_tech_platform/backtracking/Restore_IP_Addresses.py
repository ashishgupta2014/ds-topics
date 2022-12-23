"""
https://workat.tech/problem-solving/practice/restore-ip-addresses

https://www.youtube.com/watch?v=61tN4YEdiTM
"""
class Solution:
    res = []

    def backtrack(self, s, i, dots, cur):
        if dots == 4 and i == len(s):
            self.res.append(cur[:-1])
            return
        if dots > 4:
            return
        for j in range(i, min(i+3, len(s))):
            if int(s[i:j+1]) < 256 and (i==j or s[i] != '0'):
                self.backtrack(s, j+1, dots+1, cur+s[i:j+1]+'.')

    def restoreIPAddresses(self, s: str):
        self.res = []
        if len(s) > 12:
            return self.res
        self.backtrack(s, 0, 0, '')
        return self.res

solve = Solution()

string = "25525511135"

print(solve.restoreIPAddresses(string))


