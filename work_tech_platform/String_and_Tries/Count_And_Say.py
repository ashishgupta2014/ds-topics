"""
https://workat.tech/problem-solving/practice/count-and-say

https://leetcode.com/problems/count-and-say/

https://www.youtube.com/watch?v=usAZEcL_y-0
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = "1"
        for i in range(2, n + 1):
            s += '$'
            l = len(s)
            cnt = 1
            tmp = ""
            for j in range(1 , l):
                if s[j] != s[j - 1]:
                    tmp += str(cnt + 0)
                    tmp += s[j - 1]
                    cnt = 1
                else:
                    cnt += 1
            s = tmp
        return s

solve = Solution()

print(solve.countAndSay(n=1))
print(solve.countAndSay(n=2))
print(solve.countAndSay(n=3))
print(solve.countAndSay(n=4))
print(solve.countAndSay(n=5))
print(solve.countAndSay(n=6))



