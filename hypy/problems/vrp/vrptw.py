"""VRPTW Components."""


from typing import Optional

from hypy.base import BaseProblem
from hypy.problems.vrp.base_components import Customer, Depot, Vehicle


class VRPTWProblem(BaseProblem):
    """_summary_.

    :param BaseProblem: _description_
    :type BaseProblem: _type_
    """

    def __init__(
        self,
        depot: Optional[Depot] = None,
        vehicles: Optional[list[Vehicle]] = None,
        customers: Optional[list[Customer]] = None,
    ) -> None:
        """_summary_.

        :param depot: _description_, defaults to None
        :type depot: Optional[Depot], optional
        :param vehicles: _description_, defaults to None
        :type vehicles: Optional[list[Vehicle]], optional
        :param customers: _description_, defaults to None
        :type customers: Optional[list[Customer]], optional
        """
        super().__init__()
        self.depot = depot
        self.vehicles = vehicles
        self.customers = customers

    def load_problem(self) -> None:
        """_summary_.

        :raises NotImplementedError: _description_
        """
        raise NotImplementedError
