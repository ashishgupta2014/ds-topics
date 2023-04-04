"""
https://leetcode.com/problems/merge-intervals/description/

https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = result[-1]
            next_start, next_end = intervals[i]
            if end >= next_start:
                n = len(result)-1
                s = min(start, next_start)
                e = max(end, next_end)
                result[n] = [s, e]
            else:
                result.append(intervals[i])
        return result

solve = Solution()
print(solve.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))
print(solve.merge(intervals=[[1,4],[4,5]]))
print(solve.merge(intervals=[[1,4],[0,0]]))
print(solve.merge(intervals=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))