"""
https://workat.tech/problem-solving/practice/longest-palindromic-substring

space optimized with two pointer https://www.youtube.com/watch?v=XYQecbcd6_c
dp problem https://www.youtube.com/watch?v=UflHuQj6MVA
https://www.geeksforgeeks.org/longest-palindromic-substring-using-dynamic-programming/
"""
class Solution:
    def lps(self, s: str) -> str:
        n = len(s)
        res = ""
        res_len = 0
        for i in range(n):
            # odd length string
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right-left+1 > res_len:
                    res = s[left:right+1]
                    res_len = right-left+1
                left -= 1
                right += 1
            # even length string
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                if right-left+1 > res_len:
                    res = s[left:right+1]
                    res_len = right-left+1
                left -= 1
                right += 1
        return res


solve = Solution()
cases = ["cbbd", "abcdcab", "abcdcba", "abcd", "abaadcd", "workattech"]
for case in cases:
    print(solve.lps(s=case))


