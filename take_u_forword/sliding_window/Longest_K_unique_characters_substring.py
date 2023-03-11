"""
https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""

class Solution:

    def longestKSubstr(self, s, k):

        left = right = 0
        counter = {}
        ans = -1
        while right < len(s):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    counter.pop(s[left])
                left += 1
            if len(counter) == k:
                ans = max(ans, right-left+1)
            right += 1
        return ans


solve = Solution()
print(solve.longestKSubstr(s='aabacbebebe', k=3))