import numpy as np
import matplotlib.pyplot as plt

side, p0 = 100, 0.5

arr0 = np.random.choice([0, 1], size=(side, side), p=[1-p0, p0])
plt.imshow(arr0)
plt.show()
