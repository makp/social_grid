import numpy as np
import matplotlib.pyplot as plt
from update import UpdateAll
from random_walk import RandWalk

side = 300
num_walkers = side**2//8
time_steps = 1500

agg = UpdateAll(side, 8)        # aggregation nbr
rw = RandWalk(side)             # random walk

init = rw.create_init(num_walkers, False)  # all walkers labeled as 1
init[side//2, side//2] = 2                 # sticky cell


def stick(cell, nbrs):
    if cell == 2:             # sticky cell
        b = nbrs == 1         # non-sticky nbrs
        if np.any(b):
            nbrs[b] = 2
    return nbrs


def run_once(init):
    ca1 = agg.update_nbrs(init, stick)
    return rw.run(ca1, 1, 1)


def run(init, n=1):
    out = [init]
    for _ in range(n):
        out.append(run_once(out[-1]))
    return out


def run_sans_memory(init, n=1):
    out = init
    for _ in range(n):
        out = run_once(out)
    return out


res = run_sans_memory(init, time_steps)
plt.axis('off')
plt.imshow(res)

plt.show()
