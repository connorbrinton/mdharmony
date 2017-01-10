"""
AtomProperty module.
"""
from collections import namedtuple

AtomProperty = namedtuple('AtomProperty', ['singular', 'plural', 'description'])
ATOM_PROPERTIES = [
    AtomProperty('index', 'indices', "Atom index"),
    AtomProperty('chain', 'chains', "Chain"),
    AtomProperty('segment', 'segments', "Segment"),
    AtomProperty('resname', 'resnames', "Residue name"),
    AtomProperty('resseq', 'resseqs', "Residue sequence number"),
    AtomProperty('name', 'names', "Name"),
    AtomProperty('element', 'elements', "Element"),
    AtomProperty('charge', 'charges', "Charge")
]
