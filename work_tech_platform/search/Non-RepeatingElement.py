"""
https://workat.tech/problem-solving/practice/non-repeating-element
"""


class Solution:
    def findNonRepeatingElement(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        elif arr[0] != arr[1]:
            return arr[0]
        elif arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid - 1] != arr[mid] and arr[mid + 1] != arr[mid]:
                return arr[mid]

            elif arr[mid + 1] == arr[mid] and mid % 2 == 0:
                low = mid + 1
            elif arr[mid - 1] == arr[mid] and mid % 2 != 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1


solve = Solution()
arr = [1, 1, 2, 3, 3, 4, 4]

print(solve.findNonRepeatingElement(arr))
