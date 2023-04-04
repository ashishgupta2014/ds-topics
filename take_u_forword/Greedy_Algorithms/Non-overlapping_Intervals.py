"""
https://leetcode.com/problems/non-overlapping-intervals/description/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i[0])
        keep = [intervals[0]]  # the intervals that won't be rm

        for i in range(1, len(intervals)):
            if keep[-1][1] > intervals[i][1]:  # [1,3] vs. [1,2]
                keep[-1] = intervals[i]
            else:
                if keep[-1][1] <= intervals[i][0]:  # [1,2] vs. [2,3]
                    keep.append(intervals[i])
        return len(intervals) - len(keep)


solve = Solution()
print(solve.eraseOverlapIntervals(intervals=[[1,2],[2,3],[3,4],[1,3]]))