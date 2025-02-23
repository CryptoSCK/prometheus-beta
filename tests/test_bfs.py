import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    """Test BFS on a simple connected graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F'] or result == ['A', 'C', 'B', 'F', 'D', 'E']

def test_single_node_graph():
    """Test BFS on a graph with a single node."""
    graph = {'A': []}
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A']

def test_disconnected_nodes():
    """Test BFS on a graph with disconnected nodes."""
    graph = {
        'A': [],
        'B': [],
        'C': []
    }
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A']

def test_error_start_node_not_in_graph():
    """Test that a ValueError is raised when start node is not in graph."""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search(graph, 'X')

def test_error_invalid_graph():
    """Test that a TypeError is raised for invalid graph input."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search([], 'A')  # List instead of dict
    
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search("not a graph", 'A')  # String instead of dict