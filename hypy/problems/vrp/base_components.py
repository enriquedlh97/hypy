"""VRP Base Components."""


from __future__ import annotations

import numpy as np
import numpy.typing as npt

from hypy.base import BaseHeuristic, BaseProblem, BaseSolution
from hypy.problems.vrp.exceptions import LocationCoordinatesError


class Location:
    """_summary_."""

    def __init__(self, coordinates: npt.NDArray[np.float_]) -> None:
        """_summary_.

        :param coordinates: _description_
        :type coordinates: npt.NDArray[np.float_]
        :raises LocationCoordinatesError: _description_
        :raises LocationCoordinatesError: _description_
        :raises LocationCoordinatesError: _description_
        """
        if not isinstance(coordinates, np.ndarray):
            raise LocationCoordinatesError(coordinates_type=type(coordinates))

        if len(coordinates.shape) > 1:
            raise LocationCoordinatesError(shape=coordinates.shape[1])  # type: ignore  # noqa: E501

        if coordinates.size == 0:
            raise LocationCoordinatesError(size=coordinates.size)

        self.coordinates = coordinates

    def __sub__(self, location: Location) -> np.float_ | np.int_:
        """_summary_.

        :param location: _description_
        :type location: Location
        :return: _description_
        :rtype: np.float_ | np.int_
        """
        return self.coordinates - location.coordinates  # type: ignore

    def __add__(self, location: Location) -> np.float_ | np.int_:
        """_summary_.

        :param location: _description_
        :type location: Location
        :return: _description_
        :rtype: np.float_ | np.int_
        """
        return self.coordinates + location.coordinates  # type: ignore


class BaseElement:
    """_summary_."""

    def __init__(self, location: Location) -> None:
        """_summary_.

        :param location: _description_
        :type location: Location
        :raises TypeError: _description_
        """
        if isinstance(location, Location):
            self.location = location
        else:
            raise TypeError(
                f"Location must be of type {Location}, not {type(location)}"
            )

    def compute_distance(self, element: BaseElement) -> np.float_:
        """_summary_.

        :param element: _description_
        :type element: BaseElement
        :return: _description_
        :rtype: np.float_
        """
        # TODO: Check Location types are the same, same dimensions, etc.
        return self.distance_op(element.location)

    def distance_op(self, location: Location) -> np.float_:
        """_summary_.

        :param location: _description_
        :type location: Location
        :return: _description_
        :rtype: np.float_
        """
        return np.linalg.norm(self.location - location, ord=2)


class Customer(BaseElement):
    """_summary_.

    :param BaseElement: _description_
    :type BaseElement: _type_
    """

    def __init__(self, location: Location, demand: float | int) -> None:
        """_summary_.

        :param location: _description_
        :type location: Location
        :param demand: _description_
        :type demand: float | int
        """
        super().__init__(location)
        self.demand = demand


class Vehicle(BaseElement):
    """_summary_.

    :param BaseElement: _description_
    :type BaseElement: _type_
    """

    def __init__(self, location: Location, capacity: float | int) -> None:
        """_summary_.

        :param location: _description_
        :type location: Location
        :param capacity: _description_
        :type capacity: float | int
        """
        super().__init__(location)
        self.capacity = capacity


class Depot(BaseElement):
    """_summary_.

    :param BaseElement: _description_
    :type BaseElement: _type_
    """

    def __init__(self, location: Location) -> None:
        """_summary_.

        :param location: _description_
        :type location: Location
        """
        super().__init__(location)


class Route:
    """_summary_."""

    def __init__(self, vehicle: Vehicle, route: list[Customer]) -> None:
        """_summary_.

        :param vehicle: _description_
        :type vehicle: Vehicle
        :param route: _description_
        :type route: list[Customer]
        """
        self.vehicle = vehicle
        self.route = route

    def __len__(self):
        """_summary_.

        :return: _description_
        :rtype: _type_
        """
        return len(self.route)


class Solution(BaseSolution):
    """_summary_.

    :param BaseSolution: _description_
    :type BaseSolution: _type_
    """

    def __init__(self, routes: list[Route]) -> None:
        """_summary_.

        :param routes: _description_
        :type routes: list[Route]
        """
        self.routes = routes


class VRPProblem(BaseProblem):
    """_summary_.

    :param BaseProblem: _description_
    :type BaseProblem: _type_
    """

    def __init__(
        self, customers: list[Customer], vehicles: list[Vehicle]
    ) -> None:
        """_summary_.

        :param customers: _description_
        :type customers: list[Customer]
        :param vehicles: _description_
        :type vehicles: list[Vehicle]
        """
        super().__init__()
        self.customers = customers
        self.vehicles = vehicles


class VRPHeuristic(BaseHeuristic):
    """_summary_.

    :param BaseHeuristic: _description_
    :type BaseHeuristic: _type_
    """

    def __init__(self) -> None:
        """_summary_."""
        super().__init__()
