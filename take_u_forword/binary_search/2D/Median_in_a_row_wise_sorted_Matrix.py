"""
https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1

https://www.youtube.com/watch?v=63fPPOdIr2c&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=63
"""
class Solution:

    def count_smaller_numbers(self, arr, target):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] <= target:
                low = mid+1
            else:
                high = mid-1
        return low

    def median(self, matrix, R, C):
        low = 0
        high = 1e9

        while low <= high:
            mid = low + (high-low)//2
            count = 0
            for r in range(R):
                count += self.count_smaller_numbers(arr=matrix[r], target=mid)
            if count <= (R*C)//2:
                low = mid+1
            else:
                high = mid-1
        return int(low)

solve = Solution()
print(solve.median(matrix=[[1, 3, 5], [2, 6, 9], [3, 6, 9]], R=3, C=3))