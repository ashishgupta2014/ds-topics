"""
https://practice.geeksforgeeks.org/problems/geeks-training/1

https://takeuforward.org/data-structure/dynamic-programming-ninjas-training-dp-7/

https://www.youtube.com/watch?v=AE39gJYuRog&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=8
"""
class Solution:

    def dfs(self, points, n, day, last, dp):
        if day == 0:
            max_point_on_day_0 = 0
            for i in range(n):
                if i != last:
                    max_point_on_day_0 = max(max_point_on_day_0, points[day][i])
            return max_point_on_day_0
        if dp[day][last] != -1:
            return dp[day][last]
        max_point_on_day = 0
        for i in range(n):
            if i != last:
                score = points[day][i] + self.dfs(points, n, day-1, i, dp)
                max_point_on_day = max(max_point_on_day, score)
        dp[day][last] = max_point_on_day
        return max_point_on_day

    # def tabular(self, points, n):
    #     dp = [[0] * 4 for _ in range(n)]
    #     dp[0][0] = points[0][1] if points[0][1] > points[0][2] else points[0][2]
    #     dp[0][1] = points[0][0] if points[0][0] > points[0][2] else points[0][2]
    #     dp[0][2] = points[0][1] if points[0][1] > points[0][2] else points[0][2]
    #     #dp[0][3] = max(points[0])
    #     for day in range(1, n):
    #         for last in range(3):
    #             dp[day][last] = 0
    #             for task in range(3):
    #                 if task != last:
    #                     activity = points[day][task] + dp[day - 1][task]
    #                     dp[day][last] = max(dp[day][last], activity)
    #     return dp[n-1][2]

    def ninjaTraining(self, n, points):
        dp = [[0 for j in range(4)] for i in range(n)]

        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

        for day in range(1, n):
            for last in range(4):
                dp[day][last] = 0
                for task in range(3):
                    if task != last:
                        activity = points[day][task] + dp[day - 1][task]
                        dp[day][last] = max(dp[day][last], activity)

        return dp[n - 1][3]
    def maximumPoints(self, points, n):
        # dp = [[-1]*4 for _ in range(n)]
        # return self.dfs(points, n, n-1, 3, dp)
        # return self.tabular(points, n)
        return self.ninjaTraining(n, points)

solve = Solution()
print(solve.maximumPoints(points=[[1,2,5],[3,1,1],[3,3,3]], n=3))
print(solve.maximumPoints(points=[[10, 50, 1], [5, 100, 11]], n=2))