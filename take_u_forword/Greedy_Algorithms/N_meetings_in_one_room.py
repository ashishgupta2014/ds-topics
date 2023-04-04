"""
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
"""
class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        meetings = list(zip(start, end))
        meetings = sorted(meetings, key=lambda j: j[1])
        max_count = 1
        finish_time = meetings[0][1]
        for i in range(1, n):
            if meetings[i][0] > finish_time:
                max_count += 1
                finish_time = meetings[i][1]
        return max_count

solve = Solution()
print(solve.maximumMeetings(n=6, start=[1,3,0,5,8,5], end=[2,4,6,7,9,9]))