import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('input.csv')
df.plot.line(x='T',y=['D1','D2'], grid=True, title = 'TITLE', ylim = (-70,-50) )

plt.show()
