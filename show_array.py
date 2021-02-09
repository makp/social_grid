import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Visualize:
    def __init__(self, dic):
        self.dic = dic          # TODO: Change attribute

    def show_single(self,arr,ax):
        """Show array."""
        arr_new = rgb_convert(arr, self.dic)
        out = ax.imshow(arr_new)
        return out

    # TODO: Combine the following two functions
    def show_multiple(self,arrs,axs):
        out = []
        for ax,arr in zip(axs, arrs):
            out.append(self.show_single(arr,ax))
        return out

    def show_multiple_with_hist(self,arrs,axs,dic):
        arrs_new = rgb_convert_with_hist(arrs,dic)
        out = []
        for ax,arr in zip(axs, arrs_new):
            out.append(ax.imshow(arr))
        return out

# TODO: Combine the following two functions
def rgb_convert(arr, dic):
    """Replace color names with RGB values according to dictionary 'dic', and apply the resulting dictionary to each element of a 2D-array."""
    keys = dic.keys()
    vals = (colors.to_rgb(val) for val in dic.values())
    n_rows, n_cols = arr.shape
    arr_new = np.empty((n_rows, n_cols, 3))  # add extra array to store RGB color
    for key,val in zip(keys,vals):
        arr_new[arr==key] = val
    return arr_new

def rgb_convert_with_hist(larrs, dic):
    """"""
    gen = pair_larrs(larrs)
    keys = np.array(tuple(dic.keys()))
    vals = (colors.to_rgb(val) for val in dic.values())
    out = []
    nrs, ncs = larrs[0].shape
    arr_new = np.empty((nrs,ncs, 3))
    for g in gen:               # iterate through pairs of arrays
        for key,val in zip(keys,vals):
            b = np.logical_and(g[0]==key[0], g[1]==key[1])
            arr_new[b] = val
        out.append(arr_new)
    return out

def pair_larrs(larrs):
    """Returns a generator that pairs the list of arrays 'larrs.'"""
    rg = range(len(larrs)-1)
    gen = ([larrs[i], larrs[i+1]] for i in rg)
    return gen


# fig, axs = plt.subplots(nrows=1, ncols=5)
# fig.set_title("")

# plt.tight_layout()
# plt.show()
