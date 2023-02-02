"""
https://practice.geeksforgeeks.org/problems/generate-all-binary-strings

"""
class Solution:

    def dfs(self, n, i, temp, result):
        if i == n:
            result.append(''.join(temp))
            return
        temp[i] = '0'
        self.dfs(n, i+1, temp, result)
        if (0 < i < len(temp) and temp[i-1] == '0') or (0 <= i < len(temp)-1 and temp[i+1] == '0') or i == 0:
            temp[i] = '1'
            self.dfs(n, i + 1, temp, result)

    def generateBinaryStrings(self, n):
        result = []
        temp = [None]*n
        self.dfs(n, 0, temp, result)
        return result

solve = Solution()
print(solve.generateBinaryStrings(n=3))
print(solve.generateBinaryStrings(n=4))
print(solve.generateBinaryStrings(n=2))
print(solve.generateBinaryStrings(n=1))
