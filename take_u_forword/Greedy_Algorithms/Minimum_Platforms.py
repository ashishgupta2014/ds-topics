"""
https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

https://www.youtube.com/watch?v=dxVcMDI7vyI&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=46
"""
class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n, arr, dep):
        arr.sort()
        dep.sort()
        platform_needed = max_platform = 1
        d = 0
        a = 1
        while a < n and d < n:
            if arr[a] <= dep[d]:
                platform_needed += 1
                max_platform = max(max_platform, platform_needed)
                a += 1
            else:
                platform_needed -= 1
                d += 1
        return max_platform



solve = Solution()
print(solve.minimumPlatform(n=6, arr=[900, 940, 950, 1100, 1500, 1800], dep=[910, 1200, 1120, 1130, 1900, 2000]))