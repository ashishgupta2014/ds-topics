"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

https://www.youtube.com/watch?v=qtVh-XEpsJo&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=27
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_len = 0
        used = []
        while right < len(s):
            while s[right] in used:
                used.pop(0)
                left += 1
            used.append(s[right])
            max_len = max(max_len, right-left+1)
            right+= 1
        return max_len


solve = Solution()
print(solve.lengthOfLongestSubstring(s='abcabcbb'))
print(solve.lengthOfLongestSubstring(s='bbbbb'))
print(solve.lengthOfLongestSubstring(s='pwwkew'))