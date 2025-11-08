import pytest

from src.bubble_sort import bubble_sort
from src.heap_sort import heap_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-3, 5, 8, -1, 0, 0], [-3, -1, 0, 0, 5, 8]),
    ],
)
def test_heap_sort(input_list, expected):
    assert heap_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-3, 5, 8, -1, 0, 0], [-3, -1, 0, 0, 5, 8]),
    ],
)
def test_bubble_sort(input_list, expected):
    assert bubble_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-3, 5, 8, -1, 0, 0], [-3, -1, 0, 0, 5, 8]),
    ],
)
def test_merge_sort(input_list, expected):
    assert merge_sort(input_list) == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([], []),
        ([1], [1]),
        ([2, 2, 2], [2, 2, 2]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([-3, 5, 8, -1, 0, 0], [-3, -1, 0, 0, 5, 8]),
    ],
)
def test_quick_sort(input_list, expected):
    assert quick_sort(input_list) == expected
