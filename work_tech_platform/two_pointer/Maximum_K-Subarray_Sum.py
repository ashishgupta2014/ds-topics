"""
https://workat.tech/problem-solving/practice/maximum-k-subarray-sum
"""


class Solution:
    def maxKSubarraySum(self, A, k: int) -> int:
        s = sum(A[:k])
        ans = s
        j = 0
        for i in range(k, len(A)):
            s -= A[j]
            s += A[i]
            j += 1
            ans = max(ans, s)
        return ans


solve = Solution()
Array = [3, 5, 6, 2, 4, 7, 8]
k = 3
print(solve.maxKSubarraySum(Array, k))
