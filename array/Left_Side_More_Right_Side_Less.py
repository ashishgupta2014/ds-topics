import unittest


def findElement(array, n):
    left = [0]*n
    left[0] = array[0]
    right = [0]*n
    right[n-1] = array[n-1]
    for i in range(1, n):
        left[i] = max(left[i-1], array[i])
    for i in range(n-2, -1, -1):
        right[i] = min(right[i+1], array[i])
    for i in range(1, n-1):
        if left[i] <= array[i] <= right[i]:
            return i
    return -1


# ok for all test cases required
class Test(unittest.TestCase):
    def test_findElement1(self):
        actual = findElement([5, 1, 4, 3, 6, 8, 10, 7, 9], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement2(self):
        actual = findElement([6, 2, 5, 4, 7, 9, 11, 8, 10], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement3(self):
        actual = findElement([5, 1, 4, 4], 4)
        expected = -1
        self.assertEqual(actual, expected)
