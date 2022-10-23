def sort012(arr, n):
    i = low = 0
    high = n
    while i <= high:
        if arr[i] == 2:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        elif arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        else:
            i += 1


if __name__ == '__main__':
    array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    sort012(array, len(array) - 1)
    print(array)
