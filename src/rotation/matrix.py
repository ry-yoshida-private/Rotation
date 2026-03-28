from __future__ import annotations

import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class RotationMatrix:
    """
    Container class for rotation matrix representation of rotation.
    
    Attributes
    ----------
    value: np.ndarray
        The rotation matrix as a 3x3 matrix.

    Raises
    ------
    ValueError:
        If the rotation matrix is not a 3x3 matrix.
        If the rotation matrix is not orthogonal.
        If the rotation matrix does not have determinant +1 (not a proper rotation).
    """
    value: np.ndarray

    def __post_init__(self):
        """Validate that the rotation matrix is valid."""
        self._is_valid_rotation_matrix()

    def _is_valid_rotation_matrix(self) -> None:
        """Check if a matrix is a valid rotation matrix."""
        if self.value.shape != (3, 3):
            raise ValueError("Invalid rotation matrix: must be a 3x3 matrix")
        
        if not self.is_orthogonal:
            raise ValueError("Invalid rotation matrix: must be orthogonal")
        
        if not self.is_determinant_correct:
            raise ValueError("Invalid rotation matrix: must have correct determinant")

    @property
    def is_orthogonal(self) -> bool:
        """
        Check if the rotation matrix is orthogonal.
        
        Returns
        -------
        bool:
            True if the rotation matrix is orthogonal, False otherwise.
        """
        return np.allclose(self.value.T @ self.value, np.eye(3), atol=1e-6)

    @property
    def is_determinant_correct(self) -> bool:
        """
        Check if the rotation matrix has determinant +1 (proper rotation in SO(3)).

        Returns
        -------
        bool:
            True if the determinant is +1, False otherwise.
        """
        return np.isclose(np.linalg.det(self.value), 1.0, atol=1e-6)

    @property
    def T(self) -> np.ndarray:
        """
        Return the transpose of the rotation matrix.
        
        Returns
        -------
        np.ndarray:
            The transpose of the rotation matrix.
        """
        return self.value.T

    @property
    def inv(self) -> np.ndarray:
        """
        Return the inverse of the rotation matrix.
        
        Returns
        -------
        np.ndarray:
            The inverse of the rotation matrix.
        """
        return np.linalg.inv(self.value)

    @property
    def x_axis(self) -> np.ndarray:
        """
        Return the x-axis of the rotation matrix.
        
        Returns
        -------
        np.ndarray:
            The x-axis of the rotation matrix with shape (3,).
        """
        return self.value[:, 0]
    
    @property
    def y_axis(self) -> np.ndarray:
        """
        Return the y-axis of the rotation matrix.
        
        Returns
        -------
        np.ndarray:
            The y-axis of the rotation matrix with shape (3,).
        """
        return self.value[:, 1]
    
    @property
    def z_axis(self) -> np.ndarray:
        """
        Return the z-axis of the rotation matrix.
        
        Returns
        -------
        np.ndarray:
            The z-axis of the rotation matrix with shape (3,).
        """
        return self.value[:, 2]

    def __matmul__(
        self, 
        other: RotationMatrix
        ) -> RotationMatrix:
        """
        Multiply two rotation matrices.
        
        Returns
        -------
        RotationMatrix:
            The product of the two rotation matrices.
        
        """
        return RotationMatrix(value=self.value @ other.value)


    @classmethod
    def unit_matrix(cls) -> RotationMatrix:
        """
        Create the identity rotation matrix.

        Returns
        -------
        RotationMatrix:
            The unit rotation matrix.
        """
        return cls(value=np.eye(3))

    @classmethod
    def from_approximate_matrix_by_qr(
        cls,
        value: np.ndarray,
        ) -> RotationMatrix:
        """
        Create a RotationMatrix object from an approximate rotation matrix by QR decomposition.

        Parameters
        ----------
        value: np.ndarray
            The approximate rotation matrix.

        Returns
        -------
        RotationMatrix:
            The rotation matrix from the approximate matrix.
        """
        Q, _ = np.linalg.qr(value) #Q, R
        det = np.linalg.det(Q)

        if det < 0:
            Q[:, -1] *= -1
        return cls(value=Q)

    @classmethod
    def from_approximate_matrix_with_SVD(
        cls,
        value: np.ndarray,
        ) -> RotationMatrix:
        """
        Create a RotationMatrix object from an approximate rotation matrix by SVD decomposition.

        Parameters
        ----------
        value: np.ndarray
            The approximate rotation matrix.

        Returns
        -------
        RotationMatrix:
            The rotation matrix from the approximate matrix.
        """
        u, _, vh = np.linalg.svd(value) # u, s, vh: np.ndarray
        rotation_matrix = u @ vh

        if np.linalg.det(rotation_matrix) < 0:
            u[:, -1] *= -1
            rotation_matrix = u @ vh

        return cls(value=rotation_matrix)

