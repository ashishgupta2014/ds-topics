
def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    inversion = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inversion += mid-i + 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1
    return inversion


def mergeSort(arr, low, high):
    inversion = 0
    if low < high:
        mid = low + (high - low) // 2
        inversion = mergeSort(arr, low, mid)
        inversion += mergeSort(arr, mid + 1, high)
        inversion += merge(arr, low, mid, high)
    return inversion


def getInversions(arr, n):
    return mergeSort(arr, 0, n - 1)


# Taking inpit using fast I/O.
def takeInput():
    n = 5
    arr = [1, 1, 2, 2, 3]
    return arr, n


# Main.
arr, n = takeInput()
print(getInversions(arr, n))
