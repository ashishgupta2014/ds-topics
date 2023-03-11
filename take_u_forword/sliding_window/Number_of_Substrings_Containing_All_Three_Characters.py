"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
"""
from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = count = 0
        d = Counter()
        n = len(s)
        while right < n:
            d[s[right]] += 1
            while len(d) == 3:
                count += len(s) - right
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            right += 1
        return count



solve = Solution()
print(solve.numberOfSubstrings(s='abcabc'))