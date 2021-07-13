import matplotlib.pyplot as plt
from sd_game import SD
from show_array import Show

sd = SD(2.6)                    # temptation payoff
vis = Show(sd.cdic, sd.cdic_hist)  # convert dics to RGB

ca0 = sd.create_init(50, .8)    # create init array

n_steps = 40
series = sd.run(ca0, n_steps, 'indifferent')

fig, axs = plt.subplots(1, 2, figsize=(10, 10))
[ax.axis('off') for ax in axs.flatten()]
vis.show_tuple(series[::n_steps], axs, False)

plt.tight_layout()
plt.show()
