import numpy as np
from neighbor import Nbr


class RandWalk(Nbr):
    """Models multiple random walkers in a cellular automata.

    Args:
    - dim: CA dimension
    - num_nbrs (optional): number of neighbors (4 or 8)

    Assumptions:
    - Two walkers cannot occupy the same cell.
    - Periodic boundary conditions."""
    def __init__(self, dim, num_nbrs=4):
        self.dim = dim
        self.num_nbrs = num_nbrs
        self.ind_arr = self.get_inds_nbrs(self.dim)

    def walk_multi(self, arr, n=1):
        out = [arr]
        for _ in range(n):
            out.append(walk(out[-1], self.ind_arr))
        return out

    def make_grid(self, num_walkers, tag=True):
        if tag:
            walkers = np.arange(1, num_walkers+1)
        else:
            walkers = np.ones(num_walkers)
        arr = np.zeros(self.dim**2, dtype=int)
        arr[:num_walkers] = walkers
        np.random.shuffle(arr)
        return arr.reshape((self.dim, self.dim))


def walk(a, ia):
    ind_walkers = np.nonzero(a)
    a_new = np.copy(a)
    for i, j in np.nditer(ind_walkers):
        walker = a[i, j]
        ind_nbrs = tuple(ia[:, k, i, j] for k in range(2))
        nbrs = a_new[ind_nbrs]
        a_new[i, j], a_new[ind_nbrs] = choose(walker, nbrs)
    return a_new - a


def choose(walker, nbrs):
    ind_zeros = np.where(nbrs == 0)[0]
    if ind_zeros.size > 0:
        c = np.random.choice(ind_zeros)
        nbrs[c] = walker
    else:
        walker *= 2
    return walker, nbrs
