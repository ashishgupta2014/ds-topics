"""
https://workat.tech/problem-solving/practice/integer-to-roman/editorial

https://leetcode.com/problems/integer-to-roman/submissions/372844304/
"""
class Solution:
    def integerToRoman(self, num: int) -> str:
        d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        s = ''
        quotient = num
        m = 1
        n = 5
        while quotient:
            quotient, r = divmod(quotient, 10)
            if 0 < r < 4:
                s = r*d[m]+s
            elif r == 4:
                s = d[m]+d[n]+s
            elif r == 5:
                s = d[n]+s
            elif 5 < r < 9:
                s = d[n]+(r-5)*d[m]+s
            elif r == 9:
                s = d[m]+d[m*10]+s
            m, n = 10*m, 10*n
        return s
solve = Solution()
print(solve.integerToRoman(num=123))