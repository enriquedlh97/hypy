"""VRPTW Components Module."""


from __future__ import annotations

import os

# This has to stay here for proper jitclass compilation
if os.environ.get("GLOBAL_NAME") is None:
    os.environ["GLOBAL_NAME"] = "hypy.problems.vrp.vrptw.components"

import numba
import numpy as np
from numba.experimental import jitclass
from numba.experimental.jitclass.base import JitClassType

from hypy.jitclass_compilation import jit_compile
from hypy.problems.vrp.components import (  # VRP,;Route,;Solution,;Vehicle,
    Customer,
    Depot,
    Location,
)

# TODO: Add explanation
MODULE_NAME = "hypy.problems.vrp.vrptw.components"

# Make sure to be using the correct version of the objects 
# (jitted or not jitted)
if not isinstance(Location, type(JitClassType)):
    Location = jitclass(LocationVRPTW)

if isinstance(Customer, type(JitClassType)):
    Customer = Customer.__base__

# # @jit_compile
# class VRPTWCustomer(Customer):
#     """_summary_.

#     Args:
#         Customer: _description_
#     """

#     __init__Customer = Customer.__init__
#     id_number: numba.int64
#     demand: numba.float64
#     time_window: TimeWindow
#     location: Location

#     def __init__(
#         self,
#         id_number: np.int64 | numba.int64,
#         demand: np.float64 | numba.float64,
#         time_window: TimeWindow,
#         location: Location,
#     ) -> None:
#         """_summary_.

#         Args:
#             id_number: _description_
#             demand: _description_
#             time_window: _description_
#             location: _description_. Defaults to None.
#         """
#         self.__init__Customer(demand, location)
#         self.id_number = id_number
#         self.time_window = time_window


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class TimeWindow:
    """_summary_."""

    ready_time: numba.int64
    due_date: numba.int64
    service_duration: numba.int64

    def __init__(
        self,
        ready_time: np.int64 | numba.int64,
        due_date: np.int64 | numba.int64,
        service_duration: np.int64 | numba.int64,
    ) -> None:
        """_summary_.

        Args:
            ready_time (int): _description_
            due_date (int): _description_
            service_duration (int): _description_
        """
        self.ready_time = ready_time
        self.due_date = due_date
        self.service_duration = service_duration


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class VRPTWCustomer(Customer):
    """_summary_.

    Args:
        Customer: _description_
    """

    __init__Customer = Customer.__init__
    id_number: numba.int64
    demand: numba.float64
    time_window: TimeWindow
    location: Location

    def __init__(
        self,
        id_number: np.int64 | numba.int64,
        demand: np.float64 | numba.float64,
        time_window: TimeWindow,
        location: Location,
    ) -> None:
        """_summary_.

        Args:
            id_number: _description_
            demand: _description_
            time_window: _description_
            location: _description_. Defaults to None.
        """
        self.__init__Customer(demand, location)
        self.id_number = id_number
        self.time_window = time_window


@jit_compile(os.environ["GLOBAL_NAME"], MODULE_NAME)
class VRPTWDepot(Depot):
    """_summary_.

    Args:
        Depot (_type_): _description_
    """

    __init__Depot = Depot.__init__
    id_number: numba.int64
    time_window: TimeWindow
    location: Location

    def __init__(
        self,
        id_number: np.int64 | numba.int64,
        time_window: TimeWindow,
        location: Location,
    ) -> None:
        """_summary_.

        Args:
            id_number: _description_
            time_window: _description_
            location: _description_. Defaults to None.
        """
        self.__init__Depot(location)
        self.id_number = id_number
        self.time_window = time_window


# class VRPTWRoute(Route):
#     """_summary_.

#     Args:
#         Route (_type_): _description_
#     """

#     def __init__(self, vehicle: Vehicle, route: list[VRPTWCustomer]) -> None:
#         """_summary_.

#         Args:
#             vehicle (Vehicle): _description_
#             route (list[VRPTWCustomer]): _description_
#         """
#         super().__init__(vehicle)
#         self.route = route

#     def remove(
#         self, position: int, number_of_customers_to_delete: int
#     ) -> VRPTWRoute:
#         if position < 0 or position >= super().__len__():
#             raise NameError("Wrong remove position in the route.")
#         if position + number_of_customers_to_delete > super().__len__():
#             raise NotEnoughCustomersError(
#                 self, min_required=position + number_of_customers_to_delete
#             )
#         del self.route[position + 1 : position + number_of_customers_to_delete]

#         return self

#     def insert(
#         self, position: int, sequence: list[VRPTWCustomer]
#     ) -> VRPTWRoute:
#         if position < 0 or position > super().__len__():
#             raise NameError("Wrong insert position in the route.")

#         self.route = (
#             self.route[: position + 1] + sequence + self.route[position + 1 :]
#         )

#         return self

#     def violate_windows(self):
#         pass

#     def exceeds_capacity(self):
#         pass

#     @staticmethod
#     def validate_route_insertion(
#         customer: VRPTWCustomer, position: int, route: VRPTWRoute
#     ) -> bool:
#         route.insert(position, [customer])
#         return not (route.violate_windows() or route.exceeds_capacity())


# class VRPTWSolution(Solution):
#     """_summary_.

#     Args:
#         Solution (_type_): _description_
#     """

#     def __init__(self, routes: list[VRPTWRoute]) -> None:
#         """_summary_.

#         Args:
#             routes (list[VRPTWRoute]): _description_
#         """
#         self.routes = routes


# class VRPTW(VRP):
#     """VRPTW Problem Class."""

#     def __init__(
#         self,
#         depot: list[VRPTWDepot],
#         customers: list[VRPTWCustomer],
#         vehicles: list[Vehicle],
#         instance_name: str = "VRPTW Instance",
#         file_name: str | None = None,
#     ) -> None:
#         """Class Constructor.

#         Args:
#             depot: _description_
#             customers: _description_
#             vehicles: _description_
#             instance_name: _description_. Defaults to "VRPTW Instance".
#             file_name: _description_. Defaults to None.
#         """
#         super().__init__(vehicles=vehicles)
#         self.depot = depot
#         self.customers = customers
#         self.instance_name = instance_name
#         self.file_name = file_name

#     @classmethod
#     def from_file(
#         cls,
#         file_name: str,
#         read_problem_function: Callable[
#             [str], tuple[str, VRPTWDepot, list[Vehicle], list[VRPTWCustomer]]
#         ],
#         instance_name: str = "VRPTW Instance",
#     ) -> VRPTW:
#         """Alternative problem constructor from file.

#         Args:
#             file_name: _description_
#             read_problem_function: _description_
#             instance_name: _description_. Defaults to "VRPTW Instance".

#         Returns:
#             VRPTW: _description_
#         """
#         instance_name, depot, vehicles, customers = read_problem_function(
#             file_name
#         )
#         return cls(
#             depot=[depot],
#             customers=customers,
#             vehicles=vehicles,
#             instance_name=instance_name,
#             file_name=file_name,
#         )

#     def __repr__(self) -> str:
#         """_summary_.

#         Returns:
#             str: _description_
#         """
#         return (
#             f"{self.__class__.__name__}( "
#             + f"depots=[{len(self.depot)} Depot(s)], "
#             + f"customers=[{len(self.customers)} Customer(s)], "
#             + f"vehicles=[{len(self.vehicles)} Vehicles(s)], "
#             + f"name={self.instance_name}, file={self.file_name} )"
#         )

# if __name__ != "__main__":
#     Location = jitclass(Location)
