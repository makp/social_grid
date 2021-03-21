import numpy as np
from cell_automata import CA

ca = CA(4)
arr = np.zeros((5, 9))
arr[2, 4] = 1


def choose_cell(*nbrs):
    lst = list(nbrs)
    inds = range(len(lst))
    inds_empty = [i for i in inds if lst[i] == 0]
    if inds_empty == []:        # no empty cells
        out = [1] + lst         # stay put
        return out
    else:
        ind_choice = np.random.choice(inds_empty)
        lst[ind_choice] = 1
        out = [0] + lst
        return out
