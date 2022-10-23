# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version == 4:
        return True
    return False


def firstBadVersion(n: int) -> int:
    low = 1
    high = n

    while low <= high:
        mid = low + (high - low) // 2
        if 1 < mid < n:
            if isBadVersion(mid) and isBadVersion(mid + 1) and isBadVersion(mid - 1):
                high = mid - 1
            elif isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            else:
                low = mid + 1
        else:
            if isBadVersion(low):
                return low
            elif isBadVersion(high):
                return high
            else:
                return mid


print(firstBadVersion(5))
