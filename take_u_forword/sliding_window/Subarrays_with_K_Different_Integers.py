"""
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

https://www.youtube.com/watch?v=utbQQr1U7bM

"""
from typing import List


class Solution:

    def at_most_k(self, nums, k):
        left = right = 0
        counter = {}
        ans = 0
        while right < len(nums):
            counter[nums[right]] = 1 + counter.get(nums[right], 0)

            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    counter.pop(nums[left])
                left += 1

            ans += right - left + 1
            right += 1
        return ans
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most_k(nums, k) - self.at_most_k(nums, k-1)


solve = Solution()
print(solve.subarraysWithKDistinct(nums=[1,2,1,2,3], k=2))