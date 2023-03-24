"""
https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
"""
class Solution:
    # User function Template for python3
    def findFloor(self, A, N, X):
        if A[-1] <= X:
            return N-1
        low = 0
        high = N-1

        while low <= high:
            mid = low + (high-low)//2
            if A[mid] == X or (A[mid] < X and (mid+1 < N and A[mid+1] > X)):
                return mid
            elif A[mid] > X:
                high = mid-1
            else:
                low = mid+1
        return -1

solve = Solution()
print(solve.findFloor(A=[1,2,8,10,11,12,19], N=7, X=5))
print(solve.findFloor(A=[1,2,8,10,11,12,19], N=7, X=0))