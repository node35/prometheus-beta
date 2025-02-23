from typing import List, Dict, Any, Optional, Callable

def depth_first_search(graph: Dict[Any, List[Any]], 
                       start: Any, 
                       visitor: Optional[Callable[[Any], None]] = None) -> List[Any]:
    """
    Perform Depth-First Search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph.
        start (Any): Starting node for the DFS traversal.
        visitor (Optional[Callable[[Any], None]], optional): Optional visitor function 
                to be called on each node during traversal. Defaults to None.

    Returns:
        List[Any]: List of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid dictionary.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Track visited nodes and traversal order
    visited = set()
    traversal_order = []
    
    def dfs_recursive(node):
        # Mark node as visited
        visited.add(node)
        
        # Call visitor function if provided
        if visitor:
            visitor(node)
        
        # Add to traversal order
        traversal_order.append(node)
        
        # Recursively explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the start node
    dfs_recursive(start)
    
    return traversal_order