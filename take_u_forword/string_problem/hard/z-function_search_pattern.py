"""
https://www.scaler.com/topics/data-structures/z-algorithm/

https://www.youtube.com/watch?v=z2pcwg82rOE
"""
class Solution:

    def z_function(self, string, z):
        n = len(string)
        left = right = 0
        for i in range(1, n):
            if i > right:
                left = right = i
                while right < n and string[right-left] == string[right]:
                    right += 1
                z[i] = right-left
                right -= 1
            else:
                k = i-left
                if z[k] < right-i+1:
                    z[i] = z[k]
                else:
                    left = i
                    while right < n and string[right - left] == string[right]:
                        right += 1
                    z[i] = right - left
                    right -= 1
        return z

    def findMatching(self, text, pattern):
        string = pattern + '$' + text
        z = [0]*len(string)
        z = self.z_function(string, z)
        for i in range(len(pattern)+1, len(string)):
            if z[i] == len(pattern):
                return i-len(pattern)-1
        return -1

solve = Solution()
print(solve.findMatching(text='aaaab', pattern='aab'))