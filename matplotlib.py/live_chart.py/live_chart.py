
import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd
from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(-10,10))


    plt.cla()
    plt.plot(x_vals, y_vals, label= 'chanel 1')
    plt.grid()
    plt.ylim((-10, 10))

ani = FuncAnimation(plt.gcf(),animate, interval=100)

plt.show()