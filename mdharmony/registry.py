"""
Registry module for MDHarmony, registering backends.
"""
TOPOLOGY_CLASSES = {}


def register_topology_class(backend):
    # Create true decorator function
    def register_topology_class_for_backend(topology_clz):
        TOPOLOGY_CLASSES[backend] = topology_clz

    # Return it
    return register_topology_class_for_backend
