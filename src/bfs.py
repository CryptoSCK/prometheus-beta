from collections import deque
from typing import Dict, List, Set, Any, Optional

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search (BFS) on a graph.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph.
        start (Any): Starting node for the BFS traversal.

    Returns:
        List[Any]: Nodes visited in BFS order.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid adjacency list.
    """
    # Validate input graph
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary (adjacency list)")
    
    # Check if start node exists in graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Initialize visited set and queue
    visited: Set[Any] = set()
    queue = deque([start])
    traversal_order: List[Any] = []
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Skip if already visited
        if current in visited:
            continue
        
        # Mark as visited and add to traversal order
        visited.add(current)
        traversal_order.append(current)
        
        # Add unvisited neighbors to queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return traversal_order