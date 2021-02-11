import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class Show:
    def __init__(self, cdic, cdic_hist):
        self.cdic = rgb_convert_dic(cdic)
        self.cdic_hist = rgb_convert_dic(cdic_hist)

    def show_array(self,arr,ax):
        """"""
        return ax.imshow(rgb_convert_array(arr, self.cdic))

    def show_tuple(self,t_arrs,axs,hist=False):
        """"""
        if hist:
            t = rgb_convert_with_hist(t_arrs,self.cdic_hist)
        else:
            t = rgb_convert_sans_hist(t_arrs,self.cdic)
        gen = (ax.imshow(arr) for ax,arr in zip(axs.flatten(),t))
        return tuple(gen)

def rgb_convert_with_hist(t_arrs, dic):
    """Group consecutive arrays from t_arrs into pairs, and then transform each pair into an array with RGB values according to dictionary 'dic.'"""
    gen = pair_arrays(t_arrs)
    out = []
    arr_new = np.empty((*t_arrs[0].shape, 3))
    for g in gen:               # iterate through pairs of arrays
        for key in dic.keys():
            arr_bool = np.logical_and(g[0]==key[0], g[1]==key[1])
            arr_new[arr_bool] = dic[key]
        out.append(arr_new.copy())
    return tuple(out)

def rgb_convert_sans_hist(t_arrs, dic):
    gen = (rgb_convert_array(arr,dic) for arr in t_arrs)
    return tuple(gen)

def pair_arrays(t_arrs):
    """Returns a generator that pairs consecutive arrays in the tuple 't_arrs.'"""
    rg = range(len(t_arrs)-1)
    gen = ((t_arrs[i], t_arrs[i+1]) for i in rg)
    return gen

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