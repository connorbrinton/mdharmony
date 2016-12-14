"""
Module defining Topology class.
"""
import mdharmony
import mdharmony.registry

class Topology(object):
    @staticmethod
    def load(*args, **kwargs):
        # Extract backend
        backend = kwargs.get('backend', None)

        # Default parameters
        if backend is None:
            backend = mdharmony.DEFAULT_BACKEND

        # Find backend topology loader
        return mdharmony.registry.TOPOLOGY_CLASSES[backend].load(*args, **kwargs)
