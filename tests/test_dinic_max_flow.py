import pytest
from src.dinic_max_flow import DinicMaxFlow

def test_simple_max_flow():
    """Test a simple max flow scenario."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    assert max_flow_solver.max_flow(0, 5) == 19

def test_complex_max_flow():
    """Test a more complex max flow scenario."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 4: 2},
        2: {4: 2},
        3: {5: 2},
        4: {3: 1, 5: 3},
        5: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    assert max_flow_solver.max_flow(0, 5) == 4

def test_no_path_max_flow():
    """Test scenario with no path between source and sink."""
    graph = {
        0: {1: 5},
        1: {2: 3},
        2: {3: 2},
        3: {},
        4: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    assert max_flow_solver.max_flow(0, 4) == 0

def test_same_source_sink():
    """Test when source and sink are the same node."""
    graph = {
        0: {1: 5, 2: 3},
        1: {2: 2},
        2: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    assert max_flow_solver.max_flow(0, 0) == 0

def test_invalid_nodes():
    """Test handling of invalid source or sink nodes."""
    graph = {
        0: {1: 5},
        1: {}
    }
    
    max_flow_solver = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(2, 1)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(0, 2)

def test_empty_graph():
    """Test max flow on an empty graph."""
    graph = {}
    
    max_flow_solver = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(0, 1)