"""
https://workat.tech/problem-solving/practice/string-permutations
https://leetcode.com/problems/permutations/

https://www.youtube.com/watch?v=YK78FU5Ffjw
https://www.youtube.com/watch?v=s7AvT7cGdSo
"""
# class Solution:
#     res = []
#
#     def backtracking(self, s, freq, cur):
#         if len(cur) == len(s):
#             self.res.append(''.join(cur))
#             return
#         for i in range(len(s)):
#             if not freq[i]:
#                 freq[i] = True
#                 cur.append(s[i])
#                 self.backtracking(s, freq, cur)
#                 freq[i] = False
#                 cur.pop()
#
#
#     def getAllPermutations(self, s: str):
#         self.res = []
#         freq = {i: False for i in range(len(s))}
#         self.backtracking(list(s), freq, [])
#         return self.res


class Solution:
    res = []

    def backtracking(self, s, left, right):
        if left == right:
            self.res.append(''.join(s))
            return
        for i in range(left, right):
            s[i], s[left] = s[left], s[i]
            self.backtracking(s, left+1, right)
            s[i], s[left] = s[left], s[i]

    def getAllPermutations(self, s: str):
        self.res = []
        self.backtracking(list(s), 0, len(s))
        return self.res

solve = Solution()
string = 'abc'
print(solve.getAllPermutations(string))


