from eightPuzzle import *

if __name__ == "__main__":
    initial_state = ["1", "3", "4", "8", "6", "2", "7", "5", " "]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state))
    print("\nTest I Completed \n\n")                    |

    initial_state = ["5", "2", "3", "4", "1", "6", "7", "8", " "]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state))
    print("\nTest K Completed \n\n")

    initial_state = ["2", "3", "5", "1", "6", "4", "7", "8", " "]
    goal_state = ["1", "2", "3", "8", " ", "4", "7", "6", "5"]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state))
    print("\nTest L Completed \n\n")

    "******************************************************************"
    """ Different goal state"""
    initial_state = ["2", "3", "5", "1", "6", "4", "7", "8", " "]
    goal_state = ["1", "2", "3", "4", "5", "6", "7", "8", " "]
    InformedSearch(EightPuzzle(initial_state), EightPuzzle(goal_state))
    print("\nTest M Completed \n\n")

    # ^ BAD TEST: SEARCH FAILED
