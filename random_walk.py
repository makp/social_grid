import numpy as np
from neighbor import Nbr


class RandWalk(Nbr):
    def __init__(self, dim, num_nbrs=4):
        self.dim = dim
        self.num_nbrs = num_nbrs
        self.ind_arr = self.get_inds_nbrs(self.dim)

    def walk_multi(self, arr, n=1):
        out = [arr]
        for _ in range(n):
            out.append(walk(out[-1], self.ind_arr))
        return out

    def make_grid(self, num_agents):
        agents = np.arange(1, num_agents+1)
        arr = np.zeros(self.dim**2, dtype=int)
        arr[:num_agents] = agents
        np.random.shuffle(arr)
        return arr.reshape((self.dim, self.dim))


def walk(a, ia):
    a_new = np.copy(a)
    ind_agents = np.nonzero(a_new)
    for i, j in np.nditer(ind_agents):
        ag = a[i, j]
        ind_nbrs = tuple(ia[:, k, i, j] for k in range(2))
        nbrs = a_new[ind_nbrs]
        a_new[i, j], a_new[ind_nbrs] = choose(ag, nbrs)
    return a_new - a


def choose(ag, nbrs):
    ind_zeros = np.where(nbrs == 0)[0]
    if ind_zeros.size > 0:
        c = np.random.choice(ind_zeros)
        nbrs[c] = ag
    else:
        ag *= 2
    return ag, nbrs
