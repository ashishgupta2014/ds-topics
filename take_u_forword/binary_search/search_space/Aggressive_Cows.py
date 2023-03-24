"""
https://practice.geeksforgeeks.org/problems/aggressive-cows/1

https://www.youtube.com/watch?v=wSOfYesTBRk&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=71
"""
class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        low = 1
        high = stalls[n-1] - stalls[0]
        res = 0
        while low <= high:
            mid = low + (high-low)//2
            if self.is_possible(mid, k, stalls):
                res = mid
                low = mid+1
            else:
                high = mid-1
        return res
    def is_possible(self, distance, k, stalls):
        p = 1
        i = 0
        k -= 1
        while p < len(stalls):
            if abs(stalls[i] - stalls[p]) >= distance:
                k -= 1
                i = p
                if k == 0:
                    return True
            p += 1
        return False


solve = Solution()
print(solve.solve(n=5, k=3, stalls=[1, 2, 4, 8, 9]))
print(solve.solve(n=5, k=3, stalls=[10, 1, 2, 7, 5]))