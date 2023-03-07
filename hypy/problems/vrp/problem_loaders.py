"""VRP loader functions module."""
from __future__ import annotations

import numpy as np

from hypy.problems.vrp.components import Location, Vehicle
from hypy.problems.vrp.vrptw.components import (
    TimeWindow,
    VRPTWCustomer,
    VRPTWDepot,
)


def read_solomon_instance(
    file_name: str,
) -> tuple[str, VRPTWDepot, list[Vehicle], list[VRPTWCustomer]]:
    """_summary_.

    Args:
        file_name: _description_

    Returns:
        tuple[ str, VRPTWDepot, list[Vehicle], list[VRPTWCustomer] ]:
            _description_
    """
    with open(file_name) as instance:
        instance_data: list[str] = instance.readlines()
        instance_name: str = instance_data[0].strip()
        num_vehicles: int = int(instance_data[4].split()[0])
        vehicle_capacity: int = int(instance_data[4].split()[1])
        depot: VRPTWDepot = VRPTWDepot(
            id_number=int(instance_data[9].split()[0]),
            time_window=TimeWindow(
                ready_time=int(instance_data[9].split()[4]),
                due_date=int(instance_data[9].split()[5]),
                service_duration=int(instance_data[9].split()[6]),
            ),
            location=Location(
                np.array(
                    [instance_data[9].split()[1], instance_data[9].split()[2]]
                )
            ),
        )
        vehicles: list[Vehicle] = [
            Vehicle(capacity=vehicle_capacity, location=depot.location)
            for _ in range(num_vehicles)
        ]
        customers: list[VRPTWCustomer] = []

        for customer in instance_data[10:]:
            customer = customer.split()
            customers.append(
                VRPTWCustomer(
                    id_number=int(customer[0]),
                    demand=int(customer[3]),
                    time_window=TimeWindow(
                        ready_time=int(customer[4]),
                        due_date=int(customer[5]),
                        service_duration=int(customer[6]),
                    ),
                    location=Location(np.array([customer[1], customer[2]])),
                )
            )

    return (instance_name, depot, vehicles, customers)
