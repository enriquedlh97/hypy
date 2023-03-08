"""VRP Base Components Module.

This module allows the user to make basic operations with the base
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

import os

if os.environ.get("GLOBAL_NAME") is None:
    os.environ["GLOBAL_NAME"] = "hypy.problems.vrp.components"


from typing import List

import numba
import numpy as np

from hypy.base import Heuristic, Problem, Solution
from hypy.jitclass_compilation import jit_compile

MODULE_NAME = "hypy.problems.vrp.components"


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class Location:
    """VRP Element 2-Dimensional Location Class."""

    coordinates: numba.float64[:]

    def __init__(self, coordinates: np.float64 | numba.float64[:]) -> None:
        """Class Constructor.

        Args:
            coordinates: _description_

        Raises:
            LocationCoordinatesError: _description_
            LocationCoordinatesError: _description_
            LocationCoordinatesError: _description_
        """

        self.coordinates = coordinates

    def __sub__(self, location: Location) -> Location:
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
        return Location(self.coordinates - location.coordinates)

    def __add__(self, location: Location) -> Location:
        """Addition Method.

        Args:
            location: _description_

        Returns:
            _description_
        """
        return Location(self.coordinates + location.coordinates)


# Here the '@jit_compile' decorator is omitted because more classes are
# subclassed from this one in the current file. This is because
# 'jitclass' does not support subclassing.
class VRPElement:
    """VRP Base Element Class."""

    location: Location

    def __init__(self, location: Location) -> None:
        """Class Constructor.

        Args:
            location: _description_

        Raises:
            TypeError: _description_
        """
        self.location = location

    def compute_distance(self, element: VRPElement) -> np.float64:
        """Computes distance between current object an another VRP element.

        Args:
            element: _description_

        Returns:
            _description_
        """
        if self.location.coordinates.size != element.location.coordinates.size:
            raise ValueError(
                "Both elements must have locations of the same dimensions"
            )

        return self.distance_op(element.location)

    def distance_op(self, location: Location) -> np.float64:
        """Defines the distance operation. Defaults to euclidean distance.

        Args:
            location: _description_

        Returns:
            _description_
        """
        return np.linalg.norm((self.location - location).coordinates, ord=2)


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class Customer(VRPElement):
    """VRP Customer Class."""

    __init__VRPElement = VRPElement.__init__
    demand: numba.float64
    location: Location

    def __init__(
        self, demand: np.float64 | numba.float64, location: Location
    ) -> None:
        """Class Constructor.

        Args:
            location: _description_
            demand: _description_
        """
        self.__init__VRPElement(location)
        self.demand = demand


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class Vehicle(VRPElement):
    """VRP Vehicle Class."""

    __init__VRPElement = VRPElement.__init__
    capacity: numba.float64
    location: Location

    def __init__(
        self, capacity: np.float64 | numba.float64, location: Location
    ) -> None:
        """Class Constructor.

        Args:
            location: _description_
            capacity: _description_
        """
        self.__init__VRPElement
        self.capacity = capacity
        self.location = location


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class Depot(VRPElement):
    """VRP Depot Class."""

    __init__VRPElement = VRPElement.__init__
    location: Location

    def __init__(self, location: Location) -> None:
        """Class Constructor.

        Args:
            location: _description_
        """
        self.__init__VRPElement
        self.location = location


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class Route:
    """VRP Route Class."""

    vehicle: Vehicle
    route: List[Customer]

    def __init__(self, vehicle: Vehicle, route: list[Customer]) -> None:
        """Class Constructor.

        Args:
            vehicle: _description_
            route: _description_. Defaults to [].
        """
        self.vehicle = vehicle
        self.route = route

    def __len__(self) -> int:
        """Length ob object method.

        Returns:
            _description_
        """
        return len(self.route)


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class VRPSolution(Solution):
    """VRP Solution Class."""

    __init__Solution = VRPElement.__init__
    routes: List[Route]

    def __init__(self, routes: list[Route]) -> None:
        """Class Constructor.

        Args:
            routes: _description_
        """
        self.__init__Solution
        self.routes = routes

    def __len__(self) -> int:
        """_summary_.

        Returns:
            int: _description_
        """
        return len(self.routes)


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class VRP(Problem):
    """VRP Problem Class."""

    __init__Problem = Problem.__init__
    depots: List[Depot]
    customers: List[Customer]
    vehicles: List[Vehicle]

    def __init__(
        self,
        depots: List[Depot],
        customers: List[Customer],
        vehicles: List[Vehicle],
    ) -> None:
        """Class Constructor.

        Args:
            depot: _description_
            customers: _description_
            vehicles: _description_
        """
        self.__init__Problem
        self.depots = depots
        self.customers = customers
        self.vehicles = vehicles


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class VRPHeuristic(Heuristic):
    """VRP Heuristic Class."""

    def __init__(self) -> None:
        """Class Constructor."""
        super().__init__()

    def apply(self, solution: Solution) -> Solution:
        """_summary_.

        Args:
            solution (Solution): _description_

        Raises:
            NotImplementedError: _description_

        Returns:
            Solution: _description_
        """
        raise NotImplementedError
