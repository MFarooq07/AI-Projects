class Queue:
    """
    A Queue class to be used in combination with state space
    search. The enqueue method adds new elements to the end. The
    dequeue method removes elements from the front.
    """

    def __init__(self):
        """
        initializes the queue
        """
        self.queue = []

    def __str__(self):
        """
        this tells what's in the queue
        """
        result = "Queue contains " + str(len(self.queue)) + " items\n"
        for item in self.queue:
            result += str(item) + "\n"
        return result

    def enqueue(self, node):
        """
        this method adds a node to the queue
        """
        self.queue.append(node)

    def dequeue(self):
        """
        this method removes the first node in the queue
        """
        if not self.empty():
            return self.queue.pop(0)
        else:
            raise Exception

    def size(self):
        """
        this method helps in determining the number of nodes in the
        element
        """
        return len(self.queue)

    def empty(self):
        """
        this method lets you know if the queue is empty or not
        """
        return len(self.queue) == 0


class Node:
    """
    A Node class to be used in combination with state space search.  A
    node contains a state, a parent node, and the depth of the node in
    the search tree.  The root node should be at depth 0.
    """

    def __init__(self, state, parent, depth):
        """
        the current state
        the parent of the search
        the depth of the search
        """
        self.state = state
        self.parent = parent
        self.depth = depth

    def __str__(self):
        """
        prints out the current search
        """
        result = "\nState: " + str(self.state)
        result += "\nDepth: " + str(self.depth)
        if self.parent != None:
            result += "\nParent: " + str(self.parent.state)
        return result


class ImprovedSearch:
    """
    A modified search class that utilizes state visitation tracking to improve efficiency.

    This class is an enhanced version of the general search class. It applies a state visitation tracking mechanism
    to prevent revisiting previously explored states, reducing the number of nodes visited during the search.

    Attributes:
        initialState (ProblemState): The initial state of the search.
        goalState (ProblemState): The goal state to be reached.
        verbose (bool): If True, displays additional information during the search.
        q (Queue): The queue used for managing nodes.
        node_count (int): The count of nodes visited during the search.
        visited_states (dict): A dictionary to store visited states.

    """
    def __init__(self, initialState, goalState, verbose=False):
        """
        Initializes the improved search with the provided initial and goal states.

        Args:
            initialState (ProblemState): The initial state of the search.
            goalState (ProblemState): The goal state to be reached.
            verbose (bool, optional): If True, displays additional information during the search. Default is False.
        """
        self.q = Queue()
        self.q.enqueue(Node(initialState, None, 0))
        self.goalState = goalState
        self.verbose = verbose
        self.node_count = 0
        self.visited_states = {}  # Dictionary to store visited states
        solution = self.execute()
        if solution == None:
            print("Search failed")
        else:
            self.showPath(solution)

    def execute(self):
        """
        Executes the search using state visitation tracking to improve efficiency.

        Returns:
            Node or None: The goal node if found, None if the search fails.
        """
        while not self.q.empty():
            current = self.q.dequeue()
            self.node_count +=1
            print(self.q.size())
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()

                for nextState in successors:
                    # Check if the state has not been visited before
                    if nextState.dictkey() not in self.visited_states:
                        n = Node(nextState, current, current.depth + 1)
                        self.q.enqueue(n)
                        # Mark the state as visited
                        self.visited_states[nextState.dictkey()] = True
                        if self.verbose:
                            print("Expanded:", current)
                            print("Number of successors:", len(successors))
                            print("Queue length:", self.q.size())
                            print("Nodes visited:", self.node_count)
                            print("-------------------------------")
            print("\n")
        return None

    def showPath(self, node):
        """
        Displays the path from the initial state to the goal state.

        Args:
            node (Node): The goal node.
        """
        path = self.buildPath(node)
        for current in path:
            print(current.state)
        print("Goal reached in", current.depth, "steps")

    def buildPath(self, node):
        """
        Builds the path from the goal node to the start state.

        Args:
            node (Node): The goal node.

        Returns:
            list: A list of nodes representing the path.
        """
        result = []
        while node != None:
            result.insert(0, node)
            node = node.parent
        return result


class ProblemState:
    """
    An interface class for problem domains.
    """

    def __str__(self):
        """
        Returns a string representing the state.
        """
        abstract()

    def applyOperators(self):
        """
        Returns a list of valid successors to the current state.
        """
        abstract()

    def equals(self, state):
        """
        Tests whether the state instance equals the given state.
        """
        abstract()

    def dictkey(self):
        """
        Returns a string that can be used as a dictionary key to
        represent unique states.
        """
        abstract()
