import numpy as np
import scipy.stats
from matplotlib import pyplot as plt


def x_prob(nx, a):
    center = 0
    dev = 1
    x = np.random.normal(center, dev, nx)
    Pax = 1
    for _x in x:
      N = np.sqrt(np.log(a)/2*np.pi)
      Pxa = N * a**(-_x**2 / 2)
      #Px = scipy.stats.norm(center, dev).pdf(x)
      Pa = 1
      Pax = Pax * Pxa * Pa
    return Pax
a = np.linspace(1, 10, 1000)
Pxa = x_prob(nx=100, a=a)
plt.plot(a, Pxa)
plt.show()

a0 = 1
a_prime = a0
t = 0
nstep = 100
for step in np.arange(nstep):
    _a = np.random.normal(a_prime, 1, 1)