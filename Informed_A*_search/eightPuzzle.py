from informedSearch import *

from informedSearch import *

import time


class EightPuzzle(InformedProblemState):
    """
    Implement this
    """

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.blank_pos = self.puzzle.index(" ")

    def __str__(self):
        puzzle_str = ""
        for i in range(0, 9, 3):
            puzzle_str += " ".join(str(tile) if tile != " " else " " for tile in self.puzzle[i:i + 3]) + "\n"
        return puzzle_str

    def move_blank_up(self):
        """
        moves the blank tile up by replacing it with the tile above- IF POSSIBLE
        """
        puzzle = self.puzzle[:]
        blk_pos = self.blank_pos

        if blk_pos > 2:
            rep_val = puzzle[blk_pos - 3]  # value of the cell to be replaced
            puzzle[blk_pos - 3] = " "
            puzzle[blk_pos] = rep_val

            return EightPuzzle(puzzle)

        return self

    def move_blank_down(self):
        """
        moves the blank tile down by replacing it with the tile below- IF POSSIBLE
        """
        puzzle = self.puzzle[:]
        blk_pos = self.blank_pos

        if blk_pos < 6:
            rep_val = puzzle[blk_pos + 3]
            puzzle[blk_pos + 3] = " "
            puzzle[blk_pos] = rep_val

            return EightPuzzle(puzzle)

        return self

    def move_blank_l(self):
        """
        swap the tile with the left tile- IF POSSIBLE
        """
        puzzle = self.puzzle[:]
        blk_pos = self.blank_pos

        if blk_pos % 3 != 0:
            rep_val = puzzle[blk_pos - 1]
            puzzle[blk_pos - 1] = " "
            puzzle[blk_pos] = rep_val

            return EightPuzzle(puzzle)

        return self

    def move_blank_r(self):
        """
        swap the tile with the right tile- IF POSSIBLE
        """
        puzzle = self.puzzle[:]
        blk_pos = self.blank_pos

        if blk_pos % 3 != 2:
            rep_val = puzzle[blk_pos + 1]
            puzzle[blk_pos + 1] = " "
            puzzle[blk_pos] = rep_val

            return EightPuzzle(puzzle)

        return self

    def equals(self, state):
        """
        Tests whether the state instance equals the given state.
        """
        return self.puzzle == state.puzzle

    def dictkey(self):
        """
        Returns a tuple that can be used as a dictionary key to
        represent unique states.
        """
        return tuple(self.puzzle)

    def heuristic(self, goal_state):
        """
        Calculate the heuristic value for the current state. Contains two different heuristics
        """
        # Heuristic 1: Tiles out of place
        tiles_out_of_place = sum(1 for a, b in zip(self.puzzle, goal_state.puzzle) if a != b)

        # Heuristic 2: Manhattan distance
        manhattan_distance = 0
        goal_positions = {}

        for i, tile in enumerate(goal_state.puzzle):
            if tile != " ":
                goal_positions[tile] = (i // 3, i % 3)

        for i, tile in enumerate(self.puzzle):
            if tile != " ":
                current_position = (i // 3, i % 3)
                goal_position = goal_positions[tile]
                manhattan_distance += abs(current_position[0] - goal_position[0]) + abs(
                    current_position[1] - goal_position[1])

        # return tiles_out_of_place  # use when running the tiles out of place method
        return manhattan_distance  # use when running the manhattan distance method

    def applyOperators(self):

        states = [self.move_blank_up(), self.move_blank_down(), self.move_blank_l(), self.move_blank_r()]

        return states


if __name__ == "__main__":
    start = time.time()       # starting the timer to calculate the running time

    # Tests in the README.md

    initial_state = [" ", "1", "3", "8", "2", "4", "7", "6", "5"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest A Completed \n\n")

    initial_state = ["1", "3", "4", "8", "6", "2", " ", "7", "5"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest B Completed \n\n")

    initial_state = ["1", "3", " ", "4", "2", "5", "8", "7", "6"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest C Completed \n\n")

    initial_state = ["7", "1", "2", "8", " ", "3", "6", "5", "4"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest D Completed \n\n")

    initial_state = ["8", "1", "2", "7", " ", "4", "6", "5", "3"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest E Completed \n\n")

    initial_state = ["2", "6", "3", "4", " ", "5", "1", "8", "7"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\n Test F Completed  \n\n")

    initial_state = ["7", "3", "4", "6", "1", "5", "8", " ", "2"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest G Completed \n\n")

    initial_state = ["7", "4", "5", "6", " ", "3", "8", "1", "2"]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state), True)
    print("\nTest H Completed \n\n")

    end = time.time()        # ending the timer to calculate the running time
    print("Time: ", end - start)
