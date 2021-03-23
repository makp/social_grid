import numpy as np


class CA:
    def __init__(self, num_nbrs):
        self.num_nbrs = num_nbrs

    def rotate_array(self, arr):
        nbr = dic[self.num_nbrs]  # nbr type
        arrs = np.array([rotateCA(arr, *t) for t in nbr])
        return arrs

    def list_nbrs(self, arr):
        """Returns an array in which each cell is replaced by an 1D array
        containing the cell in question followed by its neighbors based on
        the chosen type of neighborhood (von Neumann or Moore)."""
        arrs = self.rotate_array(arr)
        out = np.stack((arr, *arrs), axis=2)
        return out

    def map_nbrs(self, arr, func):
        """Returns a 2D-array in which each cell is the result applying the
        function 'func' to each cell in 'arr' and all of its neighbors."""
        arr_nbrs = self.list_nbrs(arr)
        gen = (func(*xs) for row in arr_nbrs for xs in row)
        out = np.array(tuple(gen)).reshape(arr.shape)
        return out


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


def rotate_right(array, steps):
    a = array[-steps:]
    b = array[:-steps]
    return np.concatenate((a, b))


def rotateCA(arr, i, j):
    """Return 'arr' after rotating its rows i steps and
    the members of each row by j steps."""
    arr = rotate_right(arr, i)                    # rotate rows
    t = tuple(rotate_right(row, j) for row in arr)  # rotate elements
    return np.array(t)
