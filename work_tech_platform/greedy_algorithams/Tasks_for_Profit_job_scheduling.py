"""
This is the Task class definition
https://workat.tech/problem-solving/practice/tasks-for-profit

https://workat.tech/problem-solving/approach/tfp/tasks-for-profit Improper Solution

https://www.techiedelight.com/job-sequencing-problem-deadlines/ Proper solution

https://www.youtube.com/watch?v=LjPx4wQaRIs

"""
import heapq
from typing import List

class Task:
    def __init__(self, deadline: int, profit: int):
        self.deadline = deadline
        self.profit = profit


class Solution:
    def getMaxProfit(self, tasks: List[Task]) -> int:
        tasks = [(i+1, t.deadline, t.profit)for i, t in enumerate(tasks)]
        tasks = sorted(tasks, key=lambda x:x[2], reverse=True)
        jobs = []
        for _, deadline, profit in tasks:
            if len(jobs) > deadline:
                if jobs[0] > profit:
                    continue
                heapq.heappop(jobs)
            heapq.heappush(jobs, profit)
        return sum(jobs)




solve = Solution()
print(solve.getMaxProfit(tasks=[Task(4, 20), Task(2, 10), Task(2, 40), Task(1, 30)]))

print(solve.getMaxProfit(tasks=[Task(2, 20), Task(2, 40), Task(2, 30), Task(1, 10), Task(3, 50), Task(3, 60)]))


