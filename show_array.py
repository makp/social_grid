import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Visualize:
    def __init__(self, dic):
        self.dic = dic

    def show_single(self,arr,ax):
        """Show array."""
        arr_new = rgb_convert(arr, self.dic)
        out = ax.imshow(arr_new)
        return out

    def show_multiple(self,arrs,axs):
        out = []
        for ax,arr in zip(axs, arrs):
            out.append(self.show_single(arr,ax))
        return out


def rgb_convert(arr, dic):
    """Replace color names with RGB values according to dictionary 'dic', and apply the resulting dictionary to each element of a 2D-array."""
    keys = tuple(dic.keys())
    vals = (colors.to_rgb(val) for val in dic.values())
    n_rows, n_colums = arr.shape
    arr_new = np.empty((n_rows, n_colums, 3))  # add extra array to store RGB color
    for key,val in zip(keys,vals):
        arr_new[arr==key] = val
    return arr_new

def rgb_covert_with_hist(arrs, dic):
    """"""
    # To test whether history is involved, I could check the type.
    arrs_paired = arrs          # FIXME: create function to pair arrays an arrs
    keys = np.array(tuple(dic.keys()))
    vals = (colors.to_rgb(val) for val in dic.values())
    n_rows, n_colums = arrs[0].shape
    arr_new = np.empty((n_rows, n_colums, 3))
    gen = np.array(tuple(lower_zip(arrs[0],arrs[1])))
    for key,val in zip(keys,vals):
        b = np.logical_and(arrs[0]==key[0], arrs[1]==key[1])
        arr_new[b] = val
    return arr_new

# fig, axs = plt.subplots(nrows=1, ncols=5)
# fig.set_title("")

# plt.tight_layout()
# plt.show()
