"""
Module defining VMD topology class.
"""
from __future__ import print_function

import mdharmony
import mdharmony.registry
from mdharmony.silencer import silence

# TODO: Make these imports optional for program execution (especially for other backends)
with silence():
    import vmd
from VMD import molecule

from .atomgroup import VMDAtomGroup
from .utilities import get_vmd_file_type


@mdharmony.registry.register_topology_class(mdharmony.Backend.VMD)
class VMDTopology(mdharmony.Topology):
    @staticmethod
    def load(*args, **kwargs):
        # Extract path
        path = args[0]

        # Load topology from path
        with silence():
            molid = molecule.load(get_vmd_file_type(path), path)

        return VMDTopology(molid)

    def __init__(self, molid):
        self.molid = molid

    @property
    def atoms(self):
        atom_count = molecule.numatoms(self.molid)
        indices = list(range(atom_count))
        return VMDAtomGroup(self.molid, indices)

    @property
    def bonds(self):
        raise NotImplementedError("Not yet implemented...")
