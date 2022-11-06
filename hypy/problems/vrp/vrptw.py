"""VRPTW Components Module."""


from hypy.problems.vrp.base_components import (
    Customer,
    Depot,
    Vehicle,
    VRPProblem,
)


class VRPTWProblem(VRPProblem):
    """VRPTW Problem Class."""

    def __init__(
        self,
        depot: list[Depot],
        customers: list[Customer],
        vehicles: list[Vehicle],
    ) -> None:
        """Class Constructor.

        Args:
            depot: _description_
            customers: _description_
            vehicles: _description_
        """
        super().__init__(depot, customers, vehicles)

    def load_problem(self) -> None:
        """Method to load a VRPTW problem.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
