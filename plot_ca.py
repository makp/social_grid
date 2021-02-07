import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# sim = PD(100,1.4, 0.5)
# ca_zero = sim.init
# ca_one = sim.run_once()

def rgb_convert(arr, dic):
    """Replace color names with RGB values in dictionary dic, and apply the resulting dictionary to each element of a 2D-array."""
    gen = (colors.to_rgb(val) for val in dic.values())
    vals = np.array(tuple(gen))
    keys = np.array(tuple(dic.keys()))
    n_rows, n_colums = arr.shape
    arr_new = np.empty((n_rows, n_colums, 3))  # add extra array store RGB color
    for key,val in zip(keys,vals):
        arr_new[arr==key] = val
    return arr_new



# Five horizontal images
fig, axs = plt.subplots(nrows=1, ncols=5, subplot_kw={'xticks': [], 'yticks': []})
fig.set_title("Five time steps")


plt.tight_layout()
plt.show()
