"""
Backends provider module.
"""
from __future__ import absolute_import
import imp

# If VMD python extensions are installed...
if imp.find_module('vmd'):
    # Load the VMD backend
    from . import vmd
