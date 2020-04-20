import random
from matplotlib import pyplot as plt
import numpy as np

def neighbor_for_nstate(nstate):  # The variable 'nstate' defines the number of state
    neighborhoods = []
    for i in range(nstate):
        for j in range(nstate):
            neighborhoods.append((i,j))
    return neighborhoods
    
def lookuptable(nstate, rule_number, ifprint=False):
    in_ternary = np.base_repr(rule_number, base=nstate)[::-1]
    lookup_table = {}
    neighborhoods = neighbor_for_nstate(nstate)
    for i in range(nstate**2):
        key = neighborhoods[i]
        try:
            val = in_ternary[i]
        except IndexError:
            val = '0'
        lookup_table.update({key: val})
    if ifprint == True:
        for key, val in lookup_table.items():
            print(key, '-->', val)
    return lookup_table

class ECA(object):
    '''
    Elementary cellular automata simulator.
    '''
    def __init__(self, nstate, 
                 rule_number, initial_condition):
        for i in initial_condition:
            if i not in np.arange(nstate):
                raise ValueError("incorrect initial condition")
        self.lookup_table = lookuptable(nstate, rule_number)
        self.initial = initial_condition
        self.spacetime = [initial_condition]
        self.current_configuration = initial_condition.copy()
        self.nstate = nstate
        
        
    def evolve (self, time_steps):
        for t in range(time_steps):
            new_configuration = []
            for i in range(len(self.initial)):
                
                neighborhood = (self.current_configuration[(i-1)], 
                                self.current_configuration[i])
                
                new_configuration.append(int(self.lookup_table[neighborhood]))
            # update the current configuration    
            self.current_configuration = new_configuration # here we don't want to keep making new copies, so use '='
            # add the new configuration to the spacetime field
            self.spacetime.append(new_configuration)
        return self.spacetime


length = 20
time = 20
rule_number = 38
state = 3
initial_condition = []
for i in range(length):
    initial_condition.append(random.randint(0,state-1))
print('initial_condition is: ', initial_condition)

CA_three = ECA(nstate=3, rule_number=38, initial_condition=initial_condition)
spacetime = CA_three.evolve(20)
plt.figure(figsize=(10,10))
plt.imshow(spacetime, cmap=plt.cm.ocean, interpolation='nearest')
plt.show()