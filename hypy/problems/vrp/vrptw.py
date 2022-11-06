"""_summary_.

Raises:
    NotImplementedError: _description_
"""


from hypy.problems.vrp.base_components import (
    Customer,
    Depot,
    Vehicle,
    VRPProblem,
)


class VRPTWProblem(VRPProblem):
    """_summary_."""

    def __init__(
        self,
        depot: list[Depot],
        customers: list[Customer],
        vehicles: list[Vehicle],
    ) -> None:
        """_summary_.

        Args:
            depot (list[Depot]): _description_
            customers (list[Customer]): _description_
            vehicles (list[Vehicle]): _description_
        """
        super().__init__(depot, customers, vehicles)

    def load_problem(self) -> None:
        """_summary_.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
