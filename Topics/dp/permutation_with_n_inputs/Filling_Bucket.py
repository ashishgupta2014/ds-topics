"""
https://practice.geeksforgeeks.org/problems/filling-bucket0529/1

Given a Bucket having a capacity of N litres and the task is to determine that by how many ways you can fill
it using two bottles of capacity of 1 Litre and 2 Litre only. Find the answer modulo 108.


Example 1:

Input:
3
Output:
3
Explanation:
Let O denote filling by 1 litre bottle and
T denote filling by 2 litre bottle.
So for N = 3, we have :
{OOO,TO,OT}. Thus there are 3 total ways.
Example 2:

Input:
4
Output:
5
Explanation:
Let O denote filling by 1 litre bottle and
T denote filling by 2 litre bottle.
So for N = 4, we have :
{TT,OOOO,TOO,OTO,OOT} thus there are 5 total ways.
Your Task:
You don't need to read input or print anything. Your task is to complete the function fillingBucket() which
takes an Integer N as input and returns the number of total ways possible.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""


class Solution:
    def fillingBucket(self, n):
        dp = {
            0: 0,
            1: 1,
            2: 2}
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 100000000
        return dp[n]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        N = 4

        ob = Solution()
        res = ob.fillingBucket(N)
        print(res)
        assert 5 == res
