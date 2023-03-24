"""
https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

https://www.youtube.com/watch?v=WjpswYrS2nY&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=63
"""
class Solution:
    def NthRoot(self, n, m):
        low = 1
        high = m
        while low <= high:
            mid = low + (high - low) // 2
            val = pow(mid, n)
            if val == m:
                return mid
            elif val > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1

solve = Solution()
print(solve.NthRoot(n=2, m=9))
print(solve.NthRoot(n=3, m=27))
print(solve.NthRoot(n=2, m=27))