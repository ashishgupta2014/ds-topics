class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] > arr[l]:
            largest = l
        if r < n and arr[largest] > arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        for i in range((n // 2) - 1, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        # code here
        self.buildHeap(arr, n)
        for i in range(n - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


solve = Solution()
arr = [4, 1, 3, 9, 7]
n = len(arr)
solve.HeapSort(arr, n)
print(arr)
