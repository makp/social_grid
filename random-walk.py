import numpy as np
from cell_automata import CA

ca = CA(4)                      # von Neumann nbr
arr = np.zeros((5, 9), dtype=int)
arr[2, 4:7] = 1


def make_nbrs_indices(arr):
    a = np.indices(arr.shape)
    grid = np.stack(a, axis=-1)
    nbrs = ca.rotate_array(grid)
    return nbrs


nbrs_indices = make_nbrs_indices(arr)


def get_nbrs_indices(index):
    i, j = index
    inds = [tuple(ind) for ind in nbrs_indices[:, i, j]]
    return inds


def update_walk(arr):
    arr_new = np.copy(arr)
    for index, x in np.ndenumerate(arr_new):
        if x == 1:
            inds = get_nbrs_indices(index)
            nbrs = [arr[ind] for ind in inds]
            x_new, nbrs_new = walk(nbrs)
            arr_new[index] = x_new
            for i, n in zip(inds, nbrs_new):
                arr_new[i] = n
    return arr_new // 2


def update_walk_multi(arr, n):
    out = [arr]
    for _ in range(n):
        out.append(update_walk(out[-1]))
    return out


def walk(nbrs):
    r = range(len(nbrs))
    inds_empty = [i for i in r if nbrs[i] == 0]
    if inds_empty:              # empty spots available
        c = np.random.choice(inds_empty)
        out = (1, nbrs[:c]+[2]+nbrs[c+1:])
    else:
        out = (2, nbrs)         # stay put
    return out
