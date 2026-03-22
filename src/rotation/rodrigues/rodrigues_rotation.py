import numpy as np
from dataclasses import dataclass
from functools import cached_property

from .skew_symmetric_matrix import SkewSymmetricMatrix
from ..matrix import RotationMatrix

@dataclass(frozen=True)
class RodriguesRotationParameter:
    """
    Container class for Rodrigues rotation parameter.

    Attributes
    ----------
    value: np.ndarray
        The Rodrigues rotation parameter.
    """
    value: np.ndarray

    def __post_init__(self) -> None:
        """
        Validate that the Rodrigues rotation parameter is valid.
        
        Raises
        ------
        ValueError:
            If the Rodrigues rotation vector is not a 3x1 vector.
        """
        if self.value.shape != (3,):
            raise ValueError("Rodrigues rotation vector must be a 3x1 vector")

    @property
    def x(self) -> float:
        """
        Return the x component of the Rodrigues rotation parameter.

        Returns
        -------
        float:
            The x component of the Rodrigues rotation parameter.
        """
        return self.value[0]

    @property
    def y(self) -> float:
        """
        Return the y component of the Rodrigues rotation parameter.

        Returns
        -------
        float:
            The y component of the Rodrigues rotation parameter.
        """
        return self.value[1]

    @property
    def z(self) -> float:
        """
        Return the z component of the Rodrigues rotation parameter.

        Returns
        -------
        float:
            The z component of the Rodrigues rotation parameter.
        """
        return self.value[2]

    def transform(
        self, 
        vector: np.ndarray,
        ) -> np.ndarray:
        """
        Apply Rodrigues rotation formula to transform a vector.
        
        Parameters
        ----------
        vector: np.ndarray
            Vector to be rotated (shape: (3,))
            
        Returns
        -------
        np.ndarray
            Transformed vector (shape: (3,))

        Raises
        ------
        ValueError:
            If the input vector is not a 3x1 vector.
        """
        if vector.shape != (3,):
            raise ValueError("Input vector must be a 3x1 vector")

        return self.rotation_matrix.value @ vector

    @cached_property
    def rotation_matrix(self) -> RotationMatrix:
        """
        Convert Rodrigues rotation parameter to rotation matrix.

        Returns
        -------
        RotationMatrix:
            The rotation matrix.
        """
        theta = np.linalg.norm(self.value)

        if theta < 1e-6:
            return RotationMatrix(value=np.eye(3))

        normalized_rodrigues = RodriguesRotationParameter(value=self.value / theta)

        K = SkewSymmetricMatrix.from_k_parameter(
            k_x=normalized_rodrigues.x,
            k_y=normalized_rodrigues.y,
            k_z=normalized_rodrigues.z
            )

        I = np.eye(3) # Identity matrix
        skew_term = np.sin(theta) * K.value
        symmetric_term = (1 - np.cos(theta)) * K.squared
        R = I + skew_term + symmetric_term

        return RotationMatrix(value=R)
