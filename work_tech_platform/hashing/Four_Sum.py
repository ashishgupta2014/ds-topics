"""
https://workat.tech/problem-solving/practice/four-sum
https://leetcode.com/problems/4sum/
"""
class Solution:

    def kSum(self, nums, target: int, k: int):
        res = []
        # If we have run out of numbers to add, return res.
        if not nums:
            return res

        # There are k remaining values to add to the sum. The
        # average of these values is at least target // k.
        average_value = target // k

        # We cannot obtain a sum of target if the smallest value
        # in nums is greater than target // k or if the largest
        # value in nums is smaller than target // k.
        if average_value < nums[0] or nums[-1] < average_value:
            return res

        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res

    def twoSum(self, nums, target: int):
        res = []
        low, high = 0, len(nums) - 1

        while low < high:
            curr_sum = nums[low] + nums[high]
            if curr_sum < target or (low > 0 and nums[low] == nums[low- 1]):
                low += 1
            elif curr_sum > target or (high < len(nums) - 1 and nums[high] == nums[high + 1]):
                high -= 1
            else:
                res.append([nums[low], nums[high]])
                low += 1
                high -= 1

        return res
    def fourSum(self, nums, target: int):

        nums.sort()
        return self.kSum(nums, target, 4)


solve = Solution()

nums = [2,2,2,2,2]
target = 8

print(solve.fourSum(nums, target))