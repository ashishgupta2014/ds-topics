class Solution:
    def nextGreaterElements(self, A):
        n = len(A)
        stack, res = [], [-1] * n
        for i in range(n * 2):
            while stack and (A[stack[-1]] < A[i % n]):
                res[stack.pop()] = A[i % n]
            stack.append(i % n)
        return res


nums = [1, 2, 3, 4, 3]
print(Solution().nextGreaterElements(nums))
