"""
https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock-iii

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
"""
from typing import List


class Solution:
    def maxProfit_optimized(self, prices: List[int]) -> int:
        if not prices:
            return 0

        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)

        return D
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <=1:
            return 0
        minPrice = prices[0]
        #leftMax is from 1....n-1
        leftMax,rightMax = [0]*n,[0]*n
        for i in range(1,n):
            minPrice = min(minPrice, prices[i])
            leftMax[i] = max(leftMax[i-1], prices[i]-minPrice)

        # rightMax is from 0...n-2
        maxPrice = prices[-1]
        for i in range(n-2,-1,-1):
            maxPrice = max(maxPrice, prices[i])
            rightMax[i] = max(rightMax[i+1], maxPrice-prices[i])
        res = [x+y for x,y in zip(leftMax,rightMax)]
        return max(res)

solve = Solution()

print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3, 5]))
print(solve.maxProfit(prices=[1, 2, 3, 4, 5]))
print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3]))
print(solve.maxProfit(prices=[1,2,4,2,5,7,2,4,9,0]))
# 7-1 = 6
# 9-2 = 7

