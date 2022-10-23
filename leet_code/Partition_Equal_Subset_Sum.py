class Solution:
    def canPartition(self, nums):
        target = sum(nums) // 2

        def helper(i, s):
            if target == s:
                return True
            elif target < s:
                return False
            for i in range(i, len(nums)):
                helper(i + 1, nums[i] + s)
            return False
        return helper(0, 0)


solve = Solution()
nums = [1, 5, 11, 5]
print(solve.canPartition(nums))
