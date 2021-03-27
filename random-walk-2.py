import numpy as np
from cell_automata import CA

ca = CA(4)                      # von Neumann nbr
arr = np.zeros((5, 9), dtype=int)
arr[2, 4] = 1


def make_index_arrays(arr):
    a = np.indices(arr.shape)
    rows = ca.rotate_array(a[0])
    cols = ca.rotate_array(a[1])
    out = np.stack((rows, cols), axis=1)
    return out
