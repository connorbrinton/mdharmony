"""
A context used for temporarily silencing stdout, effectively sending it to
/dev/null. From http://stackoverflow.com/questions/977840/redirecting-fortran-called-via-f2py-output-in-python/978264#978264
"""
import contextlib
import os


@contextlib.contextmanager
def silence():
    # Create the black hole, the endless void, the bottomless pit!
    blackhole = os.open(os.devnull, os.O_RDWR)
    # Copy a reference to stdout
    original = os.dup(1)
    # Redirect fd 1 to the blackhole "file"
    os.dup2(blackhole, 1)

    # Let the body run
    yield

    # Redirect fd 1 to the original stdout
    os.dup2(original, 1)
    # Close the blackhole "file"
    os.close(blackhole)
