import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    """Test basic frequency sorting scenario."""
    input_list = [1, 1, 2, 2, 2, 3]
    expected = [3, 1, 1, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    """Test sorting an empty list."""
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    """Test sorting a list with a single element."""
    assert sort_by_frequency([5]) == [5]

def test_sort_by_frequency_all_same():
    """Test sorting a list where all elements are the same."""
    input_list = [4, 4, 4, 4]
    assert sort_by_frequency(input_list) == [4, 4, 4, 4]

def test_sort_by_frequency_complex_scenario():
    """Test a more complex sorting scenario with multiple frequencies."""
    input_list = [5, 5, 4, 4, 4, 3, 3, 3, 3]
    expected = [5, 5, 4, 4, 4, 3, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_with_negative_numbers():
    """Test sorting with negative numbers."""
    input_list = [-1, -1, 2, 2, 2, 3, 3]
    expected = [3, -1, -1, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected