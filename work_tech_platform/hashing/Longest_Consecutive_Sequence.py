"""
https://workat.tech/problem-solving/practice/longest-consecutive-sequence

https://leetcode.com/problems/longest-consecutive-sequence/
"""
class Solution:
    def longestConsecutiveSequence(self, A) -> int:
        if not A:
            return 0
        A.sort()
        long_strike = 1
        curr_strike = 1
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                if A[i] == A[i - 1] + 1:
                    curr_strike += 1
                else:
                    long_strike = max(long_strike, curr_strike)
                    curr_strike = 1
        return long_strike


class Solution2:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

solve = Solution()
arr = [24, 2, 34, 1, 3, 4, 3, -1, 28, 0]
print(solve.longestConsecutiveSequence(arr))


solve = Solution2()

arr = [24, 2, 34, 1, 3, 4, 3, -1, 28, 0]

print(solve.longestConsecutive(arr))