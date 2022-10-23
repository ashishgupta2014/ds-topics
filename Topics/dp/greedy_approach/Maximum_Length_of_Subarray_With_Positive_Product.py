class Solution:
    def getMaxLen(self, nums) -> int:
        ans = 0
        pos = 0
        neg = 0

        for n in nums:
            if n > 0:
                pos += 1
                neg = 1 + neg if neg else 0
            elif n < 0:
                tmp = pos
                pos = 1 + neg if neg else 0
                neg = 1 + tmp
            else:
                pos = 0
                neg = 0
            ans = max(ans, pos)
        return ans


solve = Solution()

nums = [1, -2, -3, 4]

res = solve.getMaxLen(nums)
print(res)
assert 4 == res

nums = [0, 1, -2, -3, -4]
res = solve.getMaxLen(nums)
print(res)
assert 3 == res

nums = [-1, -2, -3, 0, 1]

res = solve.getMaxLen(nums)
print(res)
assert 2 == res