import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

GHG_emissions = pd.read_csv("GHG_emissions.csv")
data = GHG_emissions[[str(x) for x in range(1990, 2020)]].to_numpy()
#plt.plot(range(1990, 2020), data.T)
#plt.legend(GHG_emissions["Sector"])

sector_sums = {i:sum(data[i,:]) for i in range(data.shape[0])}
low_sector_idxs = sorted(sector_sums, key=sector_sums.get)[:-9]
top_sector_idxs = sorted(sector_sums, key=sector_sums.get)[-9:]

plt.plot(np.arange(1990,2020), data[top_sector_idxs].T)
plt.plot(np.arange(1990,2020), np.sum(data[low_sector_idxs], axis=0).T)
plt.legend(list(GHG_emissions["Sector"][top_sector_idxs])+["Other"])