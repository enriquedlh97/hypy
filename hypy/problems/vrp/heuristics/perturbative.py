"""Perturbative VRP Heuristics."""

from hypy.problems.vrp.base_components import VRPHeuristic


class IntrarouteRelocate(VRPHeuristic):
    """_summary_.

    :param VRPHeuristic: _description_
    :type VRPHeuristic: _type_
    """

    def __init__(self) -> None:
        """_summary_."""
        super().__init__()
