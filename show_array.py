import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Show:
    def __init__(self, cdic, cdic_hist):
        self.cdic = cdic
        self.cdic_hist = cdic_hist

    def show(self,c,axs):
        if type(c)==np.ndarray:  # single CA
            return show_single(c,ax,self.dic)
        elif type(c)==list:     # multiple CA
            return show_multi(lst,axs,self.dic_hist)

    def show_with_hist(self,arrs,axs):
        arrs_new = rgb_convert_with_hist(arrs,self.dic_hist)
        out = []
        for ax,arr in zip(axs, arrs_new):
            out.append(ax.imshow(arr))
        return out


def show_single(arr,ax,dic):
    """Show single array."""
    arr_new = rgb_convert(arr, dic)
    out = ax.imshow(arr_new)
    return out

def show_multi(lst,axs,dic):
    """Assign matplotib AxesImage of the arrays in the list 'lst' to axes 'axs.'"""
    out = []
    for arr,ax in zip(lst,axs):
        out.append(self.show_single(arr,ax,dic))
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
    gen = pair_arrays(larrs)
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


def pair_arrays(lst):
    """Returns a generator that pairs the list of arrays 'lst.'"""
    rg = range(len(lst)-1)
    gen = ([lst[i], lst[i+1]] for i in rg)
    return gen


# fig, axs = plt.subplots(nrows=1, ncols=5)

# fig.set_title("")
# plt.tight_layout()
# plt.show()