"""
https://practice.geeksforgeeks.org/problems/fruit-into-baskets-1663137462/1
"""

class Solution:
    def sumSubarrayMins(self, N, fruits):
        left = 0
        right = 0
        ans = 0

        m = {}
        while right < N:
            if fruits[right] not in m:
                m[fruits[right]] = 1
            else:
                m[fruits[right]] += 1

            if len(m) > 2:
                m[fruits[left]] -= 1
                if m[fruits[left]] == 0:
                    del m[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans

solve = Solution()
print(solve.sumSubarrayMins(N=6, fruits=[0, 1, 2, 2, 2, 2]))
print(solve.sumSubarrayMins(N=3, fruits=[2, 1, 2]))
print(solve.sumSubarrayMins(N=41, fruits=list(map(int, '17 20 14 22 21 39 2 25 28 6 19 34 17 39 40 2 11 30 24 1 8 7 30 5 0 37 20 38 10 35 37 11 17 24 27 1 18 20 13 3 31'.split()))))