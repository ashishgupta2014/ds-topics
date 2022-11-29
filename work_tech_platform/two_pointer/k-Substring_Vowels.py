"""
https://workat.tech/problem-solving/practice/k-substring-vowels
"""


class Solution:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def kSubstringVowels(self, s: str, k: int):
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] in self.vowels:
                arr[i] = 1
            else:
                arr[i] = 0

        j = 0
        c = sum(arr[:k])
        res = [c]
        for i in range(k, len(arr)):
            c += arr[i]
            c -= arr[j]
            j += 1
            res.append(c)
        return res


solve = Solution()
s = 'workattech'
k = 3
print(solve.kSubstringVowels(s, k))
