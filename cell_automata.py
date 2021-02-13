import numpy as np

class CA:
    def __init__(self, num_nbrs):
        self.num_nbrs = num_nbrs

    def list_nbrs(self, arr):
        """Returns an array in which each cell is replaced by a 1D array containing the cell in question followed by its neighbors based on the chosen type of neighborhood (von Neumann and Moore)."""
        nbr = dic[self.num_nbrs]  # nbr type
        arrs = np.array(tuple(rotateCA(arr, *t) for t in nbr))
        out = np.dstack((arr,*arrs))
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
    return np.concatenate((a,b))

def rotateCA(arr, i, j):
    """Return 'arr' after rotating its rows i steps and the members of each row by j steps."""
    arr = rotate_right(arr, i)                    # rotate rows
    t = tuple(rotate_right(row,j) for row in arr)  # rotate elements
    return np.array(t)

