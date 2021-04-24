import numpy as np
from neighbor import Nbr


class RandWalk(Nbr):
    """Models multiple random walkers in a cellular automata.

    Args:
    - side: CA side length
    - num_nbrs (optional): number of neighbors (4 or 8)

    Assumptions:
    - Two walkers cannot occupy the same cell.
    - Periodic boundary conditions."""

    def __init__(self, side, num_nbrs=4):
        self.side = side
        self.num_nbrs = num_nbrs
        self.imap = self.inds_dict(self.side)

    def run(self, arr, n=1, cond=None):
        if n == 1:
            out = walk(arr, self.imap, cond)
        else:
            out = [arr]
            for _ in range(n):
                out.append(walk(out[-1], self.imap, cond))
        return out

    def create_init(self, num_walkers, tag=True):
        if tag:
            walkers = np.arange(1, num_walkers+1)  # differentiate walkers
        else:
            walkers = np.ones(num_walkers)  # all walkers are 1s
        arr = np.zeros(self.side**2, dtype=int)
        arr[:num_walkers] = walkers
        np.random.shuffle(arr)
        return arr.reshape((self.side, self.side))


def walk(a, dic, cond):
    if cond:
        arr = np.stack(np.indices(a.shape), axis=-1)
        inds = arr[a == cond]
    else:
        inds = np.stack(np.nonzero(a), axis=-1)
    a_new = np.copy(a)
    for i, j in inds:
        ind_nbrs = dic[i, j]
        walker, nbrs = a[i, j], a_new[ind_nbrs]
        a_new[i, j], a_new[ind_nbrs] = choose(walker, nbrs)
    return a_new


def choose(walker, nbrs):
    """Choose an empty cell to move to."""
    ind_zeros = np.where(nbrs == 0)[0]
    if ind_zeros.size > 0:
        c = np.random.choice(ind_zeros)
        nbrs[c], walker = walker, 0
    return walker, nbrs
