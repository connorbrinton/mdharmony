"""
Module defining Trajectory class.
"""
from __future__ import absolute_import

import mdharmony
import mdharmony.registry


class Trajectory(object):
    @staticmethod
    def load(*args, **kwargs):
        """
        Load the file at the specified path using the backend specified by the keyword argument
        `backend` (or the default backend, if none is specified). Returns a backend-specific
        subclass of this class.
        """
        # Extract backend
        backend = kwargs.get('backend', None)

        # Default parameters
        if backend is None:
            backend = mdharmony.DEFAULT_BACKEND

        # Make sure there was a default
        if backend is None:
            raise Exception("No backend specified.")

        # Find backend trajectory loader
        return mdharmony.registry.TRAJECTORY_CLASSES[backend].load(*args, **kwargs)

    # TODO: Define interface
