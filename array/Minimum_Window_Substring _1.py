from collections import Counter

no_of_chars = 256


def findMinWindow(s, pat):
    match = Counter(pat)
    required = len(match)
    filtered_s = []
    for i, char in enumerate(s):
        if char in match:
            filtered_s.append((i, char))
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1
        if window_counts[character] == match[character]:
            formed += 1
        while l <= r and formed == required:
            character = filtered_s[l][1]
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
            window_counts[character] -= 1
            if window_counts[character] < match[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


actual = findMinWindow("ADOBECODEBANC", "ABC")
print(actual)
