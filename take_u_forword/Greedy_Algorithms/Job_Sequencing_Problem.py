"""
https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

https://takeuforward.org/data-structure/job-sequencing-problem/
"""
class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x[2], reverse=True)
        max_deadline = max([j for _, j, _ in Jobs])
        slot = [-1]*(max_deadline+1)
        countJobs = jobProfit = 0
        for i in range(n):
            for j in range(Jobs[i][1], 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += Jobs[i][2]
                    break
        return countJobs, jobProfit



solve = Solution()
print(solve.JobScheduling(Jobs=[(1,4,20),(2,1,10),(3,1,40),(4,1,30)], n=4))