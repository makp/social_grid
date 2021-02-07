import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


#class Visualize:

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

def show_single(arr,dic,ax=None):
    """Plot array."""
    ax = ax or plt.gca()
    arr_new = rgb_convert(arr, dic)
    out = ax.imshow(arr_new)
    return out

# fig, axs = plt.subplots(nrows=1, ncols=5)
# fig.set_title("")

# plt.tight_layout()
# plt.show()
