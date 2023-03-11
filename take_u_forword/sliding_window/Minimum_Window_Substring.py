"""
https://leetcode.com/problems/minimum-window-substring/description/
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        filtered_s = []
        for i, c in enumerate(s):
            if c in dict_t:
                filtered_s.append((i, c))

        left = right = 0
        window_dict = {}
        formed = 0
        required = len(dict_t)
        ans = float('inf'), None, None

        while right < len(filtered_s):
            chr = filtered_s[right][1]
            window_dict[chr] = 1 + window_dict.get(chr, 0)
            if window_dict[chr] == dict_t[chr]:
                formed += 1
            while left <= right and formed == required:
                chr = filtered_s[left][1]
                end = filtered_s[right][0]
                start = filtered_s[left][0]
                if (end - start +1) < ans[0]:
                    ans = end - start +1, start, end
                window_dict[chr] -= 1
                if window_dict[chr] < dict_t[chr]:
                    formed -= 1
                left += 1
            right += 1
        return  "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

solve = Solution()
print(solve.minWindow(s = "ADOBECODEBANC", t = "ABC"))