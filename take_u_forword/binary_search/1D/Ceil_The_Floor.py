"""
https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1
"""
def getFloorAndCeil(arr, n, x):
    arr.sort()
    if arr[-1] < x:
        return arr[-1], -1
    elif arr[-1] == x:
        return arr[-1], arr[-1]
    elif arr[0] > x:
        return -1, arr[0]
    elif arr[0] == x:
        return arr[0], arr[0]
    low = 0
    high = n-1
    floor = -1
    ceil = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            floor, ceil = arr[mid], arr[mid]
            break
        elif arr[mid] < x and (mid + 1 < n and arr[mid + 1] > x):
            floor, ceil = arr[mid], arr[mid+1]
            break
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return floor, ceil

print(getFloorAndCeil(arr=[5, 6, 8, 9, 6, 5, 5, 6], n=8, x=7))
print(getFloorAndCeil(arr=[5, 6, 8, 9, 6, 5, 5, 6], n=8, x=10))