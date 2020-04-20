import numpy as np
from matplotlib import pyplot as plt

def x_prob(x_sample, a):
    """
    Calculate P(a|x) given 'a' and sample 'x'

    Parameters:	
    -----------
    x_sample : array_like
    Input array to be the data sample.
    a : array_like
    Calculate P(a|x) for a range of 'a'

    Returns:	
    --------
    Pax : array_like
    P(a|x)

    """
    x_sample = np.array(x_sample)
    Pax = 1 #initialize P(a|x)
    for _x in x_sample:
        N = np.sqrt(np.log(a)/2*np.pi) #Normalization factor
        Pxa = N * a**(-_x**2 / 2) #P(x|a)
        Pa = 1 #P(a) is independent of 'a'
        Pax = Pax * Pxa * Pa 
    return Pax

#make a plot for question 4)
center = 0
var = 1
nx = 100 #sample number of 'x'
x_sample = np.random.normal(center, var, nx) #generate sample 'x'
a = np.linspace(1, 10, 1000) #define the range of 'a'
Pax = x_prob(x_sample=x_sample, a=a)
plt.figure()
plt.title('P(a|x)')
plt.plot(a, Pax)
plt.xlabel('a')
plt.ylabel('P(a|x)')
plt.savefig('P(a|x)')

def MCMC(a0, a_var, nstep=500):
    """
    Perform MCMC

    Parameters:	
    -----------
    a0 : float
    Intial value of 'a'
    a_var : float
    Variance for the generating function
    nstep: int, optional
    The number of steps for MCMC

    Returns:	
    --------
    t : array_like
    Record of the step number
    a_t : array_like
    The value of a in each step

    """ 
    _a_t = a0 
    a_t = [a0]
    t = [0]
    for step in np.arange(nstep):
        a_prime = np.random.normal(_a_t, a_var, 1)
        prob_ratio = x_prob(x_sample=x_sample, a=a_prime) / x_prob(x_sample=x_sample, a=_a_t)
        A = np.min([1, prob_ratio])
        if A >= np.random.uniform(0, 1):
            _a_t = a_prime
            a_t.append(_a_t)
            t.append(step + 1)
    return t, a_t


t, a_t = MCMC(a0=1, a_var=0.3, nstep=5000)

#make a plot for question 6)
plt.figure()
plt.title('Trace Plot')
plt.plot(t, a_t)
plt.xlabel('step')
plt.ylabel('a')
plt.savefig('Trace_Plot.png')

#make a plot for question 7)
plt.figure()
plt.title('Histgram from Trace Plot')
plt.hist(a_t, bins=50, density=1, label='Histgram from Trace Plot')
plt.plot(a, Pax / np.trapz(Pax, a), label='Normalized P(a|x)')
plt.legend()
plt.xlim(0, 7)
plt.xlabel('a')
plt.ylabel('P(a|x)')
plt.savefig('Histgram_from_Trace_Plot')
plt.show()