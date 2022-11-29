""""
https://leetcode.com/problems/wiggle-subsequence/

https://www.youtube.com/watch?v=IpWoZvKzpug
"""


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        pos = 1
        neg = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                pos = neg + 1
            elif nums[i] < nums[i - 1]:
                neg = pos + 1
        return max(pos, neg)


nums = [1, 7, 4, 9, 2, 5]
solve = Solution()
print(solve.wiggleMaxLength(nums))
