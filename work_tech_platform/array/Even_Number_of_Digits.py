class Solution:

    def length(self, n):
        count = 0
        while n > 0:
            count += 1
            n = n // 10
        return count

    def getEvenDigitNumbers(self, arr):
        ans = []
        for num in arr:
            if len(str(num)) % 2 == 0:
                ans.append(num)
        return ans


solve = Solution()
# arr = [42, 564, 5775, 34, 123, 454, 1, 5, 45, 3556, 23442]
arr = [3, 11, 4, 200]
print(solve.getEvenDigitNumbers(arr))
