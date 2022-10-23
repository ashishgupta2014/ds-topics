from collections import Counter


class Solution:
    def match(self, s, p):
        for k, v in p.items():
            if k not in s or s[k] != v:
                return False
        return True

    def findAnagrams(self, s: str, p: str):
        n = len(s)
        w = len(p)
        i = 0
        res = []
        f = Counter(p)
        while i < n:
            temp = Counter(s[i:i+w])
            if self.match(temp, f):
                res.append(i)
            i += 1
        return res


s = 'abab'
p = 'ab'
result = Solution().findAnagrams(s, p)
print(result)
