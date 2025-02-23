from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's algorithm for maximum flow.
        
        :param graph: Adjacency list representation of the graph
                      Format: {source: {destination: capacity, ...}, ...}
        """
        self.graph = graph
        self.nodes = set(graph.keys()).union(
            set(node for adj_list in graph.values() for node in adj_list.keys())
        )
    
    def _bfs(self, source: int, sink: int) -> List[int]:
        """
        Perform Breadth-First Search to create level graph and check reachability.
        
        :param source: Source node
        :param sink: Sink node
        :return: List of levels for each node, None if sink is unreachable
        """
        # Reset level of all nodes
        level = {node: -1 for node in self.nodes}
        level[source] = 0
        
        # Queue for BFS
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            # Check all adjacent nodes
            for neighbor, capacity in self.graph.get(current, {}).items():
                # Only proceed if not visited and residual capacity exists
                if level[neighbor] == -1 and capacity > 0:
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)
        
        return level if level[sink] != -1 else None
    
    def _dfs(self, node: int, sink: int, flow: int, level: Dict[int, int], 
             flow_graph: Dict[int, Dict[int, int]]) -> int:
        """
        Depth-First Search to find augmenting paths in the level graph.
        
        :param node: Current node
        :param sink: Sink node
        :param flow: Current flow
        :param level: Level of each node from BFS
        :param flow_graph: Residual graph to track flows
        :return: Maximum additional flow
        """
        # Reached sink, return the flow
        if node == sink:
            return flow
        
        # Explore all adjacent nodes 
        for neighbor, capacity in self.graph.get(node, {}).items():
            # Check if this path is valid in the level graph
            residual = capacity - flow_graph.get(node, {}).get(neighbor, 0)
            
            if (level[neighbor] == level[node] + 1 and 
                residual > 0):
                
                # Try to push flow
                curr_flow = self._dfs(
                    neighbor, 
                    sink, 
                    min(flow, residual), 
                    level, 
                    flow_graph
                )
                
                # If a flow is found
                if curr_flow > 0:
                    # Update flow graph
                    flow_graph.setdefault(node, {})[neighbor] = \
                        flow_graph.get(node, {}).get(neighbor, 0) + curr_flow
                    flow_graph.setdefault(neighbor, {})[node] = \
                        flow_graph.get(neighbor, {}).get(node, 0) - curr_flow
                    
                    return curr_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink using Dinic's algorithm.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        """
        # Validate source and sink
        if source not in self.nodes or sink not in self.nodes:
            raise ValueError("Source or sink node not in graph")
        
        if source == sink:
            return 0
        
        # Track total flow and flow through each edge
        total_flow = 0
        flow_graph = {}
        
        # Repeat until no augmenting path is found
        while True:
            # Create level graph via BFS
            level = self._bfs(source, sink)
            
            # No path exists, algorithm terminates
            if level is None:
                break
            
            # Keep finding blocking flows
            while True:
                # Find augmenting path and its flow
                path_flow = self._dfs(source, sink, float('inf'), level, flow_graph)
                
                # No more augmenting paths
                if path_flow == 0:
                    break
                
                # Add to total flow
                total_flow += path_flow
        
        return total_flow