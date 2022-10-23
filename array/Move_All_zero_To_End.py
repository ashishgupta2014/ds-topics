import unittest


def MoveZeroToEnd(array, n):
    zero_index = None
    for i in range(n):
        if array[i] == 0 and zero_index is None:
            zero_index = i
        elif zero_index is not None and array[i] != 0:
            array[zero_index], array[i] = array[i], array[zero_index]
            zero_index += 1
    return array


# ok for all test cases required
class Test(unittest.TestCase):

    def test_MoveZeroToEnd1(self):
        actual = MoveZeroToEnd([1, 3, 0, 0, 4, 0, 9], 7)
        expected = [1, 3, 4, 9, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd2(self):
        actual = MoveZeroToEnd([0, 1, 0, 3, 12], 5)
        expected = [1, 3, 12, 0, 0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd3(self):
        actual = MoveZeroToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9], 13)
        expected = [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)