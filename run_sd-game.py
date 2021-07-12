import matplotlib.pyplot as plt
from sd_game import SD
from show_array import Show

sd = SD(2.6)                    # temptation payoff
vis = Show(sd.cdic, sd.cdic_hist)  # convert dics to RGB

ca0 = sd.create_init(50, .3)    # create init array

n_steps = 33
series = sd.run(ca0, n_steps, 'indifferent')

if n_steps < 15:
    n_rows = n_steps//3
    arr = series
else:
    arr = series[::5]       # every fifth member
    n_rows = (n_steps//5)//3

fig, axs = plt.subplots(n_rows, 3, figsize=(10, 10))
[ax.axis('off') for ax in axs.flatten()]
vis.show_tuple(arr, axs, False)

plt.show()
