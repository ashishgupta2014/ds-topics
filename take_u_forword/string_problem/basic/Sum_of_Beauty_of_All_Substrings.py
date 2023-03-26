"""
https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/

https://www.youtube.com/watch?v=5XjJs5SBN8g
"""
from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            freq = defaultdict(int)
            freq[ch] += 1
            for j in range(i + 1, len(s)):
                freq[s[j]] += 1
                if len(freq) > 1:
                    total += max(freq.values()) - min(freq.values())
        return total


solve = Solution()
print(solve.beautySum(s='aabcbaa'))