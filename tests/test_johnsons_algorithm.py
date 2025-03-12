import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from johnsons_algorithm import johnsons_algorithm, bellman_ford, dijkstra

def test_empty_graph():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        johnsons_algorithm({})

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = {0: {}}
    result = johnsons_algorithm(graph)
    assert result == {0: {0: 0}}

def test_simple_positive_graph():
    """Test a simple graph with positive edge weights"""
    graph = {
        0: {1: 5, 2: 2},
        1: {2: 1},
        2: {1: -3}
    }
    result = johnsons_algorithm(graph)
    
    # Verify specific path lengths
    assert result[0][1] == 4  # 0 -> 2 -> 1 = 2 + (-3) = 4
    assert result[0][2] == 2  # direct path 0 -> 2
    assert result[1][2] == -2  # 1 -> 2

def test_graph_with_negative_edges():
    """Test a graph with negative edge weights"""
    graph = {
        0: {1: -1, 2: 4},
        1: {2: 3, 3: 2},
        2: {3: 5},
        3: {}
    }
    result = johnsons_algorithm(graph)
    
    # Verify specific path lengths
    assert result[0][3] == 1  # 0 -> 1 -> 3 = -1 + 2 = 1
    assert result[0][2] == 2  # 0 -> 1 -> 2 = -1 + 3 = 2

def test_bellman_ford_negative_cycle():
    """Test Bellman-Ford detects negative cycles"""
    graph = {
        0: {1: -1},
        1: {2: -2},
        2: {0: -3}
    }
    result = bellman_ford(graph, 0)
    assert result is None

def test_dijkstra_basic():
    """Test Dijkstra's algorithm with reweighting"""
    graph = {
        0: {1: 5, 2: 2},
        1: {2: 1},
        2: {1: -3}
    }
    # Create a fake reweighting dict to simulate the correction
    reweighting = {0: 0, 1: 0, 2: 0}
    result = dijkstra(graph, 0, reweighting)
    
    assert result[1] == 3  # 0 -> 2 (2) -> 1 (-3) = 3
    assert result[2] == 2  # direct path 0 -> 2

def test_complex_graph():
    """Test a more complex graph with various edge weights"""
    graph = {
        0: {1: 3, 2: 6},
        1: {2: 2, 3: 4},
        2: {3: 1, 4: 5},
        3: {4: 2},
        4: {}
    }
    result = johnsons_algorithm(graph)
    
    # Additional checks for more complex path finding
    assert result[0][4] == 8  # Verify total path length from 0 to 4
    assert result[1][4] == 5  # Verify total path length from 1 to 4
    assert result[2][4] == 3  # Verify total path length from 2 to 4

def test_cyclic_graph():
    """Test a graph with cycles"""
    graph = {
        0: {1: 1, 2: 2},
        1: {2: 1, 3: 3},
        2: {3: 1},
        3: {0: -6}
    }
    # This tests handling of cycles without negative cycle
    result = johnsons_algorithm(graph)
    assert result is not None  # Ensure no negative cycle is detected