"""
https://practice.geeksforgeeks.org/problems/index-of-the-first-occurrence-of-pattern-in-a-text/1
https://www.youtube.com/watch?v=qQ8vS2btsxI
"""
class Solution:
    codes = {chr(ch): ch-97+1 for ch in range(97, 123)}
    def findMatching(self, text, pattern):
        hash_code = sum([self.codes[p] for p in pattern])
        window = len(pattern)
        run_sum = sum([self.codes[text[i]] for i in range(0, window)])
        if run_sum == hash_code and pattern == text[:window]:
            return 0
        i = 0
        j = window
        while j < len(text):
            run_sum -= self.codes[text[i]]
            i += 1
            run_sum += self.codes[text[j]]
            j += 1
            if run_sum == hash_code and pattern == text[i:j]:
                return i

        return -1



solve = Solution()
print(solve.findMatching(text='aaaab', pattern='aab'))