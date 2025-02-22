import pytest
from src.dinic_max_flow import DinicMaxFlow

def test_simple_max_flow():
    """Test a simple graph with one path"""
    graph = {
        0: {1: 10},
        1: {2: 10},
        2: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 2) == 10

def test_multiple_paths():
    """Test a graph with multiple augmenting paths"""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 5, 3: 10},
        2: {3: 15},
        3: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 3) == 20

def test_complex_flow_graph():
    """Test a more complex flow graph"""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 4: 2},
        2: {3: 2, 4: 2},
        3: {5: 2},
        4: {5: 3},
        5: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 5) == 4

def test_no_path_graph():
    """Test a graph with no path between source and sink"""
    graph = {
        0: {},
        1: {},
        2: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 2) == 0

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {
        0: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 0) == 0

def test_symmetric_flow_graph():
    """Test a symmetric flow graph"""
    graph = {
        0: {1: 5, 2: 5},
        1: {2: 3, 3: 4},
        2: {3: 6},
        3: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 3) == 8

def test_large_capacity_graph():
    """Test a graph with large capacities"""
    graph = {
        0: {1: 1000000, 2: 1000000},
        1: {2: 500000, 3: 500000},
        2: {3: 1000000},
        3: {}
    }
    dinic = DinicMaxFlow(graph)
    assert dinic.max_flow(0, 3) == 1000000