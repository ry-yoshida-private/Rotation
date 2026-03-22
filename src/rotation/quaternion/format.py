from enum import Enum

class QuaternionFormat(Enum):
    """
    Quaternion format enumeration.

    Attributes:
    ----------
    WXYZ: QuaternionFormat
        The quaternion format is [w, x, y, z].
    XYZW: QuaternionFormat
        The quaternion format is [x, y, z, w].
    """
    WXYZ = "wxyz"  # [w, x, y, z]
    XYZW = "xyzw"  # [x, y, z, w] 

    @property
    def as_upper(self) -> str:
        """
        Return the quaternion format as uppercase.

        Returns
        -------
        str:
            The quaternion format as uppercase.
        """
        return str(self.value).upper()

    @property
    def as_lower(self) -> str:
        """
        Return the quaternion format as lowercase.

        Returns
        -------
        str:
            The quaternion format as lowercase.
        """
        return str(self.value).lower()

    @property
    def is_scalar_first(self) -> bool:
        """
        Check if the quaternion format is scalar first.

        Returns
        -------
        bool:
            True if the quaternion format is scalar first, False otherwise.
        """
        return self == QuaternionFormat.WXYZ