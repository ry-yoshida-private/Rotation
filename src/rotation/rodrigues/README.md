# rodrigues

## Overview

Rodrigues rotation parameters (3D vectors encoding axis direction and rotation magnitude) and the associated skew-symmetric matrices.  
`RodriguesRotationParameter` maps to `RotationMatrix` via Rodrigues’ formula; vectors can be rotated with `transform`.

## Components

| Component | Description |
|-----------|-------------|
| [rodrigues_rotation.py](./rodrigues_rotation.py) | `RodriguesRotationParameter` — validation, `rotation_matrix`, `transform` for vectors |
| [skew_symmetric_matrix.py](./skew_symmetric_matrix.py) | `SkewSymmetricMatrix` — construction and squared term used in Rodrigues’ formula |

See the parent package [../README.md](../README.md) for context.
