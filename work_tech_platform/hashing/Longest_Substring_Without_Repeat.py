"""
https://workat.tech/problem-solving/practice/longest-substring-without-repeat

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

https://www.youtube.com/watch?v=wiGpQwVHdE0
"""

class Solution:
    def longestSubstringWithoutRepeat(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0
        for right, ele in enumerate(s):
            while ele in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(ele)
            res = max(res, right-left+1)
        return res

solve = Solution()

string = 'mississippi'

print(solve.longestSubstringWithoutRepeat(string))




