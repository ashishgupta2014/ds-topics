"""
https://workat.tech/problem-solving/practice/letter-combinations-of-a-phone-number

https://www.youtube.com/watch?v=0snEunUacZY
"""
class Solution:

    mappings = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    res = []

    def backtracking(self, arr, cur, i):
        if len(arr) == len(cur):
            self.res.append(''.join(cur))
            return
        for sub in range(i, len(arr)):
            for k in range(0, len(arr[sub])):
                cur.append(arr[sub][k])
                self.backtracking(arr, cur, sub+1)
                cur.pop()

    def letterCombinations(self, digits: str):
        arr = []
        self.res = []
        for i in digits:
            arr.append(list(self.mappings[i]))
        self.backtracking(arr, [], 0)
        return self.res



solve = Solution()

d = '234'

print(solve.letterCombinations(digits=d))

d = '23'

print(solve.letterCombinations(digits=d))