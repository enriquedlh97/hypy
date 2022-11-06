"""VRP Base Components Module."""


from __future__ import annotations

import numpy as np
import numpy.typing as npt

from hypy.base import BaseHeuristic, BaseProblem, BaseSolution
from hypy.problems.vrp.exceptions import LocationCoordinatesError


class Location:
    """VRP Element Location Class."""

    def __init__(self, coordinates: npt.NDArray[np.float_]) -> None:
        """Class Constructor.

        Args:
            coordinates (npt.NDArray[np.float_]): _description_

        Raises:
            LocationCoordinatesError: _description_
            LocationCoordinatesError: _description_
            LocationCoordinatesError: _description_
        """
        if not isinstance(coordinates, np.ndarray):
            raise LocationCoordinatesError(coordinates_type=type(coordinates))

        if len(coordinates.shape) > 1:
            raise LocationCoordinatesError(shape=coordinates.shape[1])  # type: ignore  # noqa: E501

        if coordinates.size == 0:
            raise LocationCoordinatesError(size=coordinates.size)

        self.coordinates = coordinates

    def __sub__(self, location: Location) -> np.float_ | np.int_:
        """Subtraction Method.

        Args:
            location (Location): _description_

        Returns:
            np.float_ | np.int_: _description_
        """
        return self.coordinates - location.coordinates  # type: ignore

    def __add__(self, location: Location) -> np.float_ | np.int_:
        """Addition Method.

        Args:
            location (Location): _description_

        Returns:
            np.float_ | np.int_: _description_
        """
        return self.coordinates + location.coordinates  # type: ignore


class BaseElement:
    """VRP Base Element Class."""

    def __init__(self, location: Location) -> None:
        """Class Constructor.

        Args:
            location (Location): _description_

        Raises:
            TypeError: _description_
        """
        if isinstance(location, Location):
            self.location = location
        else:
            raise TypeError(
                f"Location must be of type {Location}, not {type(location)}"
            )

    def compute_distance(self, element: BaseElement) -> np.float_:
        """Computes distance between current object an another VRP element.

        Args:
            element (BaseElement): _description_

        Returns:
            np.float_: _description_
        """
        # TODO: Check Location types are the same, same dimensions, etc.
        return self.distance_op(element.location)

    def distance_op(self, location: Location) -> np.float_:
        """Defines the distance operation. Defaults to euclidean distance.

        Args:
            location (Location): _description_

        Returns:
            np.float_: _description_
        """
        return np.linalg.norm(self.location - location, ord=2)


class Customer(BaseElement):
    """VRP Customer Class."""

    def __init__(self, location: Location, demand: float | int) -> None:
        """Class Constructor.

        Args:
            location (Location): _description_
            demand (float | int): _description_
        """
        super().__init__(location)
        self.demand = demand


class Vehicle(BaseElement):
    """VRP Vehicle Class."""

    def __init__(self, location: Location, capacity: float | int) -> None:
        """Class Constructor.

        Args:
            location (Location): _description_
            capacity (float | int): _description_
        """
        super().__init__(location)
        self.capacity = capacity


class Depot(BaseElement):
    """VRP Depot Class."""

    def __init__(self, location: Location) -> None:
        """Class Constructor.

        Args:
            location (Location): _description_
        """
        super().__init__(location)


class Route:
    """VRP Route Class."""

    def __init__(self, vehicle: Vehicle, route: list[Customer]) -> None:
        """Class Constructor.

        Args:
            vehicle (Vehicle): _description_
            route (list[Customer]): _description_
        """
        self.vehicle = vehicle
        self.route = route

    def __len__(self):
        """Length ob object method.

        Returns:
            _type_: _description_
        """
        return len(self.route)


class Solution(BaseSolution):
    """VRP Solution Class."""

    def __init__(self, routes: list[Route]) -> None:
        """Class Constructor.

        Args:
            routes (list[Route]): _description_
        """
        self.routes = routes


class VRPProblem(BaseProblem):
    """VRP Problem Class."""

    def __init__(
        self,
        depot: list[Depot],
        customers: list[Customer],
        vehicles: list[Vehicle],
    ) -> None:
        """Class Constructor.

        Args:
            depot (list[Depot]): _description_
            customers (list[Customer]): _description_
            vehicles (list[Vehicle]): _description_
        """
        super().__init__()
        self.depot = depot
        self.customers = customers
        self.vehicles = vehicles


class VRPHeuristic(BaseHeuristic):
    """VRP Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        super().__init__()
