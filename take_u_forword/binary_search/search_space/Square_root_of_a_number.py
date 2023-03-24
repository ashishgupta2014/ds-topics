"""
https://practice.geeksforgeeks.org/problems/square-root/0

https://www.youtube.com/watch?v=WjpswYrS2nY&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=63
"""
class Solution:
    def floorSqrt(self, x):
        low = 1
        high = x
        ans = None
        while low <= high:
            mid = low + (high-low)//2

            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid-1
            else:
                low = mid+1
                ans = mid
        return ans

solve = Solution()
print(solve.floorSqrt(x=5))