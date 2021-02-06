def lower_zip(arr0, arr1):
    """Returns a generator by zipping the rows of two 2D-arrays."""
    gen = (tuple(zip(x,y)) for x,y in zip(arr0,arr1))  # zip rows
    return gen