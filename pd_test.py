import numpy as np
import matplotlib.pyplot as plt
from pd_game import PD
from show_array import Show

pd = PD(11,2,1)                   # only one cheater in the middle
vis = Show(pd.cdic, pd.cdic_hist)  # convert dics to RGB

ca0 = pd.create_init()

series = pd.run(ca0,10)

fig,axs = plt.subplots(5,2)
vis.show_tuple(series,axs,True)
