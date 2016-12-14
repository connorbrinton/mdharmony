"""
Module defining VMD topology class.
"""
from __future__ import print_function

import mdharmony
import mdharmony.registry

@mdharmony.registry.register_topology_class(mdharmony.Backend.VMD):
class VMDTopology(mdharmony.Topology):
    def load(*args, **kwargs):
        print
