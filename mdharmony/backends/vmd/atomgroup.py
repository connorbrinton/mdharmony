"""
VMDAtomGroup module.
"""
import numpy as np

import mdharmony
from mdharmony.atomproperty import ATOM_PROPERTIES
from mdharmony.silencer import silence

with silence():
    import vmd
from VMD import atomsel



VMD_ATOM_PROPERTIES = {
    'serial': 'serial',
    'name': 'name',
    'resname': 'resname',
    'chain': 'chain',
    'resseq': 'resid', # TODO: Replace with more accurate match
    'segment': 'segid',
    'element': 'element',
    'charge': 'charge'
}


class VMDAtomGroup(mdharmony.AtomGroup):
    def __init__(self, molid, indices):
        self.molid = molid
        self.indices = np.array(indices)

    def __len__(self):
        return len(self.indices)

    def __iter__(self):
        for index in self.indices:
            yield self[index]

    def __getitem__(self, selector):
        if np.isscalar(selector):
            selector = [selector]
        return VMDAtomGroup(self.molid, self.indices[selector])


# Define property generator
def generate_property(name):
    # Look up VMD attribute
    attribute = VMD_ATOM_PROPERTIES[name]

    # Define attribute getter
    def get_attribute(vmd_atom_group):
        query = "index " + " ".join(str(index) for index in vmd_atom_group.indices)
        selection = atomsel.atomsel(query, molid=vmd_atom_group.molid).get(attribute)
        return np.asarray(selection)

    # Return property
    return property(get_attribute)


# Define property injector
def inject_properties():
    for atom_property in ATOM_PROPERTIES:
        name = atom_property.singular
        setattr(VMDAtomGroup, name, generate_property(name))


# Inject properties
inject_properties()
