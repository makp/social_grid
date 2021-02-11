import numpy as np
from neighbors import Neighbors
from helper_funcs import lower_zip

# Cmds for testing:
# from pd_game import PD; pd = PD(10, 1.4, 0.5)


class PD:
    cdic = {1:'blue',
            0:'red'}

    cdic_hist = {(0,0): 'red',
                 (1,1): 'blue',
                 (0,1): 'green',
                 (1,0): 'yellow'}

    def __init__(self, l, t, p):
        self.length = l         # CA length
        self.t_pay = t          # temptation for defecting
        self.prob = p           # initial prob of cooperating

    def create_init(self):
        """Create the initial array."""
        if 0<self.prob<1:
            return init_random(self.prob,self.length)
        elif self.prob == 1:
            return init_mid(self.length)

    def run(self, ca, n=1):
        """Run the game for 'n' timesteps and return the resulting arrays as a tuple."""
        t, l = self.t_pay, self.length
        count, out = 0, [ca]
        while count < n:
            ca_next = run_once(out[-1], t, l)
            out.append(ca_next)
            count += 1
        return tuple(out)

#
# Initial array
#
def init_random(p,l):
    """Generate a random array with 0s (defectors) and 1s (coorperators) with probability '1-prob' and 'prob,' respectively."""
    return np.random.choice(2, size=(l,l), p=[1-p, p])
        
def init_mid(l):
    """Generate array with a single defector in the middle of the grid---or approximately the middle when length is an even number."""
    m = (l-1)//2
    arr = np.ones((l,l))
    arr[m,m] = 0
    return arr

#
# Functions used to run one time step
#
def run_once(ca, t_pay, l):
    """Select the strategy with the highest payoff in the Moore neighborhood."""
    nbrs, pa = payoff_array(t_pay, ca)
    arr = Neighbors(8).list_neighbors(pa)
    b = np.array(tuple(pick_one(row) for row in arr))
    return nbrs[b].reshape(l,l)

def payoff_array(t_pay, ca):
    """Returns a tuple with two members. The first member is an array containing every cell of 'ca' followed by its Moore neighbors. The second member of the tuple is an array storing the payoff_total for each cell."""
    nbrs = Neighbors(8).list_neighbors(ca)
    s = ca.shape
    t = tuple(payoff_total(*row, t_pay) for row in nbrs)
    return nbrs, np.array(t).reshape(s)

def payoff_total(t_pay, focal, *nbrs):
    '''Return total payoff for a focal cell due to pairwise interactions with neighbors.'''
    total = sum((focal, *nbrs))
    if focal == 1:              # cooperators
        pay = total
    elif focal == 0:            # defectors
        pay = t_pay*total
    return pay

def pick_one(array_1d):
    """Returns True for only of the max element found in the 1D array. If array contains multiple entries equal to the maximum value, choose one of these entries randomly."""
    i_all = np.array(tuple(range(array_1d.size)))  # indexes
    m = max(array_1d)                              # max value
    b = array_1d == m
    i_mxs = i_all[b]            # indexes for max value entries
    if len(i_mxs) > 1:          # more than one entry
        c = np.random.choice(i_mxs)
        return i_all == c
    return b


