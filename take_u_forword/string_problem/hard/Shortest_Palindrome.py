class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        j = n-1
        prefix = ''
        suffix = ''
        while i <= j:
            if s[i] == s[j]:
                prefix += s[i]
                suffix += s[j]
                i += 1
                j -= 1
            else:
                prefix += s[j]
                suffix += s[j]
                j -= 1
        return prefix+suffix[::-1]



solve = Solution()
print(solve.shortestPalindrome(s="abcd"))