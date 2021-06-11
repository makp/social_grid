import numpy as np
from neighbor import Nbr


class UpdateCell(Nbr):
    """Updates each cell based on its state and its neighbors' states."""

    def update_cell(self, arr, func):
        """Returns a 2D-array in which each cell is the result applying the
        function 'func' to each cell in 'arr' and all of its neighbors."""
        arr_nbrs = self.list_nbrs(arr)
        gen = (func(arr) for row in arr_nbrs for arr in row)
        return np.array(tuple(gen)).reshape(arr.shape)


class UpdateAll(Nbr):
    """Update each cell and its neighbors."""

    def __init__(self, side, num_nbrs=4):
        self.side = side
        self.num_nbrs = num_nbrs
        self.imap = self.inds_dict(self.side)

    def update_nbrs(self, ca, func):
        """Update neighbors without changing focal cell."""
        ca_new = np.copy(ca)
        for index in np.ndindex(ca.shape):
            if ca[index]:
                ind_nbrs = self.imap[index]
                cell, nbrs = ca[index], ca_new[ind_nbrs]
                ca_new[ind_nbrs] = func(cell, nbrs)
        return ca_new
