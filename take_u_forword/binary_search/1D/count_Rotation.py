"""
https://practice.geeksforgeeks.org/problems/rotation4723/1
"""
class Solution:
    def findPivot(self, arr, n):
        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if mid < high and arr[mid] > arr[mid + 1]:
                return mid
            if mid > low and arr[mid - 1] > arr[mid]:
                return mid - 1
            if arr[low] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def findKRotation(self,arr,  n):
        pivot = self.findPivot(arr, n)
        return pivot + 1

solve = Solution()
print(solve.findKRotation(arr=[5, 1, 2, 3, 4], n=5))