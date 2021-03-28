import numpy as np
from cell_automata import CA


class RandomWalk(CA):
    def walk_and_update_multi(self, arr, n=1):
        out = [arr]
        for _ in range(n):
            out.append(walk_and_update(out[-1], self.num_nbrs))
        return out

    def make_grid(self, size, num_agents):
        agents = np.arange(1, num_agents+1)
        arr = np.zeros(size**2, dtype=int)
        arr[:num_agents] = agents
        np.random.shuffle(arr)
        return arr.reshape((size, size))


def make_index_arrays(arr, num_nbrs):
    ca = CA(num_nbrs)
    a = np.indices(arr.shape)
    rows = ca.rotate_array(a[0])
    cols = ca.rotate_array(a[1])
    out = np.stack((rows, cols), axis=1)
    return out


def get_nbrs_indices(arr, index, num_nbrs):
    index_nbrs = make_index_arrays(arr, num_nbrs)
    i, j = index
    rows = index_nbrs[:, 0, i, j]
    cols = index_nbrs[:, 1, i, j]
    return np.array((rows, cols))


def walk(val, arr):
    nbrs = np.copy(arr)
    inds_empty = np.where(nbrs == 0)[0]
    if inds_empty.size > 0:
        c = np.random.choice(inds_empty)
        nbrs[c] = val
    return val, nbrs


def walk_and_update(arr, num_nbrs):
    grid = np.copy(arr)
    indices = np.nonzero(grid)
    for index in np.nditer(indices):
        inds = get_nbrs_indices(arr, index, num_nbrs)
        nbrs = grid[inds[0], inds[1]]
        val = grid[index]
        val_new, nbrs = walk(val, nbrs)
        grid[index] = val_new
        grid[inds[0], inds[1]] = nbrs
    return grid - arr
