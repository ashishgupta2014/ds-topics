class Solution:
    def rob(self, nums) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    def rob_rec(self, nums) -> int:
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        memo = {}
        return dfs(0)


solve = Solution()
nums = [0, 0, 9, 3, 1, 0, 1, 8, 2, 0, 1]
print(solve.rob(nums))
print(solve.rob_rec(nums))
