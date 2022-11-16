"""VRP Base Components Module.

This module allows the suer to make basic operations with the base
elements form a VRP problem.

Examples:
    >>> import numpy as np
    >>> from hypy.problems.vrp.base_components import Location
    >>> Location(np.array([2, 3, 4])) - Location(np.array([1, 2, 3]))
    array([1, 1, 1])
    >>> Location(np.array([5, 23, 7])) - Location(np.array([2, 20, 1]))
    array([3, 3, 6])
"""


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
            coordinates: _description_

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

        Examples:
            >>> import numpy as np
            >>> Location(np.array([2, 3, 4])) - Location(np.array([1, 2, 3]))
            array([1, 1, 1])
            >>> Location(np.array([5, 23, 7])) - Location(np.array([2, 20, 1]))
            array([3, 3, 6])

        Args:
            location: _description_

        Returns:
            _description_
        """
        return self.coordinates - location.coordinates  # type: ignore

    def __add__(self, location: Location) -> np.float_ | np.int_:
        """Addition Method.

        Args:
            location: _description_

        Returns:
            _description_
        """
        return self.coordinates + location.coordinates  # type: ignore

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return f"{self.__class__.__name__}( coordinates={self.coordinates} )"


class BaseElement:
    """VRP Base Element Class."""

    def __init__(self, location: Location | None = None) -> None:
        """Class Constructor.

        Args:
            location: _description_

        Raises:
            TypeError: _description_
        """
        if location is not None:
            if isinstance(location, Location):
                self.location = location
            else:
                raise TypeError(
                    f"Location must be of type {Location}, "
                    + f"not {type(location)}"
                )

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return f"{self.__class__.__name__}( location={self.location} )"

    def compute_distance(self, element: BaseElement) -> np.float_ | None:
        """Computes distance between current object an another VRP element.

        Args:
            element: _description_

        Returns:
            _description_
        """
        # TODO: Check Location types are the same, same dimensions, etc.
        if self.location is not None:
            return self.distance_op(element.location)
        else:
            return None

    def distance_op(self, location: Location) -> np.float_:
        """Defines the distance operation. Defaults to euclidean distance.

        Args:
            location: _description_

        Returns:
            _description_
        """
        return np.linalg.norm(self.location - location, ord=2)


class Customer(BaseElement):
    """VRP Customer Class."""

    def __init__(
        self, demand: float | int, location: Location | None = None
    ) -> None:
        """Class Constructor.

        Args:
            location: _description_
            demand: _description_
        """
        super().__init__(location)
        self.demand = demand

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( location={self.location}, "
            + f"demand={self.demand} )"
        )


class Vehicle(BaseElement):
    """VRP Vehicle Class."""

    def __init__(
        self, capacity: float | int, location: Location | None = None
    ) -> None:
        """Class Constructor.

        Args:
            location: _description_
            capacity: _description_
        """
        super().__init__(location)
        self.capacity = capacity

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( location={self.location}, "
            + f"capacity={self.capacity} )"
        )


class Depot(BaseElement):
    """VRP Depot Class."""

    def __init__(self, location: Location | None = None) -> None:
        """Class Constructor.

        Args:
            location: _description_
        """
        super().__init__(location)


class Route:
    """VRP Route Class."""

    def __init__(self, vehicle: Vehicle, route: list[Customer]) -> None:
        """Class Constructor.

        Args:
            vehicle: _description_
            route: _description_
        """
        self.vehicle = vehicle
        self.route = route

    def __len__(self):
        """Length ob object method.

        Returns:
            _description_
        """
        return len(self.route)

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( vehicle={self.vehicle}, "
            + f"route=[{len(self.route)} Customers] )"
        )


class Solution(BaseSolution):
    """VRP Solution Class."""

    def __init__(self, routes: list[Route]) -> None:
        """Class Constructor.

        Args:
            routes: _description_
        """
        self.routes = routes

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( routes=[{len(self.routes)} "
            + "Routes] )"
        )


class VRP(BaseProblem):
    """VRP Problem Class."""

    def __init__(
        self,
        depot: list[Depot] = [],
        customers: list[Customer] = [],
        vehicles: list[Vehicle] = [],
    ) -> None:
        """Class Constructor.

        Args:
            depot: _description_
            customers: _description_
            vehicles: _description_
        """
        super().__init__()
        self.depot = depot
        self.customers = customers
        self.vehicles = vehicles

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( depot=[{len(self.depot)} Depot], "
            + f"customers=[{len(self.customers)} "
            + "Customers], "
            + f"vehicles=[{len(self.vehicles)} Vehicles]"
        )


class VRPHeuristic(BaseHeuristic):
    """VRP Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        super().__init__()
