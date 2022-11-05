"""Base Module."""


class BaseProblem:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        pass

    def load_problem(self) -> None:
        """_summary_.

        :raises NotImplementedError: _description_
        """
        raise NotImplementedError


class BaseSolution:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        pass


class BaseHeuristic:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        pass


class BaseHyperHeuristic:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        pass


class BaseMetaHeuristic:
    """_summary_."""

    def __init__(self) -> None:
        """_summary_."""
        pass
