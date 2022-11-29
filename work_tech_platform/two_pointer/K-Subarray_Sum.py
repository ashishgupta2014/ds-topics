class Solution:
    def kSubarraySum(self, A, k: int):
        result = [sum([A[i] for i in range(k)])]
        j = 0
        for i in range(k, len(A)):
            s = result[-1]
            s -= A[j]
            s += A[i]
            j += 1
            result.append(s)
        return result


solve = Solution()
arr = [3, 5, 6, 2, 4, 7, 8]
k = 3
# [14, 13, 12, 13, 19]
print(solve.kSubarraySum(arr, k))
