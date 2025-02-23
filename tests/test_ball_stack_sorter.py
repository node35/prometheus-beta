import pytest
from src.ball_stack_sorter import BallStackSorter

def test_initial_validation():
    # Test correct initialization
    valid_stacks = {
        'stack1': ['Red', 'Red', 'Red'],
        'stack2': ['Blue', 'Blue', 'Blue'], 
        'stack3': ['Green', 'Green', 'Green']
    }
    sorter = BallStackSorter(valid_stacks)
    assert sorter.total_balls == 9
    assert sorter.target_stack_size == 3

def test_invalid_stack_count():
    # Test that exactly 3 stacks are required
    with pytest.raises(ValueError, match="Exactly 3 stacks are required"):
        BallStackSorter({'stack1': ['Red'], 'stack2': ['Blue']})

def test_invalid_ball_count():
    # Test that total balls must be divisible by 3
    with pytest.raises(ValueError, match="Total number of balls must be divisible by 3"):
        BallStackSorter({
            'stack1': ['Red', 'Red'],
            'stack2': ['Blue', 'Blue'], 
            'stack3': ['Green']
        })

def test_already_sorted_stacks():
    sorted_stacks = {
        'stack1': ['Red', 'Red', 'Red'],
        'stack2': ['Blue', 'Blue', 'Blue'], 
        'stack3': ['Green', 'Green', 'Green']
    }
    sorter = BallStackSorter(sorted_stacks)
    states = sorter.sort_stacks()
    
    assert len(states) == 1  # Only initial state
    assert sorter.is_sorted()

def test_mixed_initial_state():
    mixed_stacks = {
        'stack1': ['Red', 'Blue', 'Green'],
        'stack2': ['Blue', 'Green', 'Red'], 
        'stack3': ['Green', 'Red', 'Blue']
    }
    sorter = BallStackSorter(mixed_stacks)
    states = sorter.sort_stacks()
    
    # Verify sorting is complete
    assert sorter.is_sorted()
    
    # Each stack should have exactly 3 balls of one color
    for stack in sorter.stacks.values():
        assert len(stack) == 3
        assert len(set(stack)) == 1

def test_move_ball():
    stacks = {
        'stack1': ['Red', 'Blue'],
        'stack2': ['Green'], 
        'stack3': []
    }
    sorter = BallStackSorter(stacks)
    
    # Move a ball from stack1 to stack3
    sorter.move_ball('stack1', 'stack3')
    
    assert sorter.stacks['stack1'] == ['Blue']
    assert sorter.stacks['stack3'] == ['Red']

def test_move_ball_from_empty_stack():
    stacks = {
        'stack1': [], 
        'stack2': ['Blue'], 
        'stack3': ['Green']
    }
    sorter = BallStackSorter(stacks)
    
    with pytest.raises(ValueError, match="Cannot move ball from empty stack: stack1"):
        sorter.move_ball('stack1', 'stack2')

def test_complex_sorting():
    # A more complex sorting scenario
    complex_stacks = {
        'stack1': ['Red', 'Blue', 'Green', 'Red'],
        'stack2': ['Blue', 'Green', 'Red', 'Blue'], 
        'stack3': ['Green', 'Red', 'Blue', 'Green']
    }
    sorter = BallStackSorter(complex_stacks)
    states = sorter.sort_stacks()
    
    # Verify sorting is complete
    assert sorter.is_sorted()
    
    # Each stack should have exactly 4 balls of one color
    for stack in sorter.stacks.values():
        assert len(stack) == 4
        assert len(set(stack)) == 1