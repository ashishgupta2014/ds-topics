"""
https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1?page=1&category[]=Heap&sortBy=submissions

Given an array Arr of N positive integers and an integer K, find K largest elements from the array.  The output elements should be printed in decreasing order.

Example 1:

Input:
N = 5, K = 2
Arr[] = {12, 5, 787, 1, 23}
Output: 787 23
Explanation: 1st largest element in the
array is 787 and second largest is 23.
Example 2:

Input:
N = 7, K = 3
Arr[] = {1, 23, 12, 9, 30, 2, 50}
Output: 50 30 23
Explanation: 3 Largest element in the
array are 50, 30 and 23.
Your Task:
You don't need to read input or print anything. Your task is to complete the function kLargest() which takes the array of integers arr, n and k as parameters and returns an array of integers denoting the answer. The array should be in decreasing order.

Expected Time Complexity: O(N + KlogK)
Expected Auxiliary Space: O(K+(N-K)*logK)

Constraints:
1 ≤ K ≤ N ≤ 105
1 ≤ Arr[i] ≤ 106
"""
import heapq


class Solution:

    def kLargest(self, arr, n, k):
        arr = [-ele for ele in arr]

        heapq.heapify(arr)

        return [-heapq.heappop(arr) for _ in range(k)]


if __name__ == '__main__':
    ob = Solution()
    arr = [12, 5, 787, 1, 23]
    k = 2
    ans = ob.kLargest(arr, len(arr), k)
    for x in ans:
        print(x, end=" ")
    print()

    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    ans = ob.kLargest(arr, len(arr), k)
    for x in ans:
        print(x, end=" ")
    print()
