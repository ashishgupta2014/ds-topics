def findMaxValue(array, low, high):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = low + (high - low) // 2
        if array[mid] < array[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low


array = [3, 5, 15, 50, 11, 10, 8, 6]
# array = [6, 9, 15, 25, 35, 50, 41, 29, 23, 8]
# array = [6, 5, 4, 3, 2, 3, 2]
#array = [1, 2, 3]
n = len(array)
print("The maximum element is ", findMaxValue(array, 0, n - 1))
