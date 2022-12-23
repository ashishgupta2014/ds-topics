"""
https://workat.tech/problem-solving/practice/distinct-numbers-window
"""
class Solution:
    def distinctNumbersInWindow(self, A, k: int):
        temp = {}
        for i in range(k):
            temp[A[i]] = temp.get(A[i], 0) + 1
        res = [len(temp)]
        j = 0

        for i in range(k, len(A)):
            if temp[A[j]] > 1:
                temp[A[j]] -= 1
            else:
                del temp[A[j]]
            j += 1
            temp[A[i]] = temp.get(A[i], 0) + 1
            res.append(len(temp))
        return res






solve = Solution()
A = [1, 1, 2, 1, 4, 6, 5]
k = 3
print(solve.distinctNumbersInWindow(A, k))

A = [1, 1, 2, 1, 1]
k = 2
print(solve.distinctNumbersInWindow(A, k))