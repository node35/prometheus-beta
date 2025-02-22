from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's max flow algorithm with a graph.
        
        :param graph: Adjacency list representation of the graph
                      {node: {neighbor: capacity}}
        """
        self.graph = graph
        self.nodes = set(graph.keys()).union(
            set(node for neighbors in graph.values() for node in neighbors)
        )
    
    def bfs(self, source: int, sink: int) -> List[int]:
        """
        Perform Breadth-First Search to create level graph.
        
        :param source: Source node
        :param sink: Sink node
        :return: List of levels for each node, or None if sink is unreachable
        """
        level = {node: -1 for node in self.nodes}
        level[source] = 0
        
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in self.graph[current].items():
                if level[neighbor] == -1 and capacity > 0:
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)
        
        return level if level[sink] != -1 else None
    
    def dfs(self, node: int, sink: int, flow: int, 
            level: Dict[int, int], 
            flow_graph: Dict[int, Dict[int, int]]) -> int:
        """
        Depth-First Search to find augmenting paths.
        
        :param node: Current node
        :param sink: Sink node
        :param flow: Current flow
        :param level: Level graph
        :param flow_graph: Residual graph
        :return: Augmented flow
        """
        if node == sink:
            return flow
        
        for neighbor, capacity in flow_graph[node].items():
            if (level[neighbor] == level[node] + 1 and 
                capacity > 0):
                curr_flow = self.dfs(
                    neighbor, 
                    sink, 
                    min(flow, capacity), 
                    level, 
                    flow_graph
                )
                
                if curr_flow > 0:
                    flow_graph[node][neighbor] -= curr_flow
                    flow_graph[neighbor][node] += curr_flow
                    return curr_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Find the maximum flow from source to sink using Dinic's algorithm.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        """
        # Create a deep copy of the graph to modify for flow
        flow_graph = {
            node: dict(neighbors) 
            for node, neighbors in self.graph.items()
        }
        
        # Add reverse edges if not present
        for node in flow_graph:
            for neighbor in flow_graph[node]:
                if neighbor not in flow_graph or node not in flow_graph[neighbor]:
                    if neighbor not in flow_graph:
                        flow_graph[neighbor] = {}
                    flow_graph[neighbor][node] = 0
        
        max_flow = 0
        
        while True:
            # Create level graph using BFS
            level = self.bfs(source, sink)
            
            # If no path exists, break
            if level is None:
                break
            
            # Find augmenting paths using DFS
            while True:
                flow = self.dfs(source, sink, float('inf'), level, flow_graph)
                
                if flow == 0:
                    break
                
                max_flow += flow
        
        return max_flow