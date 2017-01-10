"""
Main MDHarmony package, providing a unified API for loading, converting, and interacting with
in-memory molecular dynamics trajectory formats.

This package is based on use of the following primitive objects:
* Topology
* Trajectory
* ...
Which define the bare-minimum API requirements for any backend-specific object.

These objects are loaded using backend-specific loaders, including:
* VMD
* mdtraj
* ...
And stored in backend-specific python objects subclassing the above primitives.

Topologies and Trajectories are loaded using their static `load` function. Each `load` function
accepts (in addition to its own parameters) the keyword argument `backend`, which allows the user to
specify a backend to use. The default backend is unspecified, and may change from release to
release.
"""
from __future__ import absolute_import

# Enum specifying possible backends
Backend = type('Backend', (), {
    "MDTRAJ": 0,
    "VMD": 1
})

# Default backend
DEFAULT_BACKEND = None


# Import primitives
from .atomgroup import AtomGroup
from .coordinates import Coordinates
from .topology import Topology
from .trajectory import Trajectory

# Import backends
from .backends import *
