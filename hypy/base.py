"""Base Module."""
from hypy.jit_compilation_config import jit_compile


class Solution:
    """Base Solution Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


# @jit_compile
class Problem:
    """Base Problem Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass

    def load_problem(self, file_name: str) -> None:
        """Method to load a problem.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def evaluate_solution(self, solution: Solution) -> None:
        """_summary_.

        Args:
            solution (Solution): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def is_feasible(self, solution: Solution) -> bool:
        """_summary_.

        Args:
            solution (Solution): _description_

        Raises:
            NotImplementedError: _description_

        Returns:
            bool: _description_
        """
        raise NotImplementedError

    def get_feasible_neighborhood(self, solution: Solution):
        """_summary_.

        Args:
            solution (Solution): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


class Solver:
    name: str
    description: str

    def __init__(self, name: str, description: str):
        """_summary_.

        Args:
            name (str): _description_
            description (str): _description_
        """
        self.name = name
        self.description = description

    def initialize(self) -> None:
        """_summary_.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def solve(self, problem: Problem) -> Solution:
        """_summary_.

        Args:
            problem (Problem): _description_

        Raises:
            NotImplementedError: _description_

        Returns:
            Solution: _description_
        """
        raise NotImplementedError

    def run(self) -> Solution:
        """_summary_.

        Returns:
            Solution: _description_
        """
        self.initialize()
        problem: Problem = Problem()
        solution: Solution = self.solve(problem)
        return solution


class Heuristic:
    """Base Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


class HyperHeuristic:
    """Base Hyper-Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


class MetaHeuristic:
    """Base Meta-Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass
