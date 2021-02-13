import numpy as np
import matplotlib.pyplot as plt
from pd_game import PD
from show_array import Show

pd = PD(2)                         # temptation
vis = Show(pd.cdic, pd.cdic_hist)  # convert dics to RGB

ca0 = pd.create_init(101,1)          # only one cheater in the middle

n_steps = 14
series = pd.run(ca0,n_steps, 'coop_bias')

if n_steps < 15:
    n_rows = n_steps//3
    arr = series
else:
    arr = series[::5]       # every fifth member
    n_rows = (n_steps//5)//3

fig,axs = plt.subplots(n_rows,3,figsize=(10,10))
vis.show_tuple(arr,axs,True)