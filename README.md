# Rotation

`Rotation` is a Python package for working with 3D rotations.  
It provides validated rotation matrices, quaternions (WXYZ / XYZW), Rodrigues rotation parameters (axis–angle vectors), and skew-symmetric matrices.

## Installation

Install dependencies only:

```bash
pip install -r requirements.txt
```

From the repository root, add `src` to your Python path so the package can be imported:

```bash
export PYTHONPATH=src
```

## Usage

```python
import numpy as np

from rotation import (
    Quaternion,
    QuaternionFormat,
    RodriguesRotationParameter,
    RotationMatrix,
    SkewSymmetricMatrix,
)

# Identity rotation matrix
R0 = RotationMatrix.unit_matrix()

# Rodrigues vector (axis * angle); convert to matrix
r = RodriguesRotationParameter(value=np.array([0.0, 0.0, np.pi / 4]))
R1 = r.rotation_matrix

# Compose rotations
R = R0 @ R1

# Quaternion (normalized), WXYZ layout
q = Quaternion(
    value=np.array([1.0, 0.0, 0.0, 0.0]),
    format=QuaternionFormat.WXYZ,
)
R_from_q = q.rotation_matrix

# Skew-symmetric matrix from components
K = SkewSymmetricMatrix.from_k_parameter(k_x=0.0, k_y=0.0, k_z=1.0)
```

For module layout, see [src/rotation/README.md](src/rotation/README.md).
