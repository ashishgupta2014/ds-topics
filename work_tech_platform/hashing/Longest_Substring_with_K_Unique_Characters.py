"""
https://workat.tech/problem-solving/practice/longest-substring-with-k-unique-characters

https://www.techiedelight.com/find-longest-substring-containing-k-distinct-characters/

https://www.youtube.com/watch?v=u5wTpaJ5QMU
"""
class Solution:
    CHAR_RANGE = 128
    def longestSubstringWithKUniqueCharacters(self, s: str, k: int):
        n = len(s)
        length = -1
        window = set()
        left = 0
        freq = [0] * self.CHAR_RANGE
        for i in range(n):
            window.add(s[i])
            freq[ord(s[i])] = freq[ord(s[i])] + 1
            while len(window) > k:
                freq[ord(s[left])] = freq[ord(s[left])] - 1
                if freq[ord(s[left])] == 0:
                    window.remove(s[left])
                left += 1
            if len(window) == k:
                length = max(length, i-left+1)

        return length


solve = Solution()
string =  "aabcdaddaf"
k = 3
print(solve.longestSubstringWithKUniqueCharacters(string, k))

string = "mississippi"
k = 4
print(solve.longestSubstringWithKUniqueCharacters(string, k))

string = "abcdef"
k = 3
print(solve.longestSubstringWithKUniqueCharacters(string, k))

string = "aaa"

k = 2

print(solve.longestSubstringWithKUniqueCharacters(string, k))

string = "aabacbebebe"
k = 3
print(solve.longestSubstringWithKUniqueCharacters(string, k))