from typing import List, Optional, Tuple

class KnightsTour:
    """
    A class to solve the Knight's Tour problem on an 8x8 chessboard.
    
    The Knight's Tour is a sequence of moves by a knight on a chessboard 
    where the knight visits every square exactly once.
    """
    
    def __init__(self, board_size: int = 8):
        """
        Initialize the Knight's Tour solver.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def is_valid_move(self, x: int, y: int, board: List[List[int]]) -> bool:
        """
        Check if a move is valid on the board.
        
        :param x: x-coordinate of the move
        :param y: y-coordinate of the move
        :param board: Current state of the board
        :return: True if the move is valid, False otherwise
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)
    
    def solve(self, start_x: int, start_y: int) -> Optional[List[Tuple[int, int]]]:
        """
        Solve the Knight's Tour problem starting from a given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: A list of moves representing the tour, or None if no solution exists
        """
        # Validate input
        if not (0 <= start_x < self.board_size and 0 <= start_y < self.board_size):
            raise ValueError(f"Start position must be within {self.board_size}x{self.board_size} board")
        
        # Initialize the board
        board = [[-1] * self.board_size for _ in range(self.board_size)]
        move_sequence = []
        
        def backtrack(x: int, y: int, move_count: int) -> bool:
            """
            Recursive backtracking algorithm to find the Knight's Tour.
            
            :param x: Current x-coordinate
            :param y: Current y-coordinate
            :param move_count: Number of moves made so far
            :return: True if a complete tour is found, False otherwise
            """
            # Mark current square as visited
            board[x][y] = move_count
            move_sequence.append((x, y))
            
            # If all squares are visited, we found a solution
            if move_count == self.board_size * self.board_size - 1:
                return True
            
            # Try all possible knight moves
            for dx, dy in self.directions:
                next_x, next_y = x + dx, y + dy
                
                # Check if the next move is valid
                if self.is_valid_move(next_x, next_y, board):
                    # Recursively try this move
                    if backtrack(next_x, next_y, move_count + 1):
                        return True
            
            # Backtrack: unmark the current square if no solution found
            board[x][y] = -1
            move_sequence.pop()
            return False
        
        # Start the tour from the given position
        if backtrack(start_x, start_y, 0):
            return move_sequence
        
        # No solution found
        return None