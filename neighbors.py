import numpy as np

class Neighbors:
    def __init__(self, num_neighbors):
        self.num_neighbors = num_neighbors

    def list_neighbors(self, arr):
        """Returns an array in which each row lists the value of every cell followed by the value of its neighbors based on the chosen type of neighborhood (von Neumann and Moore)."""
        nbr = dic[self.num_neighbors]  # neighborhood type
        gen = (rotateCA(arr, *t) for t in nbr)
        result = arr.ravel()
        for g in gen:
            result = np.vstack((result.copy(), g.ravel()))
        return result.T

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

def rotateCA(array, i, j):
    """For a given 2D array, rotate rows i steps and their elements j steps."""
    arr = rotate_right(array, i)                  # rotate rows
    t = tuple(rotate_right(row,j) for row in arr)  # rotate elements
    return np.array(t)

