# rotation

## Overview

Utilities for representing 3D rotations: validated rotation matrices and composition, quaternions with configurable layout, and Rodrigues parameters with skew-symmetric matrices for conversion.

## Components

| Component | Description |
|-----------|-------------|
| [matrix.py](./matrix.py) | `RotationMatrix` — validate 3×3 rotations, compose with `@`, build from identity or approximate matrices |
| [quaternion/](./quaternion/README.md) | `Quaternion` / `QuaternionFormat` — normalized quaternions and WXYZ / XYZW ordering |
| [rodrigues/](./rodrigues/README.md) | `RodriguesRotationParameter` / `SkewSymmetricMatrix` — Rodrigues formula and skew-symmetric helpers |

