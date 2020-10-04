import matplotlib.pyplot as plt
import os
import numpy as np
from fast_basis import *

if __name__ == "__main__":
    np.set_printoptions(precision=5, linewidth=np.inf)
    resolution = 200
    t = np.linspace(-1, 9, resolution, endpoint=False)
    degree = 2
    knot_vector = np.linspace(0, 7, 8)
    sb = scopeBound(knot_vector, t, degree)

    b2 = basisMat(knot_vector, t, degree)
    cp = np.array([1.2,0.8,1.1,1.2,1.1])
    sp = cp.dot(b2)
    plt.grid(1)
    
    plt.xlabel('t')
    plt.ylabel(r'$S(t)$')
    for i in range(len(knot_vector) ):
        if i < len(knot_vector) - 3:
            plt.plot(t, b2[i] , '-', label=r'$B_{%d,2}(t)$'%(i))
            plt.plot(t, b2[i]* cp[i], '--C5', alpha=1)
            plt.annotate(r'${}$'.format(cp[i]), xy=(i + 1.25, 0.65))
        plt.annotate(r'$k_{}$'.format(i), xy=(i, -0.1))
    plt.plot(t, sp, 'C5', label=r'$S_2(t)$')
    plt.plot(knot_vector, [0] * len(knot_vector), 'gx', markersize=8, markeredgewidth=3, label='knots')
    plt.annotate('Weight:', xy=(-0.5, 0.65))
    plt.plot(0, -0.1)
    plt.legend()
    fig = plt.gcf()
    fig.savefig('__pycache__/{}.svg'.format(os.path.splitext(__file__)[0]))
    plt.show()
    