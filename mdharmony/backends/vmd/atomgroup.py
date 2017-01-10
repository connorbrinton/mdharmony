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
    'chain': 'chain',
    'segment': 'segid',
    'resseq': 'resid', # TODO: Replace with more accurate match
    'resname': 'resname',
    'name': 'name',
    'element': 'element',
    'charge': 'charge'
}


class VMDAtomGroup(mdharmony.AtomGroup):
    def __init__(self, molid, indices):
        self.molid = molid
        self._indices = np.array(indices)

    def __len__(self):
        return len(self._indices)

    def __iter__(self):
        for index in self._indices:
            yield self[index]

    def __getitem__(self, selector):
        if np.isscalar(selector):
            selector = [selector]
        return VMDAtomGroup(self.molid, self._indices[selector])

    @property
    def index(self):
        return self._indices

    @property
    def indices(self):
        return self._indices

    @property
    def selection(self):
        query = "index " + " ".join(str(index) for index in self._indices)
        return atomsel.atomsel(query, molid=self.molid)

    @property
    def bonds(self):
        for index, partners in enumerate(self.selection.bonds):
            for partner in partners:
                yield self[[index, partner]]


# Define property generator
def generate_property(name):
    # Look up VMD attribute
    attribute = VMD_ATOM_PROPERTIES[name]

    # Define attribute getter
    def get_attribute(vmd_atom_group):
        return np.asarray(vmd_atom_group.selection.get(attribute))

    # Return property
    return property(get_attribute)


# Define property injector
def inject_properties():
    for atom_property in ATOM_PROPERTIES:
        # Load the singular name
        name = atom_property.singular

        # Skip index/indices, we handle them manually
        if name == "index":
            continue

        # Add a getter property for the atom property
        setattr(VMDAtomGroup, name, generate_property(name))


# Inject properties
inject_properties()
