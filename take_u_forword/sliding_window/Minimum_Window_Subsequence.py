"""
https://practice.geeksforgeeks.org/problems/minimum-window-subsequence/1
"""
class Solution:
    def minWindow(self, str1, str2):
        right = 0
        i = 0
        ans = float('inf'), None, None
        while right < len(str1):
            if str1[right] == str2[i]:
                i += 1
            if i == len(str2):
                i -= 1
                left = right
                while i >= 0:
                    if str1[left] == str2[i]:
                        i -= 1
                    left -= 1
                if right-left+1 < ans[0]:
                    ans = right-left+1, left+1, right+1
                i = 0
            right += 1
        return str1[ans[1]:ans[2]] if ans[1] is not None and ans[2] is not None else ''


solve = Solution()
print(solve.minWindow(str1='geeksforgeeks', str2='eksrg'))
print(solve.minWindow(str1='ierfwenhfa', str2='efna'))