import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Show:
    def __init__(self, cdic, cdic_hist):
        self.cdic = rgb_convert_dic(cdic)
        self.cdic_hist = rgb_convert_dic(cdic_hist)

    def show(self,c,axs):
        if type(c)==np.ndarray:  # single CA
            return show_single(c,ax,self.dic)
        elif type(c)==tuple:     # multiple CA
            return show_multi(lst,axs,self.dic)

    def show_with_hist(self,arrs,axs):
        arrs_new = rgb_convert_with_hist(arrs,self.dic_hist)
        out = []
        for ax,arr in zip(axs, arrs_new):
            out.append(ax.imshow(arr))
        return out


def rgb_convert_with_hist(larrs, dic):
    """"""
    gen = pair_arrays(larrs)
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

def show_multi(t_arrs,axs,dic):
    """Assign matplotib AxesImage representing the arrays in the tuple 't' to axes 'axs.'"""
    gen = (show_single(arr,ax,dic) for arr,ax in zip(t_arrs,axs))
    return tuple(gen)

def show_single(arr,ax,dic):
    """Assign matplotib AxesImage representing the 2D-array using dictionary 'dic' to 'ax.'"""
    arr_new = rgb_convert_array(arr, dic)
    out = ax.imshow(arr_new)
    return out

def rgb_convert_array(arr, dic):
    """Returns an array that replaces the values of the original 2D-array 'arr' with RGB colors according to dictionary 'dic.'"""
    arr_new = np.empty((*arr.shape, 3))  # add extra array to store RGB color
    for key in dic.keys():
        arr_new[arr==key] = dic[key]
    return arr_new

def rgb_convert_dic(dic):
    """Return a new version of dictionary 'dic' in which dic.values() are RGB colors intead of color names"""
    keys = dic.keys()
    vals_new = (colors.to_rgb(val) for val in dic.values())
    dic_new = {key: val for key,val in zip(keys, vals_new)}
    return dic_new

# fig, axs = plt.subplots(nrows=1, ncols=5)

# fig.set_title("")
# plt.tight_layout()
# plt.show()