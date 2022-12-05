class Solution:
    def getNextGreaterElement(self, arr, key: int) -> int:
        low = 0
        n = len(arr)
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if mid == 0 and arr[mid] > key:
                return arr[mid]
            elif mid == n - 1 and arr[mid] > key:
                return key
            elif 0 < mid < n - 1 and arr[mid - 1] <= key < arr[mid + 1] and arr[mid] > key:
                return arr[mid]
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return key


solve = Solution()

arr = [1, 2, 3, 3, 4, 4, 8, 10]
key = 4

print(solve.getNextGreaterElement(arr, key))


