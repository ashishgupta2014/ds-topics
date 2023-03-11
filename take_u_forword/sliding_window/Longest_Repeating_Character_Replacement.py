"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/


"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = max_length = max_freq = 0
        char_counter = {}
        while right < len(s):
            char_counter[s[right]] = char_counter.get(s[right], 0) + 1
            # test window validity
            max_freq = max(max_freq, char_counter[s[right]])
            while (right-left+1 - max_freq) > k:
                char_counter[s[left]] -= 1
                left += 1
            max_length = max(max_length, right-left+1)

            right += 1
        return max_length



solve = Solution()
print(solve.characterReplacement(s='AABABBA', k=2))
print(solve.characterReplacement(s='ABAB', k=2))
print(solve.characterReplacement(s='ABBB', k=2))
print(solve.characterReplacement(s='BAAAB', k=2))
