import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    m = np.linspace(0,10,100)
    x = np.array([5.19613147, 5.91648112, 3.07644914, 0.59126848, 3.1200756 , 9.00650479, 6.90781348, 1.22444135, 2.86697158, 4.8806087 ])
    l1_norm = np.array([np.abs(x - mi).sum() for mi in m])
    
    x_sorted = x
    x_sorted.sort()
    target_m = x_sorted[len(x) // 2]

    x_viz = np.array([np.abs(x - xi).sum() for xi in x_sorted])
    
    y = np.abs(x - target_m).sum() * np.ones(len(m))
    fig = plt.figure()
    plt.plot(m, l1_norm, label='L1-norm')
    plt.plot(m, y, '--', label='minimum')
    plt.plot(x, x_viz, 'o', label=r'$x_i$')
    plt.grid(1)
    plt.legend()
    plt.xlabel('m')
    plt.ylabel('L1-norm')
    fig.savefig('__pycache__/{}.svg'.format(os.path.splitext(__file__)[0]))
    plt.show()
