from collections import Counter


class Solution:
    def longestPalindrome(self, words):
        freq = Counter(words)
        flag = False
        length = 0
        keys = list(freq.keys())
        for key in keys:
            if key == key[::-1]:
                length += freq[key] // 2
                if freq[key] % 2:
                    flag = True
            else:
                length += min(freq.get(key[::-1], 0), freq.get(key, 0))
                del freq[key]
        length *= 4
        if flag:
            length += 2
        return length


# words = ["ab", "ty", "yt", "lc", "cl", "ab"]
words = ["lc", "cl", "gg"]
#words = ["bb", "bb"]
solve = Solution()
print(solve.longestPalindrome(words))
