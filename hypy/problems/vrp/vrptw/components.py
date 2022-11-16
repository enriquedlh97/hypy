"""VRPTW Components Module."""


from __future__ import annotations

from typing import Callable

from hypy.problems.vrp.components import (
    VRP,
    Customer,
    Depot,
    Location,
    Vehicle,
)


class TimeWindow:
    """_summary_."""

    def __init__(
        self, ready_time: int, due_date: int, service_duration: int
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

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( "
            + f"window=[{self.ready_time}, {self.due_date}], "
            + f"service_duration={self.service_duration} )"
        )


class VRPTWCustomer(Customer):
    """_summary_.

    Args:
        Customer: _description_
    """

    def __init__(
        self,
        id_number: int,
        demand: float | int,
        time_window: TimeWindow,
        location: Location | None = None,
    ) -> None:
        """_summary_.

        Args:
            id_number: _description_
            demand: _description_
            time_window: _description_
            location: _description_. Defaults to None.
        """
        super().__init__(demand, location)
        self.id_number = id_number
        self.time_window = time_window

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( "
            + f"id={self.id_number}, demand={self.demand}, "
            + f"location={self.location}, time_window={self.time_window} )"
        )


class VRPTWDepot(Depot):
    """_summary_.

    Args:
        Depot (_type_): _description_
    """

    def __init__(
        self,
        id_number: int,
        time_window: TimeWindow,
        location: Location | None = None,
    ) -> None:
        """_summary_.

        Args:
            id_number: _description_
            time_window: _description_
            location: _description_. Defaults to None.
        """
        super().__init__(location)
        self.id_number = id_number
        self.time_window = time_window

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( "
            + f"id={self.id_number}, location={self.location}, "
            + f"time_window={self.time_window} )"
        )


class VRPTW(VRP):
    """VRPTW Problem Class."""

    def __init__(
        self,
        depot: list[VRPTWDepot],
        customers: list[VRPTWCustomer],
        vehicles: list[Vehicle],
        instance_name: str = "VRPTW Instance",
        file_name: str | None = None,
    ) -> None:
        """Class Constructor.

        Args:
            depot: _description_
            customers: _description_
            vehicles: _description_
            instance_name: _description_. Defaults to "VRPTW Instance".
            file_name: _description_. Defaults to None.
        """
        super().__init__(vehicles=vehicles)
        self.depot = depot
        self.customers = customers
        self.instance_name = instance_name
        self.file_name = file_name

    @classmethod
    def from_file(
        cls,
        file_name: str,
        read_problem_function: Callable[
            [str], tuple[str, VRPTWDepot, list[Vehicle], list[VRPTWCustomer]]
        ],
        instance_name: str = "VRPTW Instance",
    ) -> VRPTW:
        """Alternative problem constructor from file.

        Args:
            file_name: _description_
            read_problem_function: _description_
            instance_name: _description_. Defaults to "VRPTW Instance".

        Returns:
            VRPTW: _description_
        """
        instance_name, depot, vehicles, customers = read_problem_function(
            file_name
        )
        return cls(
            depot=[depot],
            customers=customers,
            vehicles=vehicles,
            instance_name=instance_name,
            file_name=file_name,
        )

    def __repr__(self) -> str:
        """_summary_.

        Returns:
            str: _description_
        """
        return (
            f"{self.__class__.__name__}( "
            + f"depots=[{len(self.depot)} Depot(s)], "
            + f"customers=[{len(self.customers)} Customer(s)], "
            + f"vehicles=[{len(self.vehicles)} Vehicles(s)], "
            + f"name={self.instance_name}, file={self.file_name} )"
        )
