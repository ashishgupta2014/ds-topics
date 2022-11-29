"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
https://workat.tech/problem-solving/practice/k-diff-pairs
"""
from collections import Counter


class Solution:
    def kDiffPairs(self, A, k: int) -> int:
        res = 0
        freq = Counter(A)
        for num in freq:
            condition1 = (k == 0 and freq[num] > 1)
            condition2 = (k > 0 and (num + k in freq))
            if condition1 or condition2:
                res += 1
        return res


solve = Solution()
arr = [1, 3, 5, 7, 10]
k = 2
print(solve.kDiffPairs(arr, k))
