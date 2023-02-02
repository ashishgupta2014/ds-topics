"""
https://leetcode.com/problems/permutation-sequence/description/

https://www.youtube.com/watch?v=wT7gcXLYoao&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=19
"""
import math
import heapq


class Solution:

    def dfs(self, numbers, i, results):
        if i >= len(numbers):
            heapq.heappush(results, ''.join(numbers))
            return
        for j in range(i, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            self.dfs(numbers, i+1, results)
            numbers[i], numbers[j] = numbers[j], numbers[i]
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n+1)]
        ans = ''
        # results = []
        # self.dfs(numbers, 0, results)
        # for _ in range(k):
        #     ans = heapq.heappop(results)
        # return ans
        fact = math.factorial(n - 1)
        k -= 1
        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
        return ans



solve = Solution()
print(solve.getPermutation(n=4, k=17))