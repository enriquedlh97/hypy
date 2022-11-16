"""Perturbative VRP Heuristics."""

from hypy.problems.vrp.components import VRPHeuristic


class IntrarouteRelocate(VRPHeuristic):
    """VRP Intraroute Relocate Class."""

    def __init__(self) -> None:
        """Constructor Method."""
        super().__init__()
