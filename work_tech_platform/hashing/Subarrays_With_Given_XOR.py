"""
https://workat.tech/problem-solving/practice/subarray-with-xor

https://www.geeksforgeeks.org/count-number-subarrays-given-xor/

"""
class Solution:
    def numSubarrayWithXOR(self, A, target: int) -> int:
        n = len(A)
        prefix_sum = [0]*n

        prefix_sum[0] = A[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1]^A[i]

        mp = dict()
        res = 0

        for i in range(n):
            tmp = target ^ prefix_sum[i]

            res += mp.get(tmp, 0)

            res += 1 if prefix_sum[i] == target else 0

            mp[prefix_sum[i]] = mp.get(prefix_sum[i], 0) + 1
        return res



solve = Solution()

A =  [1, 2, 3, 4]
k = 3

print(solve.numSubarrayWithXOR(A, k))


A = [2, 4, 3, 6, 7, 9]
k = 6
print(solve.numSubarrayWithXOR(A, k))