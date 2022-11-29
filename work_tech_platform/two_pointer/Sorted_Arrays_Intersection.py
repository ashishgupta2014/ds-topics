"""
https://workat.tech/problem-solving/practice/sorted-arrays-intersection
"""


class Solution:
    def intersection(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            return self.intersection(B, A)
        i = 0
        j = 0
        res = []
        while i < m and j < n:

            if A[i] > B[j]:
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                res.append(A[i])
                i += 1
                j += 1
        return res


solve = Solution()

arr1 = [1, 3, 4, 5, 5, 6, 6, 7]
arr2 = [2, 5, 6, 6, 7, 8]
print(solve.intersection(arr1, arr2))
