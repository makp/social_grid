import numpy as np
from cell_automata import CA

class PD(CA):
    cdic = {1:'blue',
            0:'red'}

    cdic_hist = {(0,0): 'red',
                 (1,1): 'blue',
                 (0,1): 'green',
                 (1,0): 'yellow'}

    def __init__(self, t):
        super().__init__(8)     # Use Moore nbr
        self.t_pay = t          # temptation for defecting

    def create_init(self, l, prob):
        """Create the initial array."""
        if 0<prob<1:
            return init_random(prob,l)
        elif prob == 1:
            return init_mid(l)

    # def run(self, ca, n=1):
    #     """Run the game for 'n' timesteps and return the resulting arrays as a tuple."""
    #     t, l = self.t_pay, self.length
    #     count, out = 0, [ca]
    #     while count < n:
    #         ca_next = run_once(out[-1], t)
    #         out.append(ca_next.copy())
    #         count += 1
    #     return tuple(out)

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
def run_once(ca, t_pay):
    """Select the strategy with the highest payoff in the Moore neighborhood."""
    nbrs, pa = payoff_array(ca, t_pay)
    s = ca.shape
    arr = Neighbors(8).list_neighbors(pa)  # (ca.size, 9)
    b = np.array(tuple(pick_one(row) for row in arr))
    return nbrs[b].reshape(*s)

def payoff_array(ca, t_pay):
    """Returns a tuple with two members. The first member is an array containing every cell of 'ca' followed by its Moore neighbors. The second member of the tuple is an array storing the payoff for each cell (payoff_cell)."""
    nbrs = Neighbors(8).list_neighbors(ca)
    s = ca.shape
    t = tuple(payoff_cell(t_pay,*row) for row in nbrs)
    return nbrs, np.array(t).reshape(s)

def payoff_cell(t_pay, focal, *nbrs):
    '''Return total payoff for a focal cell due to pairwise interactions with neighbors.'''
    total = sum((focal, *nbrs))
    if focal == 1:              # cooperators
        pay = total
    elif focal == 0:            # defectors
        pay = t_pay*total
    return pay

def pick_one(array_1d):
    """Returns True for only of the max element found in the 1D array. If array contains multiple entries equal to the maximum value, choose one of these entries randomly."""
    i_all = np.arange(array_1d.size)  # indexes
    m = max(array_1d)                 # max value
    bool_array = array_1d == m
    i_mxs = i_all[bool_array]   # indexes for max value entries
    if len(i_mxs) > 1:          # >1 max value
        if i_mxs[0]==0:         # select focal cell if in i_mxs
            c = 0
        else:
            c = np.random.choice(i_mxs)
        return i_all == c
    return bool_array
