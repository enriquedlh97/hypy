"""VRP Exceptions Module."""


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
