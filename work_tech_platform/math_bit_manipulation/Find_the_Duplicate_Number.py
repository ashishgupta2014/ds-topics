"""
https://workat.tech/problem-solving/practice/find-the-duplicate-number
https://leetcode.com/problems/find-the-duplicate-number/

https://www.youtube.com/watch?v=32Ll35mhWg0
https://www.youtube.com/watch?v=wjYnzkAhcNk
"""
class Solution:
    def findTheDuplicateNumber(self, nums) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                break
        return slow

solve = Solution()
arr = [3, 1, 2, 4, 2]

print(solve.findTheDuplicateNumber(arr))


arr = [3, 1, 3, 2]
print(solve.findTheDuplicateNumber(arr))

arr = [3, 2, 1, 2]
print(solve.findTheDuplicateNumber(arr))
