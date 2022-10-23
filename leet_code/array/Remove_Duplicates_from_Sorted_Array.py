class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = Solution().removeDuplicates(arr)
print(k)
print(arr[:k])
