from pq import *
from improvedSearch import *


class InformedProblemState(ProblemState):
    """
    An interface class for problem domains. Inherits the ProblemState from improvedSearch.py.
    """

    def heuristic(self, goal_state):
        """
        Takes the goal state as a parameter and returns the estimate of
        the distance from the current state to the goal state.
        """
        abstract()


class InformedNode(Node):
    """
    InformedNode class that inherits from the Node class.
    """

    def __init__(self, state, parent, depth, goal_state):
        """
        Initialize the InformedNode with the current state, parent node, depth, and goal state.
        """
        super().__init__(state, parent, depth)
        self.goal_state = goal_state

    def __str__(self):
        """
        Return a string representation of the current search node.
        """
        result = "\nState:\n" + str(self.state)
        result += "\nDepth: " + str(self.depth)
        if self.parent is not None:
            result += "\nParent:\n" + str(self.parent.state)
        return result

    def priority(self):
        """
        Calculate the node's F value for A*. Priority is F(state) = G(state) + H(state).
        """
        g = self.depth  # Depth represents the cost from the root to this node.
        h = self.state.heuristic(self.goal_state)  # Use the heuristic to estimate the cost to reach the goal state.
        f = g + h
        return f


class InformedSearch(ImprovedSearch):
    """
    InformedSearch class that inherits from ImprovedSearch class.
    """

    def __init__(self, initialState, goalState, verbose=False):
        super().__init__(initialState, goalState, verbose)
        self.q = PriorityQueue()
        self.q.enqueue(InformedNode(initialState, None, 0, goalState))
        self.goalState = goalState
        self.verbose = verbose
        self.node_count = 0
        self.visited_states = {}  # Dictionary to store visited states
        solution = self.execute()

        if solution is None:
            print("Search failed")
        else:
            self.showPath(solution)

    def execute(self):
        while not self.q.empty():
            current = self.q.dequeue()
            self.node_count += 1

            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()

                for nextState in successors:
                    # Check if the state has not been visited before
                    if nextState.dictkey() not in self.visited_states:
                        n = InformedNode(nextState, current, current.depth + 1, self.goalState)
                        self.q.enqueue(n)
                        # Mark the state as visited
                        self.visited_states[nextState.dictkey()] = True
                        if self.verbose:
                            print("Expanded:", current)
                            print("Number of successors:", len(successors))
                            print("Queue length:", self.q.size())
                            print("Node Count:", self.node_count)
                            print("-------------------------------")
        return None
