import pytest
from src.color_stack_sorter import ColorStackSorter

def test_initial_state_validation():
    """Test that initialization requires equal length stacks"""
    with pytest.raises(ValueError):
        ColorStackSorter(['Red'], ['Blue'], ['Green', 'Red'])

def test_move_ball():
    """Test moving a ball between stacks"""
    sorter = ColorStackSorter(['Red'], ['Blue'], ['Green'])
    sorter.move_ball('Red', 'Blue')
    assert len(sorter.stacks['Red']) == 0
    assert len(sorter.stacks['Blue']) == 2

def test_move_ball_invalid_same_stack():
    """Test that moving to the same stack raises an error"""
    sorter = ColorStackSorter(['Red'], ['Blue'], ['Green'])
    with pytest.raises(ValueError):
        sorter.move_ball('Red', 'Red')

def test_move_ball_empty_stack():
    """Test moving from an empty stack raises an error"""
    sorter = ColorStackSorter([], ['Blue'], ['Green'])
    with pytest.raises(ValueError):
        sorter.move_ball('Red', 'Blue')

def test_is_sorted_positive():
    """Test is_sorted returns True for correctly sorted stacks"""
    sorter = ColorStackSorter(['Red', 'Red'], ['Blue', 'Blue'], ['Green', 'Green'])
    assert sorter.is_sorted() is True

def test_is_sorted_negative():
    """Test is_sorted returns False for unsorted stacks"""
    sorter = ColorStackSorter(['Red', 'Blue'], ['Blue', 'Red'], ['Green', 'Green'])
    assert sorter.is_sorted() is False

def test_sort_simple():
    """Test sorting a simple scenario"""
    sorter = ColorStackSorter(['Blue', 'Red'], ['Red', 'Blue'], ['Green', 'Green'])
    moves = sorter.sort()
    assert sorter.is_sorted() is True
    assert len(moves) > 0

def test_sort_complex():
    """Test sorting a more complex scenario"""
    sorter = ColorStackSorter(
        ['Blue', 'Red', 'Green'], 
        ['Green', 'Blue', 'Red'], 
        ['Red', 'Green', 'Blue']
    )
    moves = sorter.sort()
    assert sorter.is_sorted() is True
    assert len(moves) > 0