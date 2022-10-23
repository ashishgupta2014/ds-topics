class Solution:
    def canReach(self, arr, start: int) -> bool:
        N = len(arr)
        visited = set()
        dp = {}

        def func(n, visited):
            if n in dp:
                return dp[n]
            if n in visited:
                return
            visited.add(n)
            if n >= N or n < 0:
                return False

            if arr[n] == 0:
                return True
            dp[n] = func(n - arr[n], visited) or func(n + arr[n], visited)
            return dp[n]

        return func(start, visited)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
# arr = [3, 0, 2, 1, 2]
# start = 2
print(Solution().canReach(arr, start))
