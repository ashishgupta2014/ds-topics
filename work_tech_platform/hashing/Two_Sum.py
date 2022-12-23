"""
https://workat.tech/problem-solving/practice/two-sum
"""
class Solution:
    def twoSum(self, A, target: int):
        d = {}
        for i, ele in enumerate(A):
            num = target - ele
            if ele in d:
                return [d[ele], i]
            else:
                d[num] = i
        return []



solve = Solution()
A = [2, 4, 2, 3, 2]
target = 7
print(solve.twoSum(A, target))