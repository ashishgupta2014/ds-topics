"""
https://leetcode.com/problems/compare-version-numbers/description/

https://workat.tech/problem-solving/practice/compare-version-numbers

"""
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue

            return -1 if rev1 < rev2 else 1

        return 0

solve = Solution()
print(solve.compareVersion(version1='1.01', version2='1.001'))
print(solve.compareVersion(version1='7.5.2.4', version2='7.5.3'))