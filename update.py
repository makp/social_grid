import numpy as np
from neighbor import Nbr


class UpdateCell(Nbr):
    """Updates each cell in a CA based on its neighbor values."""

    def update_cell(self, arr, func):
        """Returns a 2D-array in which each cell is the result applying the
        function 'func' to each cell in 'arr' and all of its neighbors."""
        arr_nbrs = self.list_nbrs(arr)
        gen = (func(arr) for row in arr_nbrs for arr in row)
        return np.array(tuple(gen)).reshape(arr.shape)


# class UpdateAll(Nbr):
#     """Update each cell and its neighbors."""