class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            low = 0
            high = cols - 1
            nums = grid[row]
            if nums[low] >= 0:
                while low <= high:
                    mid = low + (high - low) // 2
                    if nums[mid] < 0 and (0 < mid and nums[mid - 1] >= 0) or (mid == 0 and nums[mid] < 0):
                        count += cols - mid
                        break
                    elif nums[mid] >= 0:
                        low = mid + 1
                    else:
                        high = mid - 1
            else:
                count += cols
        return count


solve = Solution()
# grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
grid = [[3, -1, -3, -3, -3],
        [2, -2, -3, -3, -3],
        [1, -2, -3, -3, -3],
        [0, -3, -3, -3, -3]]
print(solve.countNegatives(grid))
