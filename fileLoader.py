import pandas as pd
import matplotlib.pyplot as plt

#df_bitcoinity = pd.read_csv('data/bitcoinity_data.csv')
df_coindesk = pd.read_csv('data/coindesk-ETH-close_data-2015-08-31_2017-05-22.csv')
#df_bitcoinity.plot(style=['o','rx'])
df_coindesk.plot(style=['o','rx'])
plt.show()
input("Press Enter to continue...")
