maxN = 10 ** 10  # the maximum value in the array possible.


class Solution:
    def upperBound(self, arr, low, high, element):
        while low < high:
            middle = low + (high - low) // 2
            if arr[middle] > element:
                high = middle
            else:
                low = middle + 1
        return low

    def getKthElement_binary_search(self, arr1, arr2, k):
        left = 1
        n = len(arr1)
        m = len(arr2)
        right = maxN  # The range of where ans can lie.
        ans = float('inf')  # We have to find min of all
        # the ans so take .

        # using binary search to check all possible values of
        # kth element
        while left <= right:
            mid = (left + right) // 2
            up_cnt = self.upperBound(arr1, 0, n, mid)
            up_cnt += self.upperBound(arr2, 0, m, mid)

            if up_cnt >= k:
                ans = min(ans, mid)  # find the min of all answers.
                right = mid - 1  # Try to find a smaller answer.
            else:
                left = mid + 1  # Current mid is too small so
                # shift right.
        return ans

    def getKthElement_merge_sort(self, firstArr, secondArr, k: int) -> int:
        m = len(firstArr)
        n = len(secondArr)
        if m < n:
            return self.getKthElement_merge_sort(secondArr, firstArr, k)
        i = 0
        j = 0
        count = 0
        while i < m and j < n:
            if firstArr[i] > secondArr[j]:
                ans = secondArr[j]
                j += 1
            else:
                ans = firstArr[i]
                i += 1
            count += 1
            if count == k:
                return ans
        while i < m:
            i += 1
            count += 1
            if count == k:
                return firstArr[i]
        while j < n:
            j += 1
            count += 1
            if count == k:
                return secondArr[j]


solve = Solution()

arr1 = [1, 10, 10, 25, 40, 54, 79]
arr2 = [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90]
k = 15
print(solve.getKthElement_merge_sort(arr1, arr2, k))
print(solve.getKthElement_binary_search(arr1, arr2, k))

# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
