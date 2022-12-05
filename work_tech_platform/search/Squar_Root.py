"""
https://workat.tech/problem-solving/practice/square-root
"""
class Solution:
    def searchRoot(self, n: int) -> int:
        low = 1
        high = n
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid == n:
                return mid
            elif mid * mid > n:
                high = mid - 1
            else:
                low = mid + 1
                ans = mid
        return ans




solve = Solution()

n = 26

print(solve.searchRoot(n))