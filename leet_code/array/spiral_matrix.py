class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom =0, len(matrix)
        while left< right and top< bottom:
            #left to right
            for i in range(left,right):
                res.append(matrix[top][i])
            top +=1
            #top to bottom
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -= 1

            #right to left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -=1
            #bottom to top last time
            for i in range(bottom-1,top -1,-1):
                res.append(matrix[i][left])
            left +=1
        return res[:len(matrix)*len(matrix[0])]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = Solution().spiralOrder(matrix)
print(result)
