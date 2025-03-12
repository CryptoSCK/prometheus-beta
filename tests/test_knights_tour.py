import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test the initialization of KnightsTour class."""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.directions) == 8

def test_is_valid_move():
    """Test the is_valid_move method."""
    kt = KnightsTour()
    board = [[-1] * 8 for _ in range(8)]
    
    # Valid move
    assert kt.is_valid_move(3, 4, board) == True
    
    # Out of bounds
    assert kt.is_valid_move(-1, 0, board) == False
    assert kt.is_valid_move(8, 8, board) == False
    
    # Already visited square
    board[3][4] = 1
    assert kt.is_valid_move(3, 4, board) == False

def test_solve_standard_start():
    """Test solving Knight's Tour from a standard starting position."""
    kt = KnightsTour()
    
    # Attempt to solve starting from different positions
    tours_to_test = [(0, 0), (3, 3), (7, 7)]
    
    for start_x, start_y in tours_to_test:
        tour = kt.solve(start_x, start_y)
        
        # Check basic tour properties
        assert tour is not None, f"No tour found starting from ({start_x}, {start_y})"
        assert len(tour) == 64, f"Tour should have 64 moves, got {len(tour)}"
        
        # Check all moves are unique
        assert len(set(tour)) == 64, "Tour should visit each square exactly once"
        
        # Check moves are valid knight moves
        for i in range(1, len(tour)):
            prev_x, prev_y = tour[i-1]
            curr_x, curr_y = tour[i]
            
            # Calculate move deltas
            dx = abs(curr_x - prev_x)
            dy = abs(curr_y - prev_y)
            
            # Verify knight move
            assert (dx == 1 and dy == 2) or (dx == 2 and dy == 1), \
                f"Invalid knight move from {tour[i-1]} to {tour[i]}"

def test_invalid_start_position():
    """Test that invalid start positions raise an error."""
    kt = KnightsTour()
    
    with pytest.raises(ValueError):
        kt.solve(-1, 0)
    
    with pytest.raises(ValueError):
        kt.solve(8, 8)

def test_no_solution_cases():
    """
    Note: A Knight's Tour always exists for 8x8 board when starting from any square.
    This function is a placeholder for potential future board size variations.
    """
    # For standard 8x8 board, a tour should always exist
    kt = KnightsTour()
    tour = kt.solve(3, 3)
    assert tour is not None