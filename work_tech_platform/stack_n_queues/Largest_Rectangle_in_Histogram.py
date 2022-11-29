class Solution:
    def getLargestArea(self, heights) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                start = index
                max_area = max(max_area, area)
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)
        return max_area


solve = Solution()

heights = [2, 1, 5, 6, 2, 3]

print(solve.getLargestArea(heights))
