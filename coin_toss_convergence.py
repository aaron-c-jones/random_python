import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def coin_toss(number_of_flips):
    average = []
    flip = np.random.choice([0, 1], size = number_of_flips, replace = True, p = [0.5, 0.5])

    for toss in range(len(flip)):
        value = np.mean(flip[0:(toss + 1)])
        average.append(value)

    return flip, average

flip100, average100 = coin_toss(100)
flip500, average500 = coin_toss(500)
flip1000, average1000 = coin_toss(1000)
flip10000, average10000 = coin_toss(10000)

### animated presentation of moving average coming from different numbers of flips
y = [average100, average500, average1000, average10000]
axis = [[0, 100, 0, 1], [0, 500, 0, 1], [0, 1000, 0, 1], [0, 10000, 0, 1]]
title = ['100 Flips', '500 Flips', '1000 Flips', '10000 Flips']
position = [0, 0, 0, 0]
adjust = [10, 50, 100, 1000]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = True)
ax = [ax1, ax2, ax3, ax4]

def update(current):
    if current == 100:
        a.event_source.stop()

    for i in range(len(ax)):
        ax[i].cla()
        ax[i].plot(y[i][:100 * current])
        ax[i].axhline(y = 0.5, linestyle = 'dashed', linewidth = 1, color = 'black')
        ax[i].axis(axis[i])
        ax[i].annotate(title[i], [position[i] + adjust[i], 0.9])

    plt.suptitle('Moving Average - Coin Toss Example')

a = animation.FuncAnimation(fig, update, interval = 100)