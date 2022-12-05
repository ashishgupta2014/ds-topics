"""
https://workat.tech/problem-solving/practice/search-rotated-array
"""


class Solution:
    def getElementIndex(self, array, target: int) -> int:
        n = len(array)
        low = 0
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2

            if array[mid] == target:
                return mid
            elif array[low] <= array[mid]:
                if array[low] <= target <= array[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if array[mid] <= target <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        if array[low] == target:
            return low
        if array[high] == target:
            return high
        return -1


solve = Solution()

arr = [4, 5, 6, 7, 1, 2, 3]
target = 6
print(solve.getElementIndex(arr, target))
