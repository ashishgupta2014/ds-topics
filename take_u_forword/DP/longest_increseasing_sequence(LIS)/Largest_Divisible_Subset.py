"""
https://leetcode.com/problems/largest-divisible-subset/description/

https://takeuforward.org/data-structure/longest-divisible-subset-dp-44/

https://www.youtube.com/watch?v=gDuZwBW9VvM
"""
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        dp = [1]*n
        arr = [0]*n
        last_index = -1
        ans = -1

        for i in range(n):
            arr[i] = i
            for j in range(i+1):
                if i != j and nums[i] % nums[j] == 0 and dp[i] < 1+dp[j]:
                    dp[i] = 1+dp[j]
                    arr[i] = j
            if dp[i] > ans:
                ans = dp[i]
                last_index = i


        result = [nums[last_index]]
        while arr[last_index] != last_index:
            last_index = arr[last_index]
            result.append(nums[last_index])
        return result[::-1]


solve = Solution()
print(solve.largestDivisibleSubset(nums=[1,2,3]))
print(solve.largestDivisibleSubset(nums=[1,16,7,8,4]))