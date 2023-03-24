"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/

https://www.youtube.com/watch?v=NTop3VTjmxk&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=65
"""
class Solution:
    def findMedianSortedArrays(self,  nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            n1, n2 = n2, n1
            temp = nums1
            nums1 = nums2
            nums2 = temp
        low = 0
        high = n1

        while low <= high:
            cut1 = low + (high-low)//2
            cut2 = (n1+n2+1)//2 - cut1

            l1 = nums1[cut1-1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < n1 else float('inf')

            l2 = nums2[cut2-1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2] if cut2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1, l2)
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1


solve = Solution()
print(solve.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))