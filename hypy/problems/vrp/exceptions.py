"""VRP Exceptions Module."""


from hypy.problems.vrp.components import Route
from hypy.problems.vrp.vrptw.components import VRPTWRoute


class LocationCoordinatesError(Exception):
    """Location Coordinates Error.

    Location Coordinates Error: Coordinates must be a non-empty 1D
    '<class 'numpy.ndarray'>
    """

    def __init__(
        self,
        coordinates_type: type | None = None,
        shape: tuple[int] | None = None,
        size: int | None = None,
        *args: object,
    ) -> None:
        """Class Constructor.

        Args:
            coordinates_type: _description_.
                Defaults to None.
            shape: _description_. Defaults
                to None.
            size: _description_. Defaults to None.
        """
        super().__init__(*args)
        self.coordinates_type = coordinates_type
        self.shape = shape
        self.size = size

    def __str__(self) -> str:
        """String Representation Method.

        Returns:
            _description_
        """
        message: str = ""

        if self.coordinates_type:
            message = (
                "Coordinates must be of type <class "
                + f"'numpy.ndarray'>, not {self.coordinates_type}"
            )

        elif self.shape:
            message = (
                "Coordinates must be 1-dimensional, "
                + f"not {self.shape}-dimensional"
            )

        elif self.size is not None:
            message = (
                "Coordinates must be a non-empty <class "
                + "'numpy.ndarray'> array"
            )

        return message


class EmptySolutionError(Exception):
    """Empty Solution Error.

    Empty Solution Error: The solution has no routes.
    """

    def __init__(self, *args: object) -> None:
        """Constructor Method."""
        super().__init__(*args)

    def __str__(self) -> str:
        """String Representation Method.

        Returns:
            _description_
        """
        return "The solution has no routes."


class NotEnoughCustomersError(Exception):
    """Not Enough Customers Error.

    Not Enough Customers Error: The route does not contain the minimum number
        of customers required for the operation.
    """

    def __init__(
        self, route: Route | VRPTWRoute, min_required: int = 2, *args: object
    ) -> None:
        """Constructor Method.

        Args:
            route (Route | VRPTWRoute): _description_
            min_required (int, optional): _description_. Defaults to 2.
        """
        super().__init__(*args)
        self.route = route
        self.min_required = min_required

    def __str__(self) -> str:
        """String Representation Method.

        Returns:
            _description_
        """
        return (
            f"The route contains {len(self.route)} customers, which is "
            + "lower than the minimum amount required for the operation."
            + "Minimum amount of customers required for this operation: "
            + f"{self.min_required}."
        )
