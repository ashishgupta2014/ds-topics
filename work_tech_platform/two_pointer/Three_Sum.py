"""
https://leetcode.com/problems/3sum/
https://workat.tech/problem-solving/practice/three-sum
"""


class Solution:
    def threeSum(self, A):
        A.sort()  # [-2, -1, 0, 1, 1]
        n = len(A)
        result = []
        for i in range(n - 2):
            if i > 0 and A[i] == A[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = A[i] + A[left] + A[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([A[i], A[left], A[right]])
                    while left < right and A[left] == A[left + 1]:
                        left += 1
                    while left < right and A[right] == A[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


solve = Solution()
# arr = [1, 1, 0, -1, -2]
arr = [1, -1, 9, -8, 0]
print(solve.threeSum(arr))
