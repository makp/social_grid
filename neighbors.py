import numpy as np

"""
Line for testing:
from neighbors import Neighbors; teste = Neighbors(lat, 4); teste.list_neighbors()
"""

class Neighbors:
    def __init__(self, array, num_neighbors):
        self.array = array
        self.num_neighbors = num_neighbors

    def list_neighbors(self):
        """Returns an array in which each row lists the value of every cell followed by the value of its neighbors based on the chosen type of neighborhood (von Neumann and Moore)."""
        nbr = dic[self.num_neighbors]  # neighborhood type
        ca = self.array                # the given CA
        gen = (rotateCA(ca, *t) for t in nbr)
        result = ca.ravel()
        for g in gen:
            result = np.vstack((result, g.ravel()))
        return result.T

dic = {4: neighNeumann, 8: neighMoore}

# Four neighbors
neighNeumann = {(+1, 0),        # N (immediately above)
                (-1, 0),        # S
                (0, -1),        # E
                (0, +1)}        # W

# Eight neighbors
neighMoore = neighNeumann.union({
    (+1, -1),                   # 
    (-1, -1),                   # 
    (-1, +1),                   # 
    (+1, +1)})                  #



def rotate_right(array, steps):
    a = array[-steps:]
    b = array[:-steps]
    return np.concatenate((a,b))

def rotateCA(array, i, j):
    """For a given 2D array, rotate rows i steps and their elements j steps."""
    arr = rotate_right(array, i)                  # rotate rows
    t = tuple(rotate_right(row,j) for row in arr)  # rotate elements
    return np.array(t)

