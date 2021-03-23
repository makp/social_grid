import numpy as np
from cell_automata import CA

ca = CA(4)                      # von Neumann nbr
arr = np.zeros((5, 9))
arr[2, 4] = 1


def make_grid(i, j):
    a = np.indices((i, j))
    return np.stack(a, axis=-1)


def walk(x, *nbrs):
    if x == 0:
        return np.array((x, *nbrs))
    else:
        lst = list(nbrs)
        inds = range(len(lst))
        inds_empty = [i for i in inds if lst[i] == 0]
        if inds_empty == []:         # no empty cells
            return np.array([1]+lst)  # stay put
        else:
            ind_choice = np.random.choice(inds_empty)
            lst[ind_choice] = 1
            return np.array([0]+lst)
