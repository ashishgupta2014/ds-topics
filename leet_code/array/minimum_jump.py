class Solution:
    def jump(self, nums) -> int:
        temp = 0
        end = 0
        ans = 0
        for i in range(len(nums) - 1):
            end = max(end, i + nums[i])
            if i == temp:
                temp = end
                ans += 1
        return ans

print(Solution().jump([2,3,1,1,4]))