"""
Utility variables, functions, and classes for the VMD backend.
"""
# VMD file mapping
VMD_FILE_TYPES = {
    'nc': 'netcdf'
}


def get_vmd_file_type(path):
    """
    Determine the file type of the given file (just use the extension by default).
    """
    extension = path.split('.')[-1]
    return VMD_FILE_TYPES.get(extension, extension)
