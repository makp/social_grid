import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


#class Visualize:

def rgb_convert(arr, dic):
    """Replace color names with RGB values according to dictionary 'dic', and apply the resulting dictionary to each element of a 2D-array."""
    gen = (colors.to_rgb(val) for val in dic.values())
    vals = np.array(tuple(gen))
    keys = np.array(tuple(dic.keys()))
    n_rows, n_colums = arr.shape
    arr_new = np.empty((n_rows, n_colums, 3))  # add extra array to store RGB color
    for key,val in zip(keys,vals):
        arr_new[arr==key] = val
    return arr_new

def show_single(arr,dic,ax=None):
    """Show array."""
    arr_new = rgb_convert(arr, dic)
    ax = ax or plt.gca()
    out = ax.imshow(arr_new)
    return out

def show_multiple(arrs,dic,axs):
    out = []
    for ax,arr in zip(axs, arrs):
        out.append(show_single(arr,dic,ax))
    return out


# fig, axs = plt.subplots(nrows=1, ncols=5)
# fig.set_title("")

# plt.tight_layout()
# plt.show()
