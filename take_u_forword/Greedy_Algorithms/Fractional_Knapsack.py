"""
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/
"""
class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue

solve = Solution()
print(solve.fractionalknapsack(W=50, arr=[Item(val=60, w=10), Item(val=100, w=20), Item(val=120, w=30)], n=3))