"""
Registry module for MDHarmony, registering backends.
"""
TOPOLOGY_CLASSES = {}
TRAJECTORY_CLASSES = {}


def register_topology_class(backend):
    # Create true decorator function
    def register_topology_class_for_backend(topology_clz):
        TOPOLOGY_CLASSES[backend] = topology_clz
        return topology_clz

    # Return it
    return register_topology_class_for_backend


def register_trajectory_class(backend):
    # Create true decorator function
    def register_trajectory_class_for_backend(trajectory_clz):
        TRAJECTORY_CLASSES[backend] = trajectory_clz
        return trajectory_clz

    # Return it
    return register_trajectory_class_for_backend
