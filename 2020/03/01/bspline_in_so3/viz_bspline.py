import matplotlib.pyplot as plt
import os
import numpy as np
from fast_basis import *

if __name__ == "__main__":
    np.set_printoptions(precision=5, linewidth=np.inf)
    resolution = 200
    t = np.linspace(-2, 11, resolution, endpoint=False)
    knot_vector = np.linspace(0, 9, 4)
    degree = 2

    b1 = basisMat(knot_vector, t, degree - 1)
    b2 = basisMat(knot_vector, t, degree)
    sb = scopeBound(knot_vector, t, degree)

    plt.plot(0, -0.2)
    px = 4
    p02 = (px,13/18)
    p01 = (px,2/3)
    p11 = (px,1/3)
    plt.plot([4,4], [0,13/18], 'k-')
    plt.plot([0,0], [0,0.13], 'k-')
    plt.plot([9,9], [0,0.13], 'k-')

    plt.annotate(r' $P_{0,2}$', xy=p02, fontsize=14)
    plt.annotate(r' $P_{0,1}$', xy=p01, fontsize=14)
    plt.annotate(r' $P_{1,1}$', xy=p11, fontsize=14)

    plt.annotate(s='', xy=(0,1/9), xytext=(4,1/9),
        arrowprops=dict(arrowstyle='<|-|>', facecolor='black'))
    plt.annotate(s='', xy=(9,1/9), xytext=(4,1/9),
        arrowprops=dict(arrowstyle='<|-|>', facecolor='black'))
    plt.annotate(r'$w_0$', xy=(2, 0.13), fontsize=14)
    plt.annotate(r'$w_1$', xy=(6, 0.13), fontsize=14)

    plt.annotate(r' $P_{0,2} = \frac{w_0}{k_2 - k_0}P_{1,1} + \frac{w_1}{k_3 - k_1}P_{0,1}$',
        xy=(0,-0.20), fontsize=16)

    for i in range(len(knot_vector)):
        if i < len(knot_vector) - 2:
            plt.plot(t, b1[i], label=r'$B_{%d,1}(t)$'%(i))
        if i < len(knot_vector) - 3:
            plt.plot(t, b2[i], label=r'$B_{%d,2}(t)$'%(i))
        plt.annotate(r'$ k_{}$'.format(i), (knot_vector[i], -0.07), fontsize=14)
    
    plt.plot(*p02, 'bo')
    plt.plot(*p01, 'ro')
    plt.plot(*p11, 'ro')
    plt.plot(px, 0, 'k_', markersize=10)

    knot_2d = np.vstack([knot_vector, [0] * len(knot_vector)])
    plt.plot(*knot_2d , 'gx', markersize=8, markeredgewidth=2, label='knot')

    plt.grid(1)
    plt.legend()
    plt.xlabel('t')
    plt.ylabel(r'$B(t)$')
    fig = plt.gcf()
    fig.savefig('__pycache__/{}.svg'.format(os.path.splitext(__file__)[0]))
    plt.show()