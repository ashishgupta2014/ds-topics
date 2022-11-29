"""
https://workat.tech/problem-solving/practice/sliding-window-maximum
"""
class Solution:
    def maxSlidingWindow(self, A, k: int):
        maxNum = max(A[:k])
        result = [maxNum]
        for i in range(1, len(A)-k+1):
            end_window = i + k - 1
            if maxNum < A[end_window]:
                maxNum = A[end_window]
                result.append(maxNum)
            elif maxNum > A[end_window] and maxNum != A[i - 1]:
                result.append(maxNum)
            else:
                maxNum = max(A[i:end_window + 1])
                result.append(maxNum)
        return result


solve = Solution()
A = [1, -2, 3, 4, 5, 3, 4, -1]
k = 3
print(solve.maxSlidingWindow(A, k))