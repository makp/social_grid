import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from random_walk import RandomWalk

randw = RandomWalk(4)

num_agents = 10
size = 100
time_steps = 50

# Make initial array
arr = randw.make_grid(size, num_agents)

# Run simulation
arrays = randw.walk_and_update_multi(arr, time_steps)

# Display arrays
fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])


def animate():
    ims = []
    for a in arrays:
        a = a.astype('float64')
        a[a == 0] = np.nan
        im = ax.imshow(a, vmin=0)
        ims.append([im])
    return ims


ani = animation.ArtistAnimation(fig, animate())
# ani.save('animation_random_walk.mp4')

plt.show()
