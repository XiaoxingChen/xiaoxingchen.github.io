import matplotlib.pyplot as plt
import os
import numpy as np
from fast_basis import *

if __name__ == "__main__":
    np.set_printoptions(precision=5, linewidth=np.inf)
    resolution = 200
    t = np.linspace(-2, 11, resolution, endpoint=False)
    knot_vector = np.linspace(0, 9, 10)
    degree = 3
    order = degree + 1

    b = [basisMat(knot_vector, t, i) for i in range(degree + 1)]
    tops = [(0.5, 1), (0.9, 0.9), (1.4, 0.75), (1.8, 0.65)]

    plt.figure(figsize=(10,5))

    
    for p in range(degree + 1):
        for i in range(len(knot_vector)):
            if i < len(b[p]):
                plt.plot(t, b[p][i], 'C{}'.format(p), linewidth=1 + 0.5 * p, label=None if i else r"$B_{i,%d}(t)$"%(p))
            if 0 == p:
                plt.annotate(r'$k_{}$'.format(i), xy=(i, -0.1), fontsize=14)        
        plt.annotate('degree {}'.format(p), xytext=(-2, 0.9 - 0.2 * p), xy=tops[p], \
            arrowprops=dict(arrowstyle='->'))
    plt.plot(knot_vector, [0] * len(knot_vector), 'gx', markersize=8, markeredgewidth=3, label='knots')
    plt.plot(0, -0.1)

    plt.grid(1)
    plt.legend()
    plt.xlabel('t')
    plt.ylabel(r'$B(t)$')
    fig = plt.gcf()
    fig.savefig('__pycache__/{}.svg'.format(os.path.splitext(__file__)[0]))
    plt.show()