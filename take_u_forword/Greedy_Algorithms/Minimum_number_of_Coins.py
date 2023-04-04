"""
https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

https://takeuforward.org/data-structure/find-minimum-number-of-coins/
"""
class Solution:

    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]

    def minPartition(self, N):
        res = []
        for c in range(len(self.coins)-1, -1, -1):
            while N >= self.coins[c]:
                N -= self.coins[c]
                res.append(self.coins[c])
        return res

solve = Solution()
print(solve.minPartition(N=43))