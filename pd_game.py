import numpy as np
from neighbors import Neighbors
from helper_funcs import lower_zip

# Cmds for testing:
# from pd_game import PD; teste = PD(10, 1.4, 0.5)


class PD:
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

    def run_once(self,ca):
        """Select the strategy with the highest payoff in the Moore neighborhood."""
        t, l = self.t_pay, self.length
        nbrs, pa = payoff_array(t, ca)
        arr = Neighbors(pa,8).list_neighbors()
        b = np.array(tuple(pick_one(row) for row in arr))
        return nbrs[b].reshape(l,l)

    # FIXME: For the two funcs below, make sure the elements of the array are tuples --- otherwise I won't be able to use a dictionary to assign them colors
    # def run_once_with_hist(self,ca):
    #     """Run run_once() but keep history by storing the previous and the current values within tuples."""
    #     ca_next = self.run_once(ca)
    #     gen = lower_zip(ca,ca_next)  # zip their rows
    #     return np.array(tuple(gen))

    # def run_multi(self, ca, n, hist=None):
    #     """Run the game for 'n' time steps and return the resulting arrays with 'ca' as the initial array. The optional keyword argument specifies whether to keep history or not."""
    #     if hist == 'True':
    #         func = self.run_once_with_hist
    #     else:
    #         func = self.run_once
    #     count, out = 0, [ca]
    #     while count < n:
    #         ca_next = func(out[-1])
    #         out.append(ca_next)
    #         count += 1
    #     return out


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
def payoff_array(t_pay, ca):
    """Returns a tuple with two members. The first member is an array containing every cell of 'ca' followed by its Moore neighbors. The second member of the tuple is an array storing the payoff_total for each cell."""
    nbrs = Neighbors(ca, 8).list_neighbors()
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
