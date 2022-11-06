"""Base Module."""


class BaseProblem:
    """Base Problem Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass

    def load_problem(self) -> None:
        """Method to load a problem.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


class BaseSolution:
    """Base Solution Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


class BaseHeuristic:
    """Base Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


class BaseHyperHeuristic:
    """Base Hyper-Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass


class BaseMetaHeuristic:
    """Base Meta-Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        pass
