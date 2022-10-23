def mergesort(array):
    low = 0
    high = len(array) - 1
    partition(array, low, high)


def partition(array, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    partition(array, low, mid)
    partition(array, mid + 1, high)
    merge(array, low, mid, high)
    return


def merge(array, low, mid, high):
    left = array[low:mid+1]
    right = array[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            array[k] = right[j]
            j += 1
        else:
            array[k] = left[i]
            i += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        array[k] = right[j]
        k += 1
        j += 1


if __name__ == '__main__':
    arr = [8, 4, 3, 12, 25, 6, 13, 10]
    mergesort(arr)
    print(arr)
