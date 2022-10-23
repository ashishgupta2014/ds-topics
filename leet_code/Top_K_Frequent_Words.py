from collections import Counter


class MaxHeap:
    def __init__(self, data):
        self.data = data
        self._build()

    def heapify(self, k):
        left = self._left_child(k)
        right = self._right_child(k)
        if left < self._length and self.data[left][0] > self.data[k][0] and self.data[left][1] > self.data[k][1]:
            largest = left
        else:
            largest = k
        if right < self._length and self.data[right][0] > self.data[largest][0] and self.data[right][1] > \
                self.data[largest][1]:
            largest = right
        if largest != k:
            self.data[k], self.data[largest] = self.data[largest], self.data[k]
            self.heapify(largest)

    @staticmethod
    def _left_child(k):
        return 2 * k + 1

    @staticmethod
    def _right_child(k):
        return 2 * k + 2

    @property
    def _length(self):
        return len(self.data)

    def _build(self):
        n = int((self._length // 2) - 1)
        for k in range(n, -1, -1):
            self.heapify(k)

    def _index(self, ele):
        return self.data.index(ele)

    def delete(self, ele):
        if ele == self.data[-1]:
            last = self.data.pop()
        else:
            i = self._index(ele)
            self.data[i], self.data[-1] = self.data[-1], self.data[i]
            last = self.data.pop()
            self.heapify(i)
        return last

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        print('Before pop=', self.data)
        last = self.data.pop()
        self.heapify(0)
        print('After pop=', self.data)
        return last


class Solution:
    def topKFrequent(self, words, k: int):
        occurence_count = Counter(words)
        most_freq_words = occurence_count.most_common()
        pq = MaxHeap(most_freq_words)
        res = []
        print(pq.data)
        for i in range(k):
            res.append(pq.pop()[0])
        return res


solve = Solution()
arr = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print(solve.topKFrequent(arr, k))
