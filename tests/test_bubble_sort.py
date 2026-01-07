import pytest

from Bubble_Sort import bubble_sort


def test_sort_returns_sorted_list():
    sorter = bubble_sort()
    data = [3, 1, 2]
    result = sorter.sort(data)
    assert result == [1, 2, 3]
    assert sorter.getSorted == [1, 2, 3]


def test_sort_handles_numeric_strings():
    sorter = bubble_sort()
    data = ["3", "1", "2"]
    result = sorter.sort(data)
    assert result == ["1", "2", "3"]


def test_sort_raises_for_non_iterable():
    sorter = bubble_sort()
    with pytest.raises(ValueError):
        sorter.sort(None)


def test_sort_raises_for_non_numeric_values():
    sorter = bubble_sort()
    with pytest.raises(ValueError):
        sorter.sort(["a", "b"])
