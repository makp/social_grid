import numpy as np


class Nbr:
    """Provides info about the neighbors of a 2D cellular automata.

    Attributes:
    - num_nbrs: Number of neighbors. Possible values:
        + 4 (von Neumann neighborhood)
        + 8 (Moore neighborhood)

    Periodic boundary conditions---i.e., borders wrap around.
"""

    def __init__(self, num_nbrs):
        self.num_nbrs = num_nbrs

    def list_nbrs(self, arr):
        """Replaces elements of `arr' with 1D arrays containing the
        original cell followed by its neighbors."""
        t = rotate_arr(arr, self.num_nbrs)
        return np.stack((arr, *t), axis=2)

    def inds_dict(self, d):
        a = np.indices((d, d))
        rs, cs = (rotate_arr(a[i], self.num_nbrs) for i in range(2))
        ind_nbrs = np.stack((rs, cs), axis=1)
        dc = {}
        for i, j in np.ndindex((d, d)):
            ii, jj = (ind_nbrs[:, axis, i, j] for axis in range(2))
            dc[(i, j)] = np.stack((ii, jj), axis=-1)
        return dc

    def get_inds_nbrs(self, d):
        a = np.indices((d, d))
        rs, cs = (rotate_arr(a[i], self.num_nbrs) for i in range(2))
        return np.stack((rs, cs), axis=1)


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


def rotate_arr(arr, num_nbrs):
    nbr = dic[num_nbrs]  # nbr type
    return tuple(rotate2d(arr, *t) for t in nbr)


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
