"""
https://leetcode.com/problems/valid-parenthesis-string/description/
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        opens = []
        for i, char in enumerate(s):
            if char == '(':
                opens.append(i)
            elif char == '*':
                stars.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while stars and opens:
            if stars[-1] > opens[-1]:
                stars.pop()
                opens.pop()
            else:
                break
        return len(opens) == 0

solve = Solution()
print(solve.checkValidString(s='(*))'))
print(solve.checkValidString(s='(*)'))
print(solve.checkValidString(s='()'))
print(solve.checkValidString(s='(((***'))
print(solve.checkValidString(s='***)))'))
print(solve.checkValidString(s='(((***)'))