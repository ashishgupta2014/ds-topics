def kth(array1, array2, m, n, k):
    if n > m:
        return kth(array2, array1, n, m, k)
    low = min(0, k - m)
    high = max(k, n)
    while low <= high:
        mid1 = low + (high - low) // 2
        mid2 = k - mid1
        left1 = float('-inf') if mid1 <= 0 else array1[mid1 - 1]
        right1 = float('inf') if mid1 >= m else array1[mid1]
        left2 = float('-inf') if mid2 <= 0 else array2[mid2 - 1]
        right2 = float('inf') if mid2 >= n else array2[mid2]
        if left1 < right2 and left2 < right1:
            return max(left1, left2)
        elif left1 > right2:
            high = mid1 - 1
        else:
            low = mid1 + 1


# ok for all test cases
import unittest


class Test(unittest.TestCase):
    def test_kth_1(self):
        k = 5
        actual = kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, k)
        expected = 6
        self.assertEqual(actual, expected)

    def test_kth_2(self):
        k = 4
        actual = kth([-2, -1, 3, 5, 6, 8], [1, 4, 8, 10], 6, 4, k)
        expected = 3
        self.assertEqual(actual, expected)

    def test_kth_3(self):
        k = 7
        actual = kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, k)
        expected = 256
        self.assertEqual(actual, expected)

    def test_kth_4(self):
        k = 4
        actual = kth([10, 20, 40, 60], [15, 35, 50, 70, 100], 4, 5, k)
        expected = 35
        self.assertEqual(actual, expected)
