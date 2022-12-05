"""
https://leetcode.com/problems/search-insert-position/

https://workat.tech/problem-solving/practice/insert-position-in-sorted-array
"""
class Solution:
    def getInsertPosition(self, nums, target: int) -> int:
        low = 0
        high = len(nums)
        prev = 0
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                prev = low
            else:
                high = mid
                prev = high
        return prev


solve = Solution()

nums = [1, 3, 5, 6]
target = 5

print(solve.getInsertPosition(nums, target))
