import random
from matplotlib import pyplot as plt
import numpy as np

def neighbor_for_nstate(state):
    count = 0
    neighborhoods = []
    for i in range(state):
        for j in range(state):
            neighborhoods.append((i,j))
            count+=1
    return neighborhoods
    
def lookuptable(state, rule_number, ifprint=False):
    in_ternary = np.base_repr(rule_number, base=state)[::-1]
    lookup_table ={}
    neighborhoods = neighbor_for_nstate(state)
    for i in range(state**2):
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
    def __init__(self, state, rule_number, initial_condition):
        for i in initial_condition:
            if i not in np.arange(state):
                raise ValueError("incorrect initial condition")
        self.lookup_table = lookuptable(state, rule_number)
        self.initial = initial_condition
        self.spacetime = [initial_condition]
        self.current_configuration = initial_condition.copy()
        self.state = state
        
        
    def evolve (self, time_steps, ifplot):
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
        if ifplot == True:
            plt.figure(figsize=(10,10))
            plt.imshow(self.spacetime, cmap=plt.cm.ocean, interpolation='nearest')
            plt.show()
