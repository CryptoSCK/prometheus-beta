import heapq
from typing import Dict, List, Optional, Tuple

def johnsons_algorithm(graph: Dict[int, Dict[int, int]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm for finding shortest paths between all pairs of vertices.
    
    Johnson's algorithm combines Bellman-Ford and Dijkstra's algorithms to find 
    shortest paths in a weighted graph, even with negative edge weights (but no negative cycles).
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph
                                           where graph[u][v] is the weight of edge from u to v
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: Dictionary of shortest paths between all pairs of vertices
                                             None if a negative cycle is detected
    
    Raises:
        ValueError: If the graph is empty
    """
    # Check for empty graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Add a new vertex connected to all other vertices with zero-weight edges
    vertices = list(graph.keys())
    dummy_vertex = max(vertices) + 1 if vertices else 0
    graph[dummy_vertex] = {v: 0 for v in vertices}
    
    # Step 1: Bellman-Ford to reweight edges
    reweighting = bellman_ford(graph, dummy_vertex)
    if reweighting is None:
        return None  # Negative cycle detected
    
    # Remove the dummy vertex
    del graph[dummy_vertex]
    
    # Step 2: Reweight the graph
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v, weight in graph[u].items():
            reweighted_graph[u][v] = weight + reweighting[u] - reweighting[v]
    
    # Step 3: Dijkstra's algorithm for each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = dijkstra(reweighted_graph, source, reweighting)
    
    return shortest_paths

def bellman_ford(graph: Dict[int, Dict[int, int]], source: int) -> Optional[Dict[int, int]]:
    """
    Bellman-Ford algorithm to find shortest paths and detect negative cycles.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Graph represented as adjacency list
        source (int): Source vertex
    
    Returns:
        Optional[Dict[int, int]]: Shortest path distances from source, or None if negative cycle exists
    """
    # Initialize distances
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        relaxed = False
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    relaxed = True
        
        # If no relaxation occurred, we can stop early
        if not relaxed:
            break
    
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None  # Negative cycle detected
    
    return distances

def dijkstra(graph: Dict[int, Dict[int, int]], source: int, 
              reweighting: Dict[int, int]) -> Dict[int, int]:
    """
    Dijkstra's algorithm for shortest paths with reweighting.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Reweighted graph
        source (int): Source vertex
        reweighting (Dict[int, int]): Original vertex weights for correction
    
    Returns:
        Dict[int, int]: Shortest path distances from source
    """
    # Priority queue for Dijkstra's algorithm
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    
    pq = [(0, source)]
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_distance > distances[u]:
            continue
        
        # Check all neighbors
        for v, weight in graph[u].items():
            # Compute distance and correct for reweighting
            distance = current_distance + weight
            corrected_distance = distance + reweighting[v] - reweighting[u]
            
            # Update if shorter path found
            if corrected_distance < distances[v]:
                distances[v] = corrected_distance
                heapq.heappush(pq, (corrected_distance, v))
    
    return distances