"""
https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
"""
class Solution:
    def arraySortedOrNot(self, arr, n):
        if n in [0, 1]:
            return True
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                return False
        return True

solve = Solution()
print(solve.arraySortedOrNot(arr=[10, 20, 30, 40, 50], n=5))