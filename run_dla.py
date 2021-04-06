import numpy as np
from update import UpdateAll
from random_walk import RandWalk

side = 100
num_walkers = side
time_steps = 2

agg = UpdateAll(side, 8)        # aggregation nbr
rw = RandWalk(side)             # random walk

init = rw.create_init(num_walkers, False)
init[side//2, side//2] = 2        # sticky cell


def stick(cell, nbrs):
    if cell == 2:             # sticky cell
        b = nbrs == 1         # non-sticky nbrs
        if np.any(b):
            nbrs[b] = 2
    return nbrs


def run_once(init):
    ca1 = agg.update_nbrs(init, stick)
    return rw.run(ca1)


def run(init, n=1):
    out = [init]
    for _ in range(n):
        out.append(run_once(out[-1]))
    return out


out = run(init, 100)
