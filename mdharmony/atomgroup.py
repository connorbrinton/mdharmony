"""
AtomGroup module.
"""
from __future__ import absolute_import

from .atomproperty import ATOM_PROPERTIES


class AtomGroup(object):
    """
    Represents a collection of atoms. Each backend provides its own specialized AtomGroup
    implementation, matching the standard set by this class.
    """
    def __len__(self):
        raise NotImplementedError("Not implemented for abstract AtomGroup.")

    def __iter__(self):
        raise NotImplementedError("Not implemented for abstract AtomGroup.")

    def __getitem__(self, selector):
        """
        Select an atom (or a slice of atoms) from this AtomGroup. The order of atoms in the
        AtomGroup is consistent between this method and atoms returned by iteration.
        """
        raise NotImplementedError("Not implemented for abstract AtomGroup.")


# Property generator for plural AtomGroup properties
def get_plural_property(singular):
    # Define getter function
    def plural_getter(atom_group):
        return set(getattr(atom_group, singular))

    # Return property
    return property(plural_getter)


# Property injector
def inject_properties():
    for atom_property in ATOM_PROPERTIES:
        # Extract property names
        singular, plural = atom_property[:2]

        # Inject plural property
        plural_property = get_plural_property(singular)
        setattr(AtomGroup, plural, plural_property)


# Inject singular and plural lookup
inject_properties()
