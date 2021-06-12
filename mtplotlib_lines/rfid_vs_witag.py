#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    font = FontProperties()
    font.set_family('serif')
    font.set_name('Times')
    plt.yticks(fontname="Times", fontsize = "15")
    plt.xticks(fontname="Times", fontsize = "15")
    plt.legend(prop={'family': 'Times'})
    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14, 15, 16], [-54, -50.4, -45.9, -42.8, -44.8, -43.9, -45.3, -44.9, -49.8, -50.8, -50.3, -50.1, -49.6, -48.2, -49.8, -48.3, -46.1], label = "Tag 1", marker='o', linewidth=2, color = "#0066ff")
    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14, 15, 16], [-50, -52, -52.1, -48.5, -47.9, -47.5, -47, -47.5, -46.9, -47.4, -46.8, -46.2, -44.1, -42.9, -46.3, -50.1, -52.6], label='Tag 2', marker='o', linewidth=2, color = "#ff0066")
    plt.axis([-0.5, 16.5, -60, -40])
    plt.grid(b=True, which='major', color='#666666', linestyle=':')
    plt.ylabel('RSSI (dBm)', fontfamily = "Times", fontsize = "18")
    plt.xlabel('Finger touch location (cm)', fontfamily = "Times", fontsize = "18")
    plt.legend()
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
