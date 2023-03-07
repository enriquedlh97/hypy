"""Perturbative VRP Heuristics."""

from copy import deepcopy
from random import randint, shuffle

from hypy.problems.vrp.components import VRPHeuristic
from hypy.problems.vrp.exceptions import (
    EmptySolutionError,
    NotEnoughCustomersError,
)
from hypy.problems.vrp.vrptw.components import (
    VRPTWCustomer,
    VRPTWRoute,
    VRPTWSolution,
)


class IntrarouteRelocate(VRPHeuristic):
    """VRP Intraroute Relocate Class."""

    def __init__(self) -> None:
        """Constructor Method."""
        super().__init__()

    def apply(self, solution: VRPTWSolution) -> VRPTWSolution:
        if len(solution) > 0:
            # Select a random route from the solution
            route: VRPTWRoute = solution.routes[randint(0, len(solution) - 1)]
            if len(route) > 1:
                # Select a customer from a random position in the route
                currrent_position: int = randint(0, len(route) - 1)
                new_position: int = self.get_factible_relocate_position(
                    currrent_position, deepcopy(route)
                )
            else:
                raise NotEnoughCustomersError(route, min_required=2)
        else:
            raise EmptySolutionError

        return solution

    @staticmethod
    def get_factible_relocate_position(
        current_position: int, route: VRPTWRoute
    ) -> int:
        current_customer: VRPTWCustomer = route.route[current_position + 1]
        route.remove(current_position + 1, 1)
        all_positions = list(range(len(route) + 1))
        del all_positions[current_position]
        shuffle(all_positions)
        for position in all_positions:
            if VRPTWRoute.validate_route_insertion(
                current_customer, position, deepcopy(route)
            ):
                return position
        return -1
