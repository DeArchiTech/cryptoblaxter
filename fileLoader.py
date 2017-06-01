import pandas as pd
import matplotlib.pyplot as plt

def plotAll():
    plot('data/bitcoinity_data.csv',"Time","USD","Bitcoin 2010 - Current")
    plot('data/coindesk-ETH-close_data-2015-08-31_2017-05-22.csv',"Time","USD","ETH 2015 - Current")

def plot(input, xaxis, yaxis, title):
    df_coindesk = pd.read_csv(input)
    ax = df_coindesk.plot(style=['o', 'rx'])
    ax.set_xlabel(xaxis)
    ax.set_ylabel(yaxis)
    plt.title(title)
    plt.show()
