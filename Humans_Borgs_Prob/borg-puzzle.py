from search import *
from improvedSearch import *

import time


class BorgState(ProblemState):
    """
    Represents the state of the Borgs and Humans crossing a river problem.

    This class defines the state of the problem, which includes the number of humans and borgs on both banks
    of the river and the location of the boat. It implements the ProblemState interface.

    Attributes:
        humans_left (int): The number of humans on the left bank.
        borg_left (int): The number of borgs on the left bank.
        boat_on_left_bank (bool): Indicates whether the boat is on the left bank.

    Methods:
        __init__(self, humans_left, borg_left, boat_on_left_bank):
            Initializes a new state with the given parameters.

        __str__(self):
            Returns a string representation of the state, including the boat's position and the number of humans
            and borgs on both banks.
    """
    def __init__(self, humans_left, borg_left, boat_on_left_bank):
        """
        Initializes a new state of the problem.

        Args:
            humans_left (int): The number of humans on the left bank.
            borg_left (int): The number of borgs on the left bank.
            boat_on_left_bank (bool): Indicates whether the boat is on the left bank.
        """
        self.total_humans = 3
        self.total_borgs = 3

        self.humans_left = humans_left

        self.borg_left = borg_left

        self.boat_on_left_bank = boat_on_left_bank

    def __str__(self):
        """
        Creates a string representation of the state.

        The string includes information about the boat's position and the number of humans and borgs on both banks
        of the river.

        Returns:
            str: A string representation of the state.
        """
        return (
                "Is boat on left bank: " + str(self.boat_on_left_bank) + "\n"
                                                                         "Humans on the left bank: " + str(
            self.humans_left) + ", " + "Borgs on the left bank: " + str(self.borg_left) + "\n"
                                                                                          "Humans on the right bank: " + str(
            self.total_humans - self.humans_left) + ", " + "Borgs on the right bank: " + str(
            self.total_borgs - self.borg_left)
        )

    def equals(self, state):
        """
        the following function checks if the goal state is reached
        """
        return (
                self.humans_left == state.humans_left
                and self.borg_left == state.borg_left
                and self.boat_on_left_bank == state.boat_on_left_bank
        )

    def dictkey(self):
        return f"{self.humans_left},{self.borg_left},{int(self.boat_on_left_bank)}"

    def is_good_number(self):
        """
        checks if moving to a certain state has a practically possible outcome
        """
        if (0 <= self.humans_left <= 3
                and 0 <= self.borg_left <= 3
                and 0 <= self.total_humans - self.humans_left <= 3
                and 0 <= self.total_borgs - self.borg_left <= 3):
            return True

        return False

    def is_valid(self):
        """
        check if the decision made fulfills the principal of maintaining the balance between humans and borgs
        that is making sure that borgs do not outnumber the humans
        """
        if self.is_good_number():
            if 0 < self.humans_left < self.borg_left:  # checking if the humans are less than borgs given that humans are on the left side
                return False
            elif 0 < self.total_humans - self.humans_left < self.total_borgs - self.borg_left:  # checking if the humans are less than borgs given that humans are on the right side
                return False
            return True
        return False

    def move_2humans(self):
        """
        move two humans from either end of the river to the other end
        """
        if self.boat_on_left_bank:
            humans_left = self.humans_left - 2
            boat_on_left_bank = False

        else:
            humans_left = self.humans_left + 2
            boat_on_left_bank = True

        return BorgState(humans_left, self.borg_left, boat_on_left_bank)

    def move_1humans(self):
        """
        move a human from either end of the river to the other end
        """
        if self.boat_on_left_bank:
            humans_left = self.humans_left - 1
            boat_on_left_bank = False

        else:
            humans_left = self.humans_left + 1
            boat_on_left_bank = True

        return BorgState(humans_left, self.borg_left, boat_on_left_bank)

    def move_2borgs(self):
        """
        move two borgs from either end of the river to the other end
        """
        if self.boat_on_left_bank:
            borg_left = self.borg_left - 2
            boat_on_left_bank = False

        else:
            borg_left = self.borg_left + 2
            boat_on_left_bank = True

        return BorgState(self.humans_left, borg_left, boat_on_left_bank)

    def move_1borgs(self):
        """
        move a borg from either end of the river to the other end
        """
        if self.boat_on_left_bank:
            borg_left = self.borg_left - 1
            boat_on_left_bank = False

        else:
            borg_left = self.borg_left + 1
            boat_on_left_bank = True

        return BorgState(self.humans_left, borg_left, boat_on_left_bank)

    def move_hum_borg(self):
        """
        move a human and a borg from either end of the river to the other end
        """
        if self.boat_on_left_bank:
            borg_left = self.borg_left - 1
            humans_left = self.humans_left - 1
            boat_on_left_bank = False

        else:
            borg_left = self.borg_left + 1
            humans_left = self.humans_left + 1
            boat_on_left_bank = True

        return BorgState(humans_left, borg_left, boat_on_left_bank)

    def applyOperators(self):
        """
        Generate and return a list of valid successor states by applying various operators.
        This function applies a set of predefined operators to the current state, resulting in a list of successor states.
        The operators include moving two borgs, moving one borg, moving a borg and a human, moving two humans, and moving one human.
        Returns:
        list: A list of valid successor states generated by applying the operators.
        Note:
        The validity of each successor state is determined using the 'is_valid()' method of the state objects.

        """
        states = [self.move_2borgs(), self.move_1borgs(), self.move_hum_borg(), self.move_2humans(),
                  self.move_1humans()]
        successor= []

        for state in states:
            if state.is_valid():
                successor.append(state)

        return successor


def search_borg_puzzle():
    """
    method that uses the `search.py` to achieve the goal state
    """
    start = time.time()
    Search(BorgState(3, 3, True), BorgState(0, 0, False), True)
    end = time.time()
    print("Time:", end - start)


def imp_search_borg_puzzle():
    """
    method that uses the `improvedSearch.py` to achieve the goal state
    """
    start = time.time()
    ImprovedSearch(BorgState(3, 3, True), BorgState(0, 0, False), True)
    end = time.time()
    print("Time:", end - start)


if __name__ == "__main__":
     # search_borg_puzzle()
     imp_search_borg_puzzle()
