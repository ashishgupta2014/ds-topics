"""
https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

https://www.youtube.com/watch?v=nv7F4PiLUzo&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=67
"""
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n < m:
            n, m = m, n
            arr1, arr2 = arr2, arr1
        low = max(0, k-m)
        high = min(k, n)

        while low <= high:
            mid1 = low + (high-low)//2
            mid2 = k - mid1
            l1 = float('-inf') if mid1 == 0 else arr1[mid1-1]
            l2 = float('-inf') if mid2 == 0 else arr2[mid2-1]
            r1 = float('inf') if mid1 == n else arr1[mid1]
            r2 = float('inf') if mid2 == m else arr2[mid2]
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = mid1-1
            else:
                low = mid1+1


solve = Solution()
print(solve.kthElement(arr1=[2, 3, 6, 7, 9], arr2=[1, 4, 8, 10], n=5, m=4, k=5))