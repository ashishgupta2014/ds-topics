class MaxHeap:
    def __init__(self, data):
        self.data = data
        self._build()

    def heapify(self, k):
        left = self._left_child(k)
        right = self._right_child(k)
        if left < self._length and self.data[left] > self.data[k]:
            largest = left
        else:
            largest = k
        if right < self._length and self.data[right] > self.data[largest]:
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
        if self._length > 1:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            last = self.data.pop()
            self.heapify(0)
        elif self.data:
            last = self.data.pop()
        else:
            last = -1
        return last

    def insert(self, ele):
        if self._length == 0:
            self.data.append(ele)
        else:
            self.data.append(ele)
            self.heapify(0)


if __name__ == '__main__':
    arr = [7, 4, 6, 3, 9, 1]
    pq = MaxHeap(arr)
    print(pq.data)
    print(pq.delete(9))
    print(pq.data)
    print(pq.pop())
    print(pq.data)
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())
    print(pq.data)
    pq.insert(0)
    print(pq.data)


