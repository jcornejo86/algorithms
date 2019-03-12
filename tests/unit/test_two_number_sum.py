import pytest
from algorithms.two_number_sum import two_number_sum

test_data_two_number_sum = [
    ([4, 6], 10, [4, 6]),
    ([4, 6, 1], 5, [1, 4]),
    ([4, 6, 1, -3], 3, [-3, 6]),
    ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [8, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [3, 15]),
    ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5, [-5, 0]),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [-47, 210]),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, []),
    ([3, 5, -4, 8, 11, 1, -1, 6], 15, []),
]

class TestAlgorithms:

    @pytest.mark.parametrize("numbers,target_sum,expected", test_data_two_number_sum)
    def test_two_number_sum(self, numbers, target_sum, expected):
        result = two_number_sum(numbers, target_sum)

        assert result == expected
