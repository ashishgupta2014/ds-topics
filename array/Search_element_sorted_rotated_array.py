import unittest


def findNumber(arr, l, h, k):
    while l < h:
        m = l + (h - l) // 2
        if k == arr[m]:
            return m
        # array is sorted
        if arr[l] <= arr[m]:
            if arr[l] <= k <= arr[m]:
                h = m - 1
            else:
                l = m + 1
        else:  # array is non sorted
            if arr[m] <= k <= arr[h]:
                l = m + 1
            else:
                h = m - 1
    if arr[l] == k:
        return l
    elif arr[h] == k:
        return h
    else:
        return -1


class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = findNumber([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 0, 9, 1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber2(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber3(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 28)
        expected = -1
        self.assertEqual(actual, expected)

    def test_findNumber4(self):
        actual = findNumber([30, 40, 50, 10, 20], 0, 4, 10)
        expected = 3
        self.assertEqual(actual, expected)
