"""
https://workat.tech/problem-solving/practice/power-set

https://www.geeksforgeeks.org/power-set/
"""
class Solution:

    def gen(self, nums, result, temp, n):
        result.append(temp.copy())
        if n >= len(nums):
            return
        for i in range(n, len(nums)):
            temp.append(nums[i])
            self.gen(nums, result, temp, i+1)
            temp.pop()

    def getPowerSet(self, nums):
        result = []
        self.gen(nums, result, [], 0)
        return result


solve = Solution()

print(solve.getPowerSet(nums=[1, 2, 3]))


