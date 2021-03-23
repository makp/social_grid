import matplotlib.pyplot as plt
from pd_game import PD
from show_array import Show

pd = PD(1.85)                      # temptation payoff
# With temptation equal to 1.85, the resulting pattern
# is invariant across the different methods listed in
# dic_funcs. That's probably bc ties in payoff are uncommon.

vis = Show(pd.cdic, pd.cdic_hist)  # convert dics to RGB

ca0 = pd.create_init(51, 1)          # only one cheater in the middle

n_steps = 12
series = pd.run(ca0, n_steps, 'indifferent')

if n_steps < 15:
    n_rows = n_steps//3
    arr = series
else:
    arr = series[::5]       # every fifth member
    n_rows = (n_steps//5)//3

fig, axs = plt.subplots(n_rows, 3, figsize=(10, 10))
[ax.axis('off') for ax in axs.flatten()]
vis.show_tuple(arr, axs, True)

plt.show()
