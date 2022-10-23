# https://leetcode.com/problems/find-pivot-index/solution/
def pivotIndex(nums):
    S = sum(nums)
    left_sum = 0
    for i, ele in enumerate(nums):
        if left_sum == S - left_sum - ele:
            return i
        left_sum += ele
    return -1


arr = [1, 7, 3, 6, 5, 6]
print(pivotIndex(arr))
