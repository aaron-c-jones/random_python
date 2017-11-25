import numpy as np
import matplotlib.pyplot as plt

def random_walk(walk_length):
    list_of_sums = []
    x = np.random.choice([-1, 1], size = walk_length, replace = True, p = [0.5, 0.5])

    for step in range(len(x)):
        value = np.sum(x[0:(step+1)])
        list_of_sums.append(value)

    return x, list_of_sums

samples, walk = random_walk(1000)

plt.plot(walk)
plt.title('Random Walk')
plt.xlabel('Step Number')
plt.ylabel('Sum')
plt.axhline(y = 0, color = 'red')
plt.show()
