import numpy as np


def coord(n):
    out = set()
    for i, j in zip(range(n+1), range(n, -1, -1)):
        out = out.union({(i, j), (-i, j), (i, -j), (-i, -j)})
    return out


def nbrs_only(arr, n):
    t = rotate_arr(arr, n)
    return np.stack(t, axis=2)


def rotate_arr(arr, n):
    nbr = coord(n)
    return tuple(rotate2d(arr, *t) for t in nbr)


def rotate1d(arr1d, s):
    """Rotate 1D array.

The returned array is a copy of the 1D array `arr1d' after rotating
its elements `s' steps."""
    return np.concatenate((arr1d[-s:], arr1d[:-s]))


def rotate2d(arr2d, i, j):
    """Rotate 2D array.

The returned array is a copy of `arr2d' after rotating its rows i
steps and the members of each row by j steps."""
    arr = rotate1d(arr2d, i)                    # rotate rows
    t = tuple(rotate1d(row, j) for row in arr)  # rotate elements
    return np.array(t)
