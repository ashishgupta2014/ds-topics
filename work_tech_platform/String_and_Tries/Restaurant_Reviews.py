"""
https://workat.tech/problem-solving/practice/restaurant-reviews

https://workat.tech/problem-solving/approach/rr/restaurant-reviews
"""
from typing import List

class Trie:
    def __init__(self):
        self.character = {}
        self.is_leaf = False


class Solution:

    def insert(self, root, word):
        cur = root
        for w in word:
            cur = cur.character.setdefault(w, Trie())
        cur.is_leaf = True

    def has_good_word(self, root, word):
        cur = root
        for w in word:
            if w not in cur.character:
                return False
            cur = cur.character[w]
        if cur.is_leaf:
            return True
        return False

    def orderReviews(self, reviews: List[str], goodWords: List[str]) -> List[str]:
        root = Trie()
        for word in goodWords:
            self.insert(root, word)

        rating = []
        for review in reviews:
            num_good_words = 0
            for word in review.split(' '):
                if self.has_good_word(root, word):
                    num_good_words += 1

            if self.has_good_word(root, review):
                num_good_words += 1
            rating.append([review, num_good_words])
        rating = sorted(rating, key=lambda x: x[1], reverse=True)
        return [r[0] for r in rating]


solve = Solution()
print(solve.orderReviews(reviews=["good restaurant", "tasty food nice ambience", "nice place"],
                         goodWords=["good", "lovely", "nice", "tasty"]))



