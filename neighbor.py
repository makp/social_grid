import numpy as np


class Nbr:
    """Manipulates cell neighbors in a cellular automata.

    Supported types of neighborhood:
    - von Neumann (4 neighbors)
    - Moore (8 neighbors)

    Periodic boundary conditions---i.e., borders wrap around.
"""

    def __init__(self, num_nbrs):
        self.num_nbrs = num_nbrs

    def rotate_array(self, arr):
        nbr = dic[self.num_nbrs]  # nbr type
        return tuple(rotate2d(arr, *t) for t in nbr)

    def list_nbrs(self, arr):
        """Replaces elements of `arr' with 1D arrays containing the
        original cell followed by its neighbors."""
        t = self.rotate_array(arr)
        return np.stack((arr, *t), axis=2)

    def map_nbrs(self, arr, func):
        """Returns a 2D-array in which each cell is the result applying the
        function 'func' to each cell in 'arr' and all of its neighbors."""
        arr_nbrs = self.list_nbrs(arr)
        gen = (func(*xs) for row in arr_nbrs for xs in row)
        return np.array(tuple(gen)).reshape(arr.shape)


# Four neighbors
neighNeumann = ((+1, 0),        # N (immediately above)
                (-1, 0),        # S
                (0, -1),        # E
                (0, +1))        # W

# Eight neighbors
neighMoore = (*neighNeumann,
              (+1, -1),         # NE
              (-1, -1),         # SE
              (-1, +1),         # SW
              (+1, +1))         # NW

dic = {4: neighNeumann, 8: neighMoore}


def rotate1d(arr1d, s):
    """Rotate 1D array.

The returned array is a copy of the 1D array `arr1d' after rotating
its elements `s' steps."""
    return np.concatenate((arr1d[-s:], arr1d[:-s]))


def rotate2d(arr2d, i, j):
    """Rotate 2D array.

The returned array is a copy of `arr2d' after rotating its rows i
steps and the members of each row by j steps."""
    arr = rotate1d(arr2d, i)                    # rotate rows
    t = tuple(rotate1d(row, j) for row in arr)  # rotate elements
    return np.array(t)
