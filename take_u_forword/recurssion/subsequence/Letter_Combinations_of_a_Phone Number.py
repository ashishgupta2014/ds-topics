"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
from typing import List


class Solution:

    phone = {'1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

    def dfs(self, arr, i, temp, result):
        if len(arr) == len(temp):
            result.append(''.join(temp))
            return
        for sub in range(i, len(arr)):
            for j in range(0, len(arr[sub])):
                temp.append(arr[sub][j])
                self.dfs(arr, sub+1, temp, result)
                temp.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        arr = []
        for i in digits:
            arr.append(list(self.phone[i]))
        result = []
        if arr:
            self.dfs(arr, 0, [], result)
        return result


solve = Solution()
print(solve.letterCombinations(digits='23'))
print(solve.letterCombinations(digits='234'))
print(solve.letterCombinations(digits=''))