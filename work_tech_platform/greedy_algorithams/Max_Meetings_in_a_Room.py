"""
https://workat.tech/problem-solving/practice/max-meetings-in-a-room

https://www.youtube.com/watch?v=II6ziNnub1Q
"""
from typing import List


class Solution:
    max_count = 0
    def dfs(self, meetings, last_end, i, count):
        if i >= len(meetings):
            self.max_count = max(self.max_count, count)
            return
        for j in range(i, len(meetings)):
            if 0 < j < len(meetings):
                start, end = meetings[j]
                if last_end <= start:
                    self.dfs(meetings, end, j+1, count+1) # include
                self.dfs(meetings, last_end, j+1, count) # not include


    def getMaxMeetings(self, meetings: List) -> int:
        meetings = [(m.start, m.end) for m in meetings]
        meetings = sorted(meetings, key=lambda j: j[1])
        # self.max_count = 0
        # self.dfs(meetings, meetings[0][1], 1, 1)
        # return self.max_count
        max_count = 1
        finish_time = meetings[0][1]
        for i in range(1, len(meetings)):
            if meetings[i][0] >= finish_time:
                max_count += 1
                finish_time = meetings[i][1]
        return max_count






solve = Solution()
print(solve.getMaxMeetings(meetings=[(3, 29), (50, 93), (88, 92), (54, 67), (50, 87)]))

print(solve.getMaxMeetings(meetings=[(66, 77), (55, 94), (73, 79), (90, 97), (43, 62)]))

print(solve.getMaxMeetings(meetings=[(57, 62), (36, 80), (50, 94), (12, 75), (62, 68), (17, 49), (62, 63)]))

print(solve.getMaxMeetings(meetings=[(32, 58), (39, 48), (1, 44), (40, 95), (34, 73)]))