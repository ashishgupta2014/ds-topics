"""
https://workat.tech/problem-solving/practice/roman-to-integer

https://leetcode.com/problems/roman-to-integer/description/
"""
romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9}


class Solution:
    def romanToInt(self, s: str) -> int:
        prev = None
        result = 0
        for c in s:
            val = romans[c]
            if prev and val > prev:
                result -= 2 * prev
            else:
                prev = val
            result += val

        return result


solve = Solution()
print(solve.romanToInt(s='IX'))
print(solve.romanToInt(s='V'))
print(solve.romanToInt(s='MCMXCIV'))