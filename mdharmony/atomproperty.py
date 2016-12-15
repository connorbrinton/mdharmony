"""
AtomProperty module.
"""
from collections import namedtuple

AtomProperty = namedtuple('AtomProperty', ['singular', 'plural', 'description'])
ATOM_PROPERTIES = [
    AtomProperty('serial', 'serials', "Serial number"),
    AtomProperty('name', 'names', "Name"),
    AtomProperty('resname', 'resnames', "Residue name"),
    AtomProperty('chain', 'chains', "Chain"),
    AtomProperty('resseq', 'resseqs', "Residue sequence number"),
    AtomProperty('segment', 'segments', "Segment"),
    AtomProperty('element', 'elements', "Element"),
    AtomProperty('charge', 'charges', "Charge")
]
