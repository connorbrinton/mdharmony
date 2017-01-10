"""
Module defining VMD topology class.
"""
from __future__ import print_function

import numpy as np

import mdharmony
import mdharmony.registry
from mdharmony.silencer import silence

# TODO: Make these imports optional for program execution (especially for other backends)
with silence():
    import vmd
from VMD import molecule

from .topology import VMDTopology
from .atomgroup import VMDAtomGroup
from .utilities import get_vmd_file_type


@mdharmony.registry.register_trajectory_class(mdharmony.Backend.VMD)
class VMDTrajectory(mdharmony.Trajectory):
    @staticmethod
    def load(*args, **kwargs):
        # Unpack trajectory path and verify topology
        path, = args
        topology = kwargs.get('topology', None)
        if topology is None:
            raise Exception("Topology must be provided to load trajectory using VMD.")
        if not isinstance(topology, VMDTopology):
            raise Exception("Topology must be loaded using VMD.")

        return VMDTrajectory(topology, path)

    def __init__(self, topology, path):
        self._topology = topology
        self.path = path

    @property
    def coordinates(self):
        return VMDCoordinates(self)

    @property
    def topology(self):
        return self._topology


class VMDCoordinates(mdharmony.Coordinates):
    def __init__(trajectory):
        # Store trajectory object
        self._trajectory = trajectory

        # Determine coordinate dimensions
        atom_count = len(self._trajectory.topology.atoms)

        # Initialize preloaded frames
        self._preloaded_frames = []
        self._preloaded_coordinates = np.empty((0, atom_count, 3))

    @property
    def trajectory(self):
        return self._trajectory

    def __getitem__(self, selection):
        # TODO: Implement
        raise NotImplementedError("Not yet implemented.")

    def preload(self, frames):
        # TODO: Implement
        raise NotImplementedError("Not yet implemented.")

    def unload(self, frames):
        # TODO: Implement
        raise NotImplementedError("Not yet implemented.")
