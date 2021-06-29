import numpy as np
from update import UpdateCell


class PD:
    cdic = {1: 'blue',
            0: 'red'}

    cdic_hist = {(0, 0): 'red',
                 (1, 1): 'blue',
                 (0, 1): 'green',
                 (1, 0): 'yellow'}

    def __init__(self, t):
        self.t_pay = t          # temptation for defecting

    def create_init(self, size, prob=1):
        """Create the initial array."""
        if 0 < prob < 1:
            return init_random(prob, size)
        elif prob == 1:
            return init_mid(size)

    def run(self, ca, n=1, method='lazy'):
        """Run PD game for 'n' timesteps and return the resulting
        arrays as a tuple."""
        t = self.t_pay
        out = [ca]
        for _ in range(n):
            ca_next = run_once(out[-1], t, method)
            out.append(ca_next.copy())
        return tuple(out)


# Class instance
nbr = UpdateCell(8)


#
# Initial array
#
def init_random(p, s):
    """Generate a random array with 0s (defectors) and 1s
    (coorperators) with probability '1-prob' and 'prob,'
    respectively."""
    return np.random.choice(2, size=(s, s), p=[1-p, p])


def init_mid(s):
    """Generate array with a single defector in the middle of the
    grid---or approximately the middle when side length is an even
    number."""
    m, arr = (s-1)//2, np.ones((s, s))
    arr[m, m] = 0
    return arr


#
# Functions used to run one time step
#

def run_once(ca, t_pay, m):
    a_pay = nbr.cell_and_nbrs(payoff_array(ca, t_pay))
    a_str = nbr.cell_and_nbrs(ca)
    ca_new = np.empty(ca.shape)
    for index in np.ndindex(ca.shape):
        ca_new[index] = strategy(a_pay[index], a_str[index], m)
    return ca_new


def payoff_array(ca, t_pay):
    return nbr.update_cell(ca, lambda arr: payoff(t_pay, arr))


def payoff(t_pay, arr):
    """Returns cell payoff from pairwise interactions with neighbors."""
    total = np.sum(arr)
    return total if arr[0] else t_pay*total


def strategy(arr_pay, arr_strat, method):
    m = np.max(arr_pay)
    b = arr_pay == m
    if np.sum(b) == 1:
        return arr_strat[b][0]
    elif np.sum(b) > 1:            # more than one max val
        return dic_funcs[method](arr_strat, b)


#
# Strategies for when defecting and cooperating yields the same payoff
#

def pick_lazy(arr_strat, b):
    if b[0]:                    # if focal cell is one of the maxs...
        return arr_strat[0]     # stick to it
    else:                       # Otherwise...
        a = arr_strat[b]
        return np.random.choice(a)  # pick one of the strats randomly


def pick_coop_bias(arr_strat, b):
    a = arr_strat[b]
    if 1 in a:
        return 1
    else:
        return 0


def pick_defect_bias(arr_strat, b):
    a = arr_strat[b]
    if 0 in a:
        return 0
    else:
        return 1


def pick_indifferent(arr_strat, b):
    a = arr_strat[b]
    return np.random.choice(a)


dic_funcs = {'lazy': pick_lazy,
             'coop_bias': pick_coop_bias,
             'defect_bias': pick_defect_bias,
             'indifferent': pick_indifferent}
