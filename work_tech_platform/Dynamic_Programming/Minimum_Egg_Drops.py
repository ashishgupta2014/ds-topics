"""
https://workat.tech/problem-solving/practice/egg-dropping
"""
class Solution:
    dp = [[-1 for _ in range(1000)] for _ in range(1000)]
    def dfs(self, floors, eggs):
        if eggs == 1 or floors in [0, 1]:
            return floors
        if self.dp[floors][eggs] != -1:
            return self.dp[floors][eggs]
        trial = float('inf')
        for f in range(1, floors+1):
            egg_broken = self.dp[f - 1][eggs - 1] if self.dp[f - 1][eggs - 1] != -1 else self.dfs(f - 1, eggs - 1)
            egg_not_broken = self.dp[floors - f][eggs] if self.dp[floors - f][eggs] != -1 else self.dfs(floors - f, eggs)
            temp = 1 + max(egg_broken, egg_not_broken)
            trial = min(trial, temp)
        self.dp[floors][eggs] = trial
        return trial

    def sample(self, floors, eggs):
        if floors in [0, 1] or eggs == 1:
            return floors
        trial = float('inf')
        for f in range(1, floors+1):
            egg_broken = self.sample(f-1, eggs-1)
            egg_not_broken = self.sample(floors-f, eggs)
            temp = 1 + max(egg_broken, egg_not_broken)
            trial = min(trial, temp)
        return trial
    def minimumMoves(self, k: int, n: int) -> int:
        return self.dfs(floors=n, eggs=k)
        # return self.sample(floors=n, eggs=k)


solve  = Solution()
print(solve.minimumMoves(k=1, n=2))
print(solve.minimumMoves(k=2, n=3))
print(solve.minimumMoves(k=2, n=5))
print(solve.minimumMoves(k=3, n=16))