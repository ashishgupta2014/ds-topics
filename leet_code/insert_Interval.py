class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

# intervals = [[1, 3], [6, 9]]
# newInterval = [2, 5]

# intervals = []
# newInterval = [5, 7]


# intervals = [[1, 5]]
# newInterval = [2, 3]


# intervals = [[1, 5]]
# newInterval = [6, 8]
solve = Solution()
print(solve.insert(intervals=intervals, newInterval=newInterval))
