"""
https://workat.tech/problem-solving/practice/repeat-and-missing-number-array
https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

https://www.youtube.com/watch?v=5nMGY4VUoRY
"""


class Solution:
    def findRepeatAndMissingNumber(self, nums):
        n = len(nums)
        x = 0
        y = 0

        # Will hold xor of all elements
        # and numbers from 1 to n
        xor1 = nums[0]

        # Get the xor of all array elements
        for i in range(1, n):
            xor1 = xor1 ^ nums[i]

        # XOR the previous result with numbers
        # from 1 to n
        for i in range(1, n + 1):
            xor1 = xor1 ^ i

        # Will have only single set bit of xor1
        set_bit_no = xor1 & ~(xor1 - 1)

        # Now divide elements into two
        # sets by comparing a rightmost set
        # bit of xor1 with the bit at the same
        # position in each element. Also,
        # get XORs of two sets. The two
        # XORs are the output elements.
        # The following two for loops
        # serve the purpose
        for i in range(n):
            if (nums[i] & set_bit_no) != 0:

                # arr[i] belongs to first set
                x = x ^ nums[i]
            else:

                # arr[i] belongs to second set
                y = y ^ nums[i]

        for i in range(1, n + 1):
            if (i & set_bit_no) != 0:

                # i belongs to first set
                x = x ^ i
            else:

                # i belongs to second set
                y = y ^ i

        # x and y hold the desired
        # output elements
        if y in nums:
            x, y = y, x
        return [x, y]

solve = Solution()
arr = [3, 2, 1, 2]
print(solve.findRepeatAndMissingNumber(arr))

arr = [5, 3, 2, 4, 3]
print(solve.findRepeatAndMissingNumber(arr))