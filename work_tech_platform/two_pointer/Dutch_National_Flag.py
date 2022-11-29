class Solution:
    def sortTheArray(self, A) -> None:
        low = mid = 0
        high = len(A) - 1

        while mid <= high:
            if A[mid] == 0:
                A[low], A[mid] = A[mid], A[low]
                low += 1
                mid += 1
            elif A[mid] == 1:
                mid += 1
            else:
                A[mid], A[high] = A[high], A[mid]
                high -= 1

solve = Solution()

A = [2, 2, 0, 1]
solve.sortTheArray(A)
print(A)

