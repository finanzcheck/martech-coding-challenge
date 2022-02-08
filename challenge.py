import unittest


def flatten(items):
    pass


param_list = [
    (
        [(1, 2, [0.6, 7.8]), (1, 0), [[0.3, 2.3], 0, 1], 6],  # input
        [1, 2, 0.6, 7.8, 1, 0, 0.3, 2.3, 0, 1, 6]  # expected output
    ),
    (
        [1, 2, 3],  # input
        [1, 2, 3]  # expected output
    ),
    (
        [None],  # input
        [None]  # expected output
    ),
    (
        [],  # input
        []  # expected output
    ),
    (
        [[]],  # input
        []  # expected output
    ),
    (
        ['abc', 1],  # input
        ['abc', 1]  # expected output
    )
]


class TestFlattenList(unittest.TestCase):

    def test_flatten_list(self):
        for input, expected in param_list:
            actual = flatten(input)
            with self.subTest(msg="Checking if actual equals expected", actual=actual, expected=expected):
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
