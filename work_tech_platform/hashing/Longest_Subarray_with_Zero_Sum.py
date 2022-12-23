"""
https://workat.tech/problem-solving/practice/longest-subarray-zero-sum

https://www.youtube.com/watch?v=xmguZ6GbatA

https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=9
"""

class Solution:
    def longestSubarrayWithZeroSum(self, A) -> int:
        long = 0
        d = {}
        prefix_sum = 0
        for i, ele in enumerate(A):
            prefix_sum += ele
            if prefix_sum == 0:
                long = max(long, i+1)
            else:
                if prefix_sum in d:
                    long = max(long, i - d[prefix_sum])
                else:
                    d[prefix_sum] = i
        return long

solve = Solution()

arr =  [3, 0, -1, -2, 3, 0, -2]

print(solve.longestSubarrayWithZeroSum(arr))

"""
long = 4

s = 3+0 = 3-1 = 2-2=0+3=3+0=3-2=1
d = {
3: 0,
2:2,
}
"""
