class Solution:
    def maxProduct(self, nums):
        max_prod = float('-inf')
        prod = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                prod *= nums[i]
            else:
                max_prod = max(max_prod, prod)
                prod = 1
        return max(max_prod, prod)


solve = Solution()
#nums = [2, 3, -2, 4]
nums = [2, 3, 1, 4, 4]
print(solve.maxProduct(nums))
