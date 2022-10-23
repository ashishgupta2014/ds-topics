# Find out if a key exists in the sorted list
# array[left..right] or not using binary search algorithm
def binarySearch(nums, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return -1


def recursivebinarySearch(nums, low, high, target):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return recursivebinarySearch(nums, mid + 1, high, target)
    else:
        return recursivebinarySearch(nums, low, mid - 1, target)


if __name__ == '__main__':

    array = [2, 5, 6, 8, 9, 10]
    key = 5
    index = recursivebinarySearch(array, 0, len(array)-1, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")
