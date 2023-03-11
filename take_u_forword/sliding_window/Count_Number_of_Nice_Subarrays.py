"""
https://leetcode.com/problems/count-number-of-nice-subarrays/description/
"""
from collections import defaultdict
from typing import List


class Solution:

    def prefix_sum(self, nums, k):
        count = prefix_sum = 0
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            prefix_sum += i
            if prefix_sum-k in d:
                count += d[prefix_sum-k]
            d[prefix_sum] += 1
        return count

    def window(self, nums, goal):
        left = right = middle = left_sum = right_sum = ans = 0

        while right < len(nums):
            left_sum += nums[right]
            while left < right and left_sum > goal:
                left_sum -= nums[left]
                left += 1

            right_sum += nums[right]
            while middle < right and (right_sum > goal or (right_sum == goal and not nums[middle])):
                right_sum -= nums[middle]
                middle += 1
            if left_sum == goal:
                ans += middle - left + 1
            right += 1
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [0 if n % 2 == 0 else 1 for n in nums]
        # return self.prefix_sum(nums, k)
        return self.window(nums, k)

solve = Solution()
print(solve.numberOfSubarrays(nums=[1,1,2,1,1], k=3))