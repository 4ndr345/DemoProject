import numpy as np

from ._version import get_versions


__version__ = get_versions()['version']
del get_versions


def rotation(angle, axsis):
    q = np.zeros(4)
    q[0] = np.sin(angle * 0.5)
    q[1:] = np.cos(angle * 0.5) * axsis
    return q
