import pytest
from src.depth_first_search import depth_first_search

def test_basic_graph_traversal():
    """Test basic graph traversal with a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Confirm expected traversal order starting from 'A'
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_single_node_graph():
    """Test graph with only one node."""
    graph = {'X': []}
    result = depth_first_search(graph, 'X')
    assert result == ['X']

def test_disconnected_graph():
    """Test graph with disconnected nodes."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_visitor_function():
    """Test graph traversal with a visitor function."""
    visited_nodes = []
    
    def visitor(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    
    depth_first_search(graph, 'A', visitor=visitor)
    assert visited_nodes == ['A', 'B', 'D', 'C', 'E']

def test_invalid_graph():
    """Test that invalid graph raises TypeError."""
    with pytest.raises(TypeError):
        depth_first_search([1, 2, 3], 'A')

def test_nonexistent_start_node():
    """Test that nonexistent start node raises ValueError."""
    graph = {'A': ['B'], 'B': []}
    with pytest.raises(ValueError):
        depth_first_search(graph, 'C')

def test_empty_graph():
    """Test empty graph raises ValueError."""
    with pytest.raises(ValueError):
        depth_first_search({}, 'A')