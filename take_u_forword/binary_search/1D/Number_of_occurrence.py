"""
https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1
"""
class Solution:

    def findFirst(self, arr, tar):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == tar:
                if mid - 1 >= 0 and arr[mid - 1] != tar or mid == 0:
                    return mid
                right = mid - 1
            elif arr[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    def findLast(self, arr, tar):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == tar:
                if mid + 1 < len(arr) and arr[mid + 1] != tar or mid == len(arr) - 1:
                    return mid
                left = mid + 1
            elif arr[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    def count(self,arr, n, x):

        first = self.findFirst(arr, x)
        last = self.findLast(arr, x)
        if first != -1 and last != -1:
            return last - first + 1
        elif first != -1 or last != -1:
            return 1
        return 0
solve = Solution()
print(solve.count(arr=[1, 1, 2, 2, 2, 2, 3], n=7, x=2))
print(solve.count(arr=[1, 1, 2, 2, 2, 2, 3], n=7, x=4))
print(solve.count(arr=[1, 1, 2, 2, 2, 2, 3], n=7, x=3))
