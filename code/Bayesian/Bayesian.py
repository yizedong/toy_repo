import numpy as np
import scipy.stats
from matplotlib import pyplot as plt


def x_prob(x_sample, a):
    x_sample = np.array(x_sample)
    Pax = 1
    for _x in x_sample:
        N = np.sqrt(np.log(a)/2*np.pi)
        Pxa = N * a**(-_x**2 / 2)
        #Px = scipy.stats.norm(center, dev).pdf(x)
        Pa = 1
        Pax = Pax * Pxa * Pa
    return Pax
center = 0
dev = 1
nx = 100
x_sample = np.random.normal(center, dev, nx)
a = np.linspace(1, 10, 1000)
Pax = x_prob(x_sample=x_sample, a=a)
plt.figure()
plt.plot(a, Pax)

a0 = 1
_a_t = a0
a_t = [a0]
t = [0]
nstep = 5000
for step in np.arange(nstep):
    a_prime = np.random.normal(_a_t, 0.3, 1)
    prob_ratio = x_prob(x_sample=x_sample, a=a_prime) / x_prob(x_sample=x_sample, a=_a_t)
    A = np.min([1, prob_ratio])
    if A >= np.random.uniform(0, 1):
        _a_t = a_prime
    a_t.append(_a_t)
    t.append(step + 1)
plt.figure()
plt.plot(t, a_t)
plt.figure()
plt.hist(a_t, bins=50, density=1)
plt.plot(a, Pax/np.trapz(Pax, a))
plt.show()