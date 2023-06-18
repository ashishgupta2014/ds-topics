"""
https://leetcode.com/problems/count-and-say/description/
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '2'
        string = '11'
        for _ in range(3, n+1):
            string += '$'
            length = len(string)
            count = 1
            temp = ''
            for i in range(1, length):
                if string[i] != string[i-1]:
                    temp += f'{count}{string[i-1]}'
                    count = 1
                else:
                    count += 1
            string = temp
        return string




solve = Solution()
print(solve.countAndSay(n=4))