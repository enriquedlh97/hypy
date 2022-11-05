"""Exceptions."""


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
        """_summary_.

        :param coordinates_type: _description_, defaults to None
        :type coordinates_type: type | None, optional
        :param shape: _description_, defaults to None
        :type shape: tuple[int] | None, optional
        :param size: _description_, defaults to None
        :type size: int | None, optional
        """
        super().__init__(*args)
        self.coordinates_type = coordinates_type
        self.shape = shape
        self.size = size

    def __str__(self) -> str:
        """_summary_.

        :return: _description_
        :rtype: str
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
