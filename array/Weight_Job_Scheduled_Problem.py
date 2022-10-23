class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        dp = [0 for _ in range(len(jobs))]
        dp[-1] = jobs[len(jobs)-1][2]
        self.startTime = [i[0] for i in jobs]
        for i in range(len(jobs) - 2, -1, -1):
            # find the index of the first job starting
            # after ith job has finished
            # to find that, we find the element which is
            # equal to or next greater than endTime[i] in startTime
            index = self.find_index(i, len(startTime) - 1, jobs[i][1])
            res = dp[index] if index < len(startTime) else 0
            dp[i] = max(jobs[i][2] + res, dp[i + 1])
        return dp[0]

    def find_index(self, low, high, target):
        if low > high:
            return low
        mid = (low + high) // 2
        if self.startTime[mid] >= target:
            return self.find_index(low, mid - 1, target)
        return self.find_index(mid + 1, high, target)


solve = Solution()
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
print(solve.jobScheduling(startTime, endTime, profit))