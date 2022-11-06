"""Perturbative VRP Heuristics."""

from hypy.problems.vrp.base_components import VRPHeuristic


class IntrarouteRelocate(VRPHeuristic):
    """VRP Intraroute Relocate Class.

    Args:
        VRPHeuristic (_type_): _description_
    """

    def __init__(self) -> None:
        """Constructor Method."""
        super().__init__()
