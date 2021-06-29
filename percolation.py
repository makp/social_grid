import numpy as np
import matplotlib.pyplot as plt
from neighbor import Nbr

side, p0, nbr_type = 10, 0.58, 8

np.random.seed(999)

arr0 = np.random.choice([0, 1], size=(side, side), p=[1-p0, p0])


def tag_clusters(arr):
    arr2d = np.copy(arr)
    tag_new = 2
    for (i, j), val in np.ndenumerate(arr2d):
        if val == 1:
            nbr_tags = find_nbr_tags(arr2d, i, j)
            if nbr_tags.any():
                arr2d[i, j] = min(nbr_tags)
            else:
                arr2d[i, j] = tag_new
                tag_new += 1
    return arr2d


def create_inds(shape):
    a = np.stack(np.indices(shape), axis=-1)
    return Nbr(4).list_nbrs(a)


def find_nbr_tags(arr, i, j):
    inds = create_inds(arr.shape)[i, j, 1:]
    nbrs = np.array([arr[tuple(ind)] for ind in inds])
    b = nbrs > 1
    return nbrs[b]


arr_clusters = tag_clusters(arr0)
plt.imshow(arr_clusters)
plt.show()
