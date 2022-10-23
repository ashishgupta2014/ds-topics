class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        distance = float('inf')
        nums.sort()

        for a in range(len(nums) - 2):
            new_target = target - nums[a]
            left, right = a + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if abs(distance) > abs(new_target - two_sum):
                    distance = new_target - two_sum

                if two_sum == new_target:
                    return target
                elif two_sum < new_target:
                    left += 1
                else:
                    right -= 1
        return target-distance


solve = Solution()
# nums = [-1, 2, 1, -4]
# target = 1

nums = [0, 1, 2]
target = 0

print(solve.threeSumClosest(nums, target))
