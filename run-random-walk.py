import numpy as np
from random_walk import RandomWalk

arr = np.zeros((5, 9), dtype=int)
arr[2, 4:7] = 1

RandomWalk().walk_and_update_multi(arr, 5)
