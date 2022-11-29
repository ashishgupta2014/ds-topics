"""
https://workat.tech/problem-solving/practice/next-greater-element
https://www.youtube.com/watch?v=Du881K7Jtk8

"""


# class Solution:
#     def getNextGreaterElement(self, A):
#         stack = []
#         output = [-1] * len(A)
#         for i in range(len(A) - 1, -1, -1):
#             if stack and stack[-1] > A[i]:
#                 output[i] = stack[-1]
#             elif stack and stack[-1] < A[i]:
#                 while stack and stack[-1] <= A[i]:
#                     stack.pop()
#                 if stack:
#                     output[i] = stack[-1]
#
#             stack.append(A[i])
#         return output

class Solution:
    def getNextGreaterElement(self, A):
        stack = []
        output = [-1] * len(A)
        for i in range(len(A)):
            while stack and A[stack[-1]] < A[i]:
                output[stack.pop()] = A[i]
            stack.append(i)
        return output


solve = Solution()
# arr = [3, 1, 2, 4, 5]
# arr = [1, 2, 3, 4]
arr = [1, 5, 2, 3, 5]

print(solve.getNextGreaterElement(arr))
