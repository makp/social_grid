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

    def run(self, ca, n=1, method='lazy'):
        """Run the game for 'n' timesteps and return the resulting arrays as a tuple."""
        t = self.t_pay
        count, out = 0, [ca]
        while count < n:
            ca_next = run_once(out[-1], t, method)
            out.append(ca_next.copy())
            count += 1
        return tuple(out)


cell = CA(8)

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
def run_once(ca, t_pay, m):
    pa = payoff_array(ca,t_pay)
    pa_nbrs = cell.list_nbrs(pa)
    ca_nbrs = cell.list_nbrs(ca)
    z = zip(pa_nbrs, ca_nbrs)
    gen = (pick_strat(a1,a2, m) for r1,r2 in z for a1,a2 in zip(r1,r2))
    out = np.array(tuple(gen)).reshape(ca.shape)
    return out

def pick_strat(arr_pay, arr_strat, method):
    b = max_bool(arr_pay)
    if sum(b) == 1:
        return arr_strat[b][0]
    elif sum(b) > 1:            # more than one max val found
        return dic_funcs[method](arr_strat, b)

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

dic_funcs = {'lazy': pick_lazy, 'coop_bias': pick_coop_bias}

def max_bool(array_1d):
    """Return an boolean 1D-array with 'True' for the maximum value and 'False' otherwise."""
    m = max(array_1d)
    array_bool = array_1d == m
    return array_bool

def payoff_array(ca, t_pay):
    """Returns a tuple with two members. The first member is an array containing every cell of 'ca' followed by its Moore neighbors. The second member of the tuple is an array storing the payoff for each cell (payoff_cell)."""
    func = lambda *xs: payoff_cell(t_pay, *xs)
    return cell.map_nbrs(ca, func)


def payoff_cell(t_pay, focal, *nbrs):
    '''Return total payoff for a focal cell due to pairwise interactions with neighbors.'''
    total = sum((focal, *nbrs))
    if focal == 1:              # cooperators
        pay = total
    elif focal == 0:            # defectors
        pay = t_pay*total
    return pay


