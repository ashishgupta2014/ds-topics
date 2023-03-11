"""
https://leetcode.com/problems/binary-subarrays-with-sum/description/


"""
import collections

class Solution:

    def prefix_sum(self, nums, goal):
        P = [0]
        for x in nums: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + goal] += 1

        return ans

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


    def numSubarraysWithSum(self, nums, goal):
        # return self.prefix_sum(nums, goal)
        return self.window(nums, goal)

solve = Solution()
print(solve.numSubarraysWithSum(nums=[1,0,1,0,1], goal=2))
print(solve.numSubarraysWithSum(nums=[0,0,0,0,0], goal=0))