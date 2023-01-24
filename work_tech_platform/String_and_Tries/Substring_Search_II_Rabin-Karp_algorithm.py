"""
https://workat.tech/problem-solving/practice/substring-search-rabin-karp

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

https://takeuforward.org/string/rabin-karp-algorithm-pattern-searching/
https://www.youtube.com/watch?v=qQ8vS2btsxI
"""
class Solution:
    chars_dict = {chr(ch): ch-97+1 for ch in range(97, 123)}
    def findStartIndexOfSubstring(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        if n >=m:
            hash_code = 0
            hash_comp = 0
            j = 0
            for i in range(m-1, -1, -1):
                hash_code += self.chars_dict[s2[j]]*(len(self.chars_dict)**i)
                hash_comp += self.chars_dict[s1[j]]*(len(self.chars_dict)**i)
                j += 1
            if hash_comp == hash_code and s1[:j] == s2:
                return 0
            k = 0
            for i in range(j, n):
                hash_comp -= self.chars_dict[s1[k]]*(len(self.chars_dict)**(m-1))
                k += 1
                hash_comp *= len(self.chars_dict)
                hash_comp += self.chars_dict[s1[i]]
                if hash_comp == hash_code and s2 == s1[k:i+1]:
                    return k
        return -1


solve = Solution()
print(solve.findStartIndexOfSubstring(s1="helloworld", s2="low"))
print(solve.findStartIndexOfSubstring(s1="aaaaab", s2="aab"))
print(solve.findStartIndexOfSubstring(s1="ccaccaaedba", s2="dba"))
print(solve.findStartIndexOfSubstring(s1="a", s2="a"))

