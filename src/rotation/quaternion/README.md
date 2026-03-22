# quaternion

## Overview

Quaternion representation of rotations.  
Uses `scipy.spatial.transform.Rotation` to convert to rotation matrices. `QuaternionFormat` selects scalar component order (WXYZ vs XYZW).

## Components

| Component | Description |
|-----------|-------------|
| [container.py](./container.py) | `Quaternion` — normalized 4-vector, format accessors, `rotation_matrix` |
| [format.py](./format.py) | `QuaternionFormat` — `WXYZ` / `XYZW` enum |

See the parent package [../README.md](../README.md) for context.
